# -*- coding: cp936 -*-
"""
��Ŀ����֪2016��1��1�������壬���д��ӡĳ���������ĺ���
printCalendar(month)���ú������ݴ��ݵ�month�·ݣ���ʾ
����ʽ��ӡ�������������д�������������д�ĺ�����ȷ�ԡ�
���磺���·ݵ�����������Ϊ��
  �� һ �� �� �� �� ��
     1  2  3  4  5  6
  7  8  9 10 11 12 13
 14 15 16 17 18 19 20
 21 22 23 24 25 26 27
 28 29
"""

first_weekday = 5 # ����ݵ�һ������5
days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # ÿ���µ�����
def printCalendar(month):
      # ����month�·ݵ�һ�������ڼ�
      t=days[month-1]
      s=0
      for i in range(0,month-1,1) :
        s=s+days[i]
      k=(s-2)%7
      p=[[],[],[],[],[],[]]
      j=(t-(7-k))//7
      b=t-(7-k)-7*j

      # ������µ�ÿһ�������ڼ�
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
      

      


      # ��ӡ���⣨��һ������������
      print('��\tһ\t��\t��\t��\t��\t��')

      # �������
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
      
# �����Ƿ���ȷ��һ���������������2�·�����
month = 2
printCalendar(month)

"""
# �����Ƿ���ȷ�ڶ����������������ȫ����·�����
monthNames = ['һ��', '����', '����', '����', '����', '����', '����', '����', '����', 'ʮ��', 'ʮһ��', 'ʮ����']
for month in range(1, 12+1):
      print ('       ', monthNames[month-1])
      printCalendar(month)
"""
