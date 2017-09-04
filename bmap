#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# written by Python program:
# 功能：获取百度地图某市某关键字获取多少条数据；返回name,address,telephone共3个字段保存到 Result.txt 文件中，会产生一个temp.txt临时文件；
# 用法：python bmap.py 城市 关键字 ...


import sys,urllib2,time,json,csv

reload(sys)
sys.setdefaultencoding('utf8')


# 参数数量少于3个时报错退出；
if len(sys.argv) < 3:
    print "Error: arguments number is wrong. \nUsage: <programName> <city> <keywords> ..."
    exit(-1)


# argv[1]:城市，argv[2]:关键字字符串，argv[3]：默认获取的数据条数*10；
arg1=sys.argv[1]
arg2=sys.argv[2]
arg3=100


# 拼装关键字列表
keywords=list()
print "\n参数数量：",len(sys.argv)
for i in range(2,len(sys.argv)):
    keywords.append(sys.argv[i])


# 拼装文件名
resultFileName = sys.argv[1]
keyword=""
for k in keywords:
    keyword += k+','
    resultFileName += '_'+k
print "关键字："+ keyword
resultFileName += '_'+ time.strftime('%Y%m%d',time.localtime(time.time())) +'.txt'
print '文件名：'+ resultFileName


# 开始收集数据。。。
print '\n开始收集数据。。。'
count=0
# 填充表头字段
string2="序号\t名称\t地址\t电话\t关键字\r\n"
with open(resultFileName, 'w') as f:
    f.write(string2)

# 在当前城市按每个关键字提取前500条内容
for keyword in keywords:
    for i in range(arg3):
        # 拼装每页获取10条数据的url
        url = 'http://api.map.baidu.com/place/v2/search?q=' +keyword+ '&region=' +sys.argv[1]+ '&page_size=10&page_num=' + str(i)+ '&output=json&ak=<Baidu Api Key>'

        # 使用json库加载数据为字典格式
        data = urllib2.urlopen(url)
        dict_i = json.loads(data.read())

        # 如果没有数据，直接跳出该关键字循环
        if int(dict_i['total']) == 0:
            break

        # 遍历取出10条字典数据里面的name,address,telephone共3个字段的数据
        string2 = ""
        for i2 in range(0, len(dict_i['results'])):
            print  str(count+1) + u"\t" + dict_i['results'][i2].get('name','None') + u"\t" + dict_i['results'][i2].get('address','None') + u"\t" + dict_i['results'][i2].get('telephone','None') + u"\t" + keyword
            string2 += str(count+1) + u"\t" + dict_i['results'][i2].get('name','None') + u"\t" + dict_i['results'][i2].get('address','None') + u"\t" + dict_i['results'][i2].get('telephone','None') + u"\t" + keyword + "\r\n"
            i2 += 1
            count += 1

        # 获取到的数据马上附加写入文件中
        with open(resultFileName,'a') as f:
            f.write(string2)


print '成功收集了 %s 条数据' % count
print '文件名：%s' % resultFileName
