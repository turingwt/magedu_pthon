# num1 = []
# for i in range(3):
#     num1.append(int(input('>>>')))
###################################################################
# if num1[0]<num1[1]:
#     if num1[0]<num1[2]:
#         if num1[1]<num1[2]:
#             num2 = [2,1,0]
#         else:
#             num2 = [1,2,0]
#     else:
#         num2 = [1,0,2]
# else:
#     if num1[0]<num1[2]:
#         num2 = [2,0,1]
#     else:
#         if num1[1]<num1[2]:
#             num2 = [0,2,1]
#         else:
#             num2 = [0,1,2]
# for i in num2:
#     print(num1[i])
######################################################################
# num2 = []
# while(len(num1)>1):
#     for i in range(len(num1)-1):
#         fir = max(num1[i],num1[i+1])
#     num2.append(num1.pop(num1.index(fir)))
# else:
#     num2.append(num1[0])
# print(num2)
######################################################################
# while(len(num1)>1):
#     for i in range(len(num1)-1):
#         fir = max(num1[i],num1[i+1])
#     print(num1.pop(num1.index(fir)))
# else:
#     print(num1[0])
######################################################################
# while(len(num1)>1):
#     fir = max(num1)
#     print(num1.pop(num1.index(fir)))
# else:
#     print(num1[0])
######################################################################
# while(len(num1)>1):
#     fir = max(num1)
#     print(fir)
#     num1.remove(fir)
# else:
#     print(num1[0])
######################################################################
# while(num1):
#     if len(num1)==1:
#         print(num1[0])
#         break
#     fir = max(num1)
#     print(fir)
#     num1.remove(fir)
######################################################################
# num1.sort(key=int)
# print(num1)
######################################################################
num1 = [0,1,2,3,4,5,6,7,8]
co = 0
fla = 0
# n = int(input("How many numbers do you want input: "))
n = len(num1)
# for i in range(n):
#     num1.append(int(input(">>>")))
for i in range(n-1):
    count = 0
    for j in range(n-i-1):
        if num1[j]>num1[j+1]:
            count = count + 1
            t = num1[j+1]
            num1[j+1] = num1[j]
            num1[j] = t
        if j==n-1-i-1:
            if count==0:
                fla = 1
                break
        co = co + 1
    if fla == 1:
        break
print(num1)
print(co)
print(count)
######################################################################


