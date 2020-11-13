import pandas as pd
import re
import timetransformer as tf


def df_clear2(df, domainname, date):
#    date0 = date.split('T',1)[0].replace('-', '/')
    date0 = tf.transform_utc_to_date(date)
    col_name = df.columns.tolist()
    col_name.insert(1, 'doname')

    df.reindex(columns=col_name)

    pattern = r"https://(.*\.com)/"
    df['doname'] = df[8].apply(lambda x: re.match(pattern, x).group(1))

    df[3] = df[3].apply(lambda x: x.split(':', 1)[0])

    num = df_column_data_num(df, 'doname', domainname)

    df1 = df.loc[df[3] == date0]

    return df1, num


def df_clear(df):
    """
    功能：清洗dataframe
    :param df: dataframe
    :return: dataframe,flag_is_repeat
    """
    flag_is_repeat = df_column_is_repeat(df, 3)

    col_name = df.columns.tolist()
    col_name.insert(1, 'doname')

    if flag_is_repeat:  # 有重复值就增加date_s这一列
        col_name.insert(2, 'date_s')

    df.reindex(columns=col_name)

    pattern = r"https://(.*\.com)/"
    df['doname'] = df[8].apply(lambda x: re.match(pattern, x).group(1))

    if flag_is_repeat:   # 有重复值，给data_s这一列填充值
        df['date_s'] = df[3].apply(lambda x: tf.transform_date_to_s(x))
    else:   # 没有重复值，把3列设为时间索引
        df[3] = pd.to_datetime(df[3], format="%d/%b/%Y:%H:%M:%S")
        df.set_index(3, inplace=True)
        return df, flag_is_repeat
    return df, flag_is_repeat


def df_column_is_repeat(df, clname):
    """
    功能：判断df的clname列是否有重复值
    :param df: dataframe
    :param clname: 列名
    :return: True 有重复值，False 没有重复值
    """
    before = df.shape[0]
    df1 = df[clname].drop_duplicates()
    after = df1.shape[0]
    n_dup = before - after
    if 0 == n_dup:
        return False
    return True


def df_column_data_num(df, clname, data):
    """
    查询df的clname列里data出现的次数
    """
    df1 = df[clname].value_counts()
    try:
        num1 = df1[data]
    except KeyError:
        print('dont has the domain name: %s ,KeyError: ' % 'domain1.com', KeyError)
        num1 = 0
    return num1


def df_column_date(df, clname, date):
    """
    根据df的clname列截取日期为date的当日数据
    参数  df：dataframe
         clname: df某一列的列名
         date：utc时间字符串，格式为 2011-02-26T15:20:00Z
    返回值：df
    """
    num1 = tf.transform_utc_to_s(date)
    num2 = num1 + 86400

    return df.loc[(num1 <= df[clname]) & (df[clname] < num2)]


def df_column1_column2_date(df, clname1, clname2, date):
    """
    功能：根据df的column1列在date当日内的数据，截取column2的数据
    参数  df：dataframe
         clname1：df限定条件列
         clname2：df被截取的列
         date：utc时间字符串，格式为 2011-02-26T15:20:00Z
    返回值：df
    """
    num1 = tf.transform_utc_to_s(date)
    num2 = num1 + 86400

    return df.loc[(num1 <= df[clname1]) & (df[clname1] < num2), clname2]


def main():
    pass


if __name__ == "__main__":
    main()