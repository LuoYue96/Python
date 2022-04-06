# # Author：LuoYue
# import re
# a = re.match("c723.+","c1234553ddd")    #match方法会从string的起始位置开始匹配
# a.group()
#输入一串字符（空格分开） 输出最后一个字符的长度
# a = input("ddd: ")
# print(len(a.split()[-1]))
#计算某个字符的出现次数
# str = input().lower()
# a = input().lower()
# print(str.count(a))
#明明的随机数
# count = int(input("输入个数： "))
# list_var = []
# for i in range(count):
#     a = int(input())
#     list_var.append(a)
# for i in sorted(set(list_var)):
#     print(i)
#字符串分隔
# str = input("input your number: ")
# var = len(str)//8
# if len(str)%8 != 0 :
#     var+=1
# for i in range(var):
#     if len(str)<8:
#         str = str.ljust(8,'0')
#     print(str[0:8])
#     str = str[8:]
#求int型正整数在内存中存储时1的个数
# var = bin(int(input()))
# print(var.count('1'))
#购物单
var1 = input().split()
dict1 = {}
dict2 = {}
for i in int(var1[1]):
    var2 = input()
    dict1[int(var2[0])] = dict2[int(var2[1])]
    dict2[int(var2[2])] = int(var2[2])
tmp1, tmp2 = 0
for i in dict1.keys():
    for j in dict2.keys():


