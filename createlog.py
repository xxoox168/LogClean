import timetransformer as tt
import random

filePath = "./"
fileName = "create2.log"
date = "28/Feb/2019:13:17:10"
number = 10000000
period = 360

def create_log(filePath,fileName,date,number,period):
    """
    功能：在路径filePath下，生成日志文件fileName,开始时间时date当日00:00:00,共生成number条
    :param filePath: 生成文件路径
    :param fileName: 生成文件名字
    :param date: 生成日志起始日期
    :param number: 生成日志条数
    :param period: 日志时间间隔
    :return: 无
    """

    str1 = "47.29.201.179 - - ["
    str2 = " +0000] \"GET /?p=1 HTTP/2.0\" "
    str3 = " 5316 \""
    str4 = "\" \"Mozilla/5.0 (Window s NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36\" \"2.75\""
    strlist = ["https://domain1.com/?p=1","https://domain2.com/?p=1","https://baidu.com/?p=1","https://google.com/?p=1"]
    statuslist = ["200", "404", "505", "504", "303"]

    date = tt.transform_date_to_s(date)
    with open(filePath + fileName, "w") as f:
        for i in range(number):
            date1 = date + i*period
            date1 = tt.transform_s_to_date(date1)
            str5 = random.choice(strlist)
            status = random.choice(statuslist)
            str = str1 + date1 + str2 + status + str3 + str5 + str4 + "\n"

            f.write(str)



def main():
    #tt.transform_date0_to_s("26/02/2011")
    #str = "+0000] \"GET /?p=1 HTTP/2.0\" 2"
    #print(str)
    create_log(filePath, fileName, date, number, period)



if __name__ == "__main__":
    main()
