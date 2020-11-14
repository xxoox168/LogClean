# LogClean
clean log file

# 项目背景：
    现有Nginx服务器日志文件大约1000万行，其中一行如下：
    47.29.201.179 - - [28/Feb/2019:13:17:10 +0000] "GET /?p=1 HTTP/2.0" 505 5316 "https://domain1.com/?p=1" "Mozilla/5.0 (Window s NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36" "2.75"
    需要统计以下指标：
        1. 计算https请求有多少个是以domain1.com为域名
        2. 给定一个日期 date ，根据http状态码计算当日（UTC时间），所有请求中成功的比例

# 使用方法：
    1.createlog.py是生成log日志的程序，在终端直接运行./createlog.py，默认会按360s间隔生成1000万条数据的log文件。生成文件位置、间隔时间、总条数可以在程序里更改
    2.logchunk.py是清洗并分析统计的程序，在终端直接运行./logchunk.py，会读取log文件并统计指标，统计结果会在终端打印出来。读取文件的位置、文件名称、统计的域名、统计的日期可以在配置文件config.cfg里更改
