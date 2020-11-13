import pandas as pd
import dfmanage as dfm
import configparser


def read_file(filepath, filename, chunksize, domainName, date):
    """
    功能：读取txt文件，清洗成固定格式后以dataframe格式输出
    :param filepath: 源文件路径
    :param filename: 源文件名
    :return: dataframe
    """
    mylist = []
    num = 0
    reader = pd.read_csv(filepath + filename, header=None, names=range(11), sep=' ', chunksize=chunksize)
    for chunk in reader:
        chunk.astype(str)
        chunk.drop([0, 1, 2, 4, 5, 7, 9, 10], axis=1, inplace=True)
        chunk[3] = chunk[3].apply(lambda x: x[1:])
        df, num1 = dfm.df_clear2(chunk, domainName, date)
        mylist.append(df)
        num = num + num1
        print('****************************')
        print('本批次%s请求的次数：%d' % (domainName, num1))
        print('目前%s请求的总次数：%d' % (domainName, num))
        # print(df.head(5))

    temp_df = pd.concat(mylist, axis=0)
    del mylist

    return temp_df, num


def cal_rate1(df):
    """
    功能：统计df的6列里出现200的比例
    :param df:
    :return:
    """
    sum0 = df.shape[0]
    if sum0 == 0:
        num = 0
        rate = 0
        # print('%s 所在日0个请求' % date0)
    else:
        num = dfm.df_column_data_num(df, 6, 200)
        rate = float(num) / float(sum0)
    return sum0, num, rate


def read_config():
    """
    功能：读取配置文件config.cfg
    :return: 参数字典
    """
    config = configparser.ConfigParser()
    print("- Empty config %s" % config.sections())

    print("- Load config file")
    config.read("./config.cfg")
    # 此处返回的sections list不包括 default
    print("> config sections : %s" % config.sections())
    # 读取配置文件中 [DEFAULT]
    return config['default']


def main():
    config = read_config()
    filepath = config['default_filepath']
    filename = config['default_filename']
    domainname = config['default_domainname']
    date = config['default_date']
    chunksize = int(config['default_chunksize'])

    df, num = read_file(filepath, filename, chunksize, domainname, date)   # 读取日志文件清洗后输出dataframe

    print("以 %s 为域名的HTTPS请求有 %d 个." % (domainname, num))

    sum0, num1, rate = cal_rate1(df)
    date1 = date.split('T', 1)[0]
    if 0 == sum0:
        print('%s 所在日0个请求' % date1)
    else:
        print('%s日，共%d次请求，成功%d次，成功率为：%.2f' % (date1, sum0, num1, rate))


if __name__ == "__main__":
    main()
