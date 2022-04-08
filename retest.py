# # Author：LuoYue
#HJ字符串最后一个单词长度
#输入一串字符（空格分开） 输出最后一个字符的长度
# a = input("ddd: ")
# print(len(a.split()[-1]))

#HJ2计算某个字符的出现次数
# str = input().lower()
# a = input().lower()
# print(str.count(a))

#HJ3明明的随机数
# count = int(input("输入个数： "))
# list_var = []
# for i in range(count):
#     a = int(input())
#     list_var.append(a)
# for i in sorted(set(list_var)):
#     print(i)

#HJ4字符串分隔
# str = input("input your number: ")
# var = len(str)//8
# if len(str)%8 != 0 :
#     var+=1
# for i in range(var):
#     if len(str)<8:
#         str = str.ljust(8,'0')
#     print(str[0:8])
#     str = str[8:]

#HJ5进制转换
# hex = input()
# dict = {"A":10,
#         "B":11,
#         "C":12,
#         "D":13,
#         "E":14,
#         "F":15}
# lenth = len(hex)
# total = 0
# for i in range(lenth-2):
#         tpm=0
#         if hex[i+2] in dict.keys():
#                 tpm = dict[hex[i+2]]*16**(lenth-3-i)
#         else:
#                 tpm = int(hex[i+2])*16**(lenth-3-i)
#         total+=tpm
# print(total)
#Python内置函数一句解决转换，  print(int(input(),16))

#HJ6质数因子
# import math
# n = int(input())
# for i in range(2, int(math.sqrt(n))+1):
# 	# 一个数可以被它所有的质因子表示
#     # 这里仅考虑不大于根号下n的因子
#     # 因为当n被所有不大于根号下n的【质】因子整除后，要么余1，要么余2，要么会剩下一个且仅会剩下一个大于等于根号下n小于等于n的质数（不可能出现两个不相等且同时大于根号下n的质因子a和b，这会导致a*b>n）
#     while n % i == 0:
#         # 第一个能被整除的一定是最小的质数因子（如果是合数，一定有2<=x<i的质因子x）
#         # 后续能被整除的也一定是质数，若是合数，则合数的质因子肯定出现在之前，不成立
#         print(i, end=' ')  # 得到的每个i都是n的质因子（即列举重复的质因子）
#         n = n // i  # n不断变小，确保没有i这个质因子
#         # 双除号：输出整数
# if n > 2:
#     print(n)

#HJ7取近似值
#tmp = float(input())
#方法1：思路字符串切片，通过index取'.'的索引，随后判断其后的数字是否大于5
# cn = tmp.index('.')
# if int(tmp[cn+1]) >= 5 :
#     print(int(tmp[:cn])+1)
# else:
#     print(tmp[:cn])
#方法2：网友，思路通过float（）和int（）做差与0.5比较
# if tmp - int(tmp) >=0.5:
#     print(int(tmp)+1)
# else:
#     print(int(tmp))
#方法3  直接给+0.5 然后int  因为int一个浮点数会直接舍弃小数部分，
# n = float(input())
# y = lambda x :int(x+0.5)
# print(y(n))

#HJ8合并表记录
# n = int(input())
# dictn = {}
# tmp=[]
# for i in range(n):                #循环收集输入信息
#     var = input().split()             #切片 分出key value
#     if var[0] in dictn.keys():           #向字典中添加key-value 如果已存在即更新，否则添加
#         dictn[var[0]]+=int(var[1])
#     else:
#         dictn[var[0]]=int(var[1])
#     if int(var[0]) not in tmp:    #对输入信息进行收集去重，保留key值，用于输出字典数据时作为排序索引
#         tmp.append(int(var[0]))
# tmp = sorted(tmp)
# for i in tmp :                    #实际字典的key如果为int，可直接对字典进行排序输出
#     print("{} {}".format(i,dictn[str(i)]))
'''网络方法，通过dict.get()来更新字典'''
# n = int(input())
# dictn = {}
# for i in range(n):
#     var = input().split()
#     key = int(var[0])
#     value = int(var[1])
#     dictn[key] = dictn.get(key,0) + value
# for i in sorted(dictn) :
#     print("{} {}".format(i,dictn[i]))

#HJ9提取不重复的整数
# var = list(input())         #因为题目要求将输入的int从右向左读出且不包含重复数字
# var.reverse()               #先将输入的string转化为list，使用reverse反向处理
# tmp = ""                    #通过临时string tmp进行去重
# for i in var:
#     if i not in tmp:
#         tmp+=i
# print(tmp)
'''字符串反向输出还可以用 string[::-1]
a = "231333"
print(a[::-1])
高级处理，先采用set去重，随后根据原string的index进行输出
list1 = list(input()[::-1])
list2 = list(set(list1))
list2.sort(key = list1.index)
print(''.join(list2))'''

#HJ10字符个数统计
#print(len(set(input())))
# print(chr(99))      #chr方法根据输入的ASCII值输出对应的字符
# print(ord('罗'))     #ord与chr反向，输入字符，输出对应的ASCII
a = "sdasd"

#HJ11数字颠倒
#print(input()[::-1])

#HJ12字符串反转
print(input()[::-1])

#HJ13句子逆序
#自写，用到了list的reverse（）
# a = "dsa dss 111 222"
# b=a.split()
# print(b)
# b.reverse()
# for i in b:
#     print(i)
# var = input().split()
#网友  直接list切片逆序赋给另一个列表，然后读出即可
# var2 = var[::-1]
# for i in var2:
#     print(i,end=' ')

#14字符串排序
n = int(input())
var = [1,5,2,3]
for i in range(n):
    var.append(input())
for i in sorted(var):
    print(i)

#HJ15求int型正整数在内存中存储时1的个数
# var = bin(int(input()))
# print(var.count('1'))

#HJ16购物单
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
        
#HJ20密码验证合格程序
import re
while True:
    try:
        var = input()
        tmp = 0
        if len(var) <= 8:
            print("NG")
        else:
            ret = re.search("[0-9]", var)
            if ret != None:
                tmp+=1
            ret = re.search("[a-z]", var)
            if ret != None:
                tmp+=1
            ret = re.search("[A-Z]", var)
            if ret != None:
                tmp+=1
            ret = re.search("\W", var)
            if ret != None:
                tmp+=1
            for j in range(0,len(var)-3):
                tmp2 = var[j]+var[j+1]+var[j+2]
                if var.count(tmp2) >=2:
                    tmp = 0
            if tmp >=3:
                print("OK")
            else:
                print("NG")
    except:
        break

#HJ21简单密码
#自创---在判断是否为大小写时用的时ASCII 太过费劲，python有isupper判断
# var = input()
# dictA = {'abc':2,'def':3,'ghi':4,'jkl':5,'mno':6,'pqrs':7,'tuv':8,'wxyz':9}
# for i in var:
#     if ord(i) in range(65,91):
#         if i == 'Z':
#             print('a',end='')
#         else:
#             print(chr(ord(i.lower())+1),end='')
#     elif ord(i) in range(97,123):
#         for j in dictA.keys():
#             if i in j:
#                 print(dictA[j],end='')
#     else:
#         print(i,end='')

#HJ22汽水瓶
# while True:
#     var = int(input("input num"))
#     if var == 0:
#         break
#     else:
#         tmp=0
#         while var // 3 != 0 :
#             tmp += var // 3
#             var = var //3 + var % 3
#         else:
#             if var == 2 :
#                 tmp+=1
#                 print(tmp)
#                 break
#             else:
#                 print(tmp)
#                 break

#HJ23删除字符串中出现次数最少的字符
#该方法较笨，没有使用dict存储，纯手动处理
var = input()  #用于接收输入
var2 = set(var)    #对接收到的string进行去重
tmp =var.count(var[0])    #取string的第一个字符出现次数作为计数器首个数字
tmp2=''            #用于存储出现次数最少的字符
for i in var2:       
        if tmp > var.count(i):    #如果遍历到的字符出现次数小，即tmp更新
        tmp=var.count(i)
        tmp2=i                #tmp2更新为次数最小的字符
    elif tmp == var.count(i):    #如果出现次数均最小，即tmp2添加该字符
        tmp2+=i
for i in var:                    #遍历原始输入字符串
    if i not in tmp2:        #如果字符不属于tmp2（出现次数最小字符串中），即输出
        print(i,end='')

#HJ27 查找兄弟单词
list1 = input().split()
#单词查询范围 list[1:-2]   目标单词des = list[-2]  输出第list[-1]
list2 = []          #用于存储兄弟单词
des=str(list1[-2])      #用于存储目标单词
for i in list1[1:-2]:       #遍历匹配的单词池
    #通过长度和字符串是否与des一致来删选一部分
    if i != list1[-2] and len(i) == len(list1[-2]):
        tmp=des             #临时变量用于接下来的删减操作
        for j in i:         #遍历筛选后的单词字符串
            if j in tmp:                    #如果遍历的字符存在目标字符中
                tmp=tmp.replace(j,'',1)    
                #在目标字符中删去匹配到的一个，这样操作是为了以防出多个相同字符
        if len(tmp) == 0:           #tmp长度为0则代表全部匹配成功，是兄弟单词
            list2.append(i)         #存储兄弟单词
print(len(list2))                   #输出兄弟单词的个数 即list2的长度
if len(list2) > int(list1[-1]):     
#判断兄弟单词的个数 是否包括想要输出的序号 如果超出则不输出
    list2=sorted(list2)             #对兄弟单词列表进行排序
    print(list2[int(list1[-1])-1])  #输出目标序号的兄弟单词

   
#HJ29字符串加解密
#原始人方法，简单逻辑往里怼
#将一些特殊的转换提前存入字典，方便接下来进行映射解析
dictT={'z':'A','Z':'a','9':'0'}        #加密用      
dictrT={'A':'z','a':'Z','0':'9'}        #解密用
s = input()       
s_r = ''                #用于存储加密输出
r=''                        #用于存储解密输出
rs = input()
for i in s:                        #加密过程，不解释。。应套逻辑
    if i in dictT.keys():            #先从那几个特殊的下手排查 z Z 9
        s_r+=(dictT[i])
    elif i.isdigit():
        s_r+=str((int(i)+1))
    elif i.islower():
        s_r+=(chr(ord(i.upper())+1))
    elif i.isupper():
        s_r+=(chr(ord(i.lower())+1))
    else:
        s_r+=(i)
for j in rs:                        #解密过程，依然硬套逻辑 从特殊的开始反转
    if j in dictrT.keys():
        r+=(dictrT[j])
    elif j.isdigit():
        r+=str((int(j)-1))
    elif j.islower():
        r+=(chr(ord(j.upper())-1))
    elif j.isupper():
        r+=(chr(ord(j.lower())-1))
    else:
        r+=(j)
print(s_r)
print(r)

#HJ31单词倒排
a = input()
tmp = ""        #用于存储转义后的字符串
count=0            #用于计数 计相邻字符是否均为单词间隔符
for i in a:        #遍历输入的字符串
    if i.islower():        #首先判断是否为小写字母
        tmp += i
        count=0            #如果该字符是单词字符，则对计数器进行归0操作
    elif i.isupper():        #其次判断是否为大写字母
        tmp += i
        count=0   
    else:                    #以下判断为单词间隔符
        count+=1            #计数器+1
        if count == 1 :    #当计数器为1时才转换成空格，计数器为0则代表当前字符为单词字符，大于1则代表相邻的两个或多个字符均为单词间隔符
            tmp+=' '    
lista = tmp.split()                #将字符串按空格切割转换成列表
for i in lista[::-1]:            #列表逆序切片输出
    print(i,end=' ')

#HJ34 图片整理
var = input()
for i in sorted(var):
    print(i,end='')
#一行解决  print(''.join(sorted(input())))

#HJ35蛇形矩阵
找到值与行列的关系，即 value=(i+j-2)*(i+j-1)/2+j，i，j是所属行与列。然后判定换行的时机，即j=N-i+1时，所属行已排满，换行
while True:
    try:
        m = int(input())
        for i in range(1, m + 1):
            for j in range(1, m - i + 2):
                if j == m - i + 1:
                    print((i + j - 2) * (i + j - 1) // 2 + j)
                else:
                    print((i + j - 2) * (i + j - 1) // 2 + j, end=' ')
    except:
        break

HJ37 统计每个月兔子的总数
斐波那契数列：1 1 2 3 5 8 13 21 34 f(n)=f(n-1)+f(n-2) n>2,n从0开始
递归法：
while True:
    try:
        month=int(input())
        n=month-1
        def func(n):
            if n<2:#基线条件
                return 1
            else:#递归条件
                return func(n-1)+func(n-2)
        print(func(n))
    except:
        break
2.循环列表
import sys
for s in sys.stdin:#s=input()读入数据的1行
    month=int(s)
    L=[]
    for i in range(month):
        if i<2:#前两个月都为1
            total=1
            L.append(total)
        else:
            total=L[i-1]+L[i-2]#之后均为前两个数的和
            L.append(total)
    print(L[-1])#最后的列表L=[1, 1, 2, 3, 5, 8, 13, 21, 34]

