# import datetime
# n = 10000000
# count = 1
# Prime_list = [2]
# start = datetime.datetime.now()
# for x in range(3,n,2):
#     for i in range(2,int(x**0.5)+1):
#         if x % i == 0:
#             break
#     else:
#         count += 1
#         # Prime_list.append(x)
# delta = (datetime.datetime.now()-start).total_seconds()
# print(delta)
# print(count)
# print(Prime_list)
#######################################################
# n = 100
# count = 1
# Prime_list = [2]
# for x in range(3,n,2):
#     for i in range(3,int(x**0.5)+1,2): #奇数/偶数必不能整除，因此没有必要除偶数
#         if x % i == 0:
#             break
#     else:
#         count += 1
#         # Prime_list.append(x)
# print(count)
# # print(Prime_list)
#######################################################
import datetime
n = 10000000
count = 1
Prime_list = [2]
start = datetime.datetime.now()
for x in range(3,n,2):
    t = x ** 0.5
    for i in Prime_list: #直接用质数列表检验整除
        if x % i == 0:
            break
        if i > t:
            count += 1
            Prime_list.append(x)
            flag = 1
            break
delta = (datetime.datetime.now()-start).total_seconds()
print(delta)
print(count)
# print(Prime_list)
#######################################################
import datetime
n = 10000000
count = 2
Prime_list = [2,3]
x = 5
step = 2
start = datetime.datetime.now()
while x < n:
    t = x**0.5
    for i in Prime_list:
        if x % i == 0:
            x += step
            if step == 2:
                step = 4
            else:
                step = 2
            break
        if i > t:
            count += 1
            Prime_list.append(x)
            x += step
            if step == 2:
                step = 4
            else:
                step = 2
            break
delta = (datetime.datetime.now()-start).total_seconds()
print(delta)
print(count)
# print(Prime_list)




