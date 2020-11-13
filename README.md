# LogClean
clean log file

# 项目背景：
    现有Nginx服务器日志文件大约1000万行，其中一行如下：
    47.29.201.179 - - [28/Feb/2019:13:17:10 +0000] "GET /?p=1 HTTP/2.0" 505 5316 "https://domain1.com/?p=1" "Mozilla/5.0 (Window s NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36" "2.75"
    需要统计以下指标：
        1. 计算https请求有多少个是以domain1.com为域名
        2. 给定一个日期 date ，根据http状态码计算当日（UTC时间），所有请求中成功的比例
