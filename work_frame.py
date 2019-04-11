# -*- coding: cp936 -*-
"""
题目：已知2016年1月1日是周五，请编写打印某个月月历的函数
printCalendar(month)，该函数根据传递的month月份，按示
例格式打印该月月历。请编写代码测试你所编写的函数正确性。
比如：二月份的月历输出结果为：
  日 一 二 三 四 五 六
     1  2  3  4  5  6
  7  8  9 10 11 12 13
 14 15 16 17 18 19 20
 21 22 23 24 25 26 27
 28 29
"""

first_weekday = 5 # 该年份第一天是周5
days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 每个月的天数
def printCalendar(month):
      # 计算month月份第一天是星期几
      t=days[month-1]
      s=0
      for i in range(0,month-1,1) :
        s=s+days[i]
      k=(s-2)%7
      p=[[],[],[],[],[],[]]
      j=(t-(7-k))//7
      b=t-(7-k)-7*j

      # 计算该月的每一天是星期几
      d=1
      for i in range(k,7,1):
          p[0].append(d)
          d=d+1   
      for q in range(1,j+1,1):
          for i in range(0,7,1):
              p[q].append(d)
              d=d+1   
      for i in range(0,b,1):
          p[j+1].append(d)
          d=d+1
      for i in range(b,7,1):
          p[j+1].append('\t')
      

      


      # 打印标题（日一二三四五六）
      print('日\t一\t二\t三\t四\t五\t六')

      # 输出月历
      print('\t'*k,end='')
      for i in range(0,7-k,1):
          print('%d\t' %p[0][i],end="")
      print('\t')    
      for j in range(1,j+1,1):
          for i in range(0,7,1):
              print('%d\t' %p[j][i],end='')
          print('\t')    
      for i in range(0,b,1):
          print('%d\t' %p[j+1][i],end='')
      print('\t'*(6-b))
      
# 函数是否正确第一个测试用例：输出2月份月历
month = 2
printCalendar(month)

"""
# 函数是否正确第二个测试用例：输出全年各月份月历
monthNames = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月']
for month in range(1, 12+1):
      print ('       ', monthNames[month-1])
      printCalendar(month)
"""
