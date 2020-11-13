import time
import datetime


def transform_s_to_date(second):
    """
    功能：输入秒数，输出指定时间格式字符串
    参数：秒数   例如1298674659
    返回值：日/月/年:时:分:秒   例如26/Feb/2011:06:57:39
    """
    timearray = time.localtime(second)  # 秒数
    otherstyletime = time.strftime("%d/%b/%Y:%X", timearray)
    return otherstyletime


def transform_date_to_s(date):
    """
    功能：输入指定时间格式字符串，输出秒数
    参数：字符串，日/月/年:时:分:秒   例如26/Feb/2011:06:57:39
    返回值：秒数   例如1298674659
    """
    t = time.strptime(date, "%d/%b/%Y:%H:%M:%S")
    return int(time.mktime(t))


def transform_date0_to_s(date):
    """
    功能：输入日月年，输出当天0点对应的秒数
    参数：字符串，日/月/年   例如26/02/2011
    返回值：秒数   例如1298649600
    """
    date = date + ":00:00:00"
    t = time.strptime(date, "%d/%m/%Y:%H:%M:%S")
#   print(int(time.mktime(t)))
    return int(time.mktime(t))


def transform_utc_to_date(utc):
    date = utc.split('T', 1)[0]
    date1 = date + ':00:00:00'
    t = time.strptime(date1, "%Y-%m-%d:%H:%M:%S")
    t1 = time.strftime("%d/%b/%Y", t)
    return t1


def transform_utc_to_s(utc):
    """
    功能：输入utc时间字符串，输出当天0点对应的秒数
    参数：字符串 2011-02-26T15:20:00Z，表示2011年2月26号15点20分0秒，Z表示是标准时间
    返回值：秒数
    """
    date = utc.split('T',1)[0]
    date1 = date + ':00:00:00'
    t = time.strptime(date1, "%Y-%m-%d:%H:%M:%S")
    return int(time.mktime(t))


def main():
    print(transform_utc_to_s('2011-02-26T15:20:00Z'))
    pass


if __name__ == "__main__":
    main()