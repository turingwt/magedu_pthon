# sq = ['1', ['2', '2'], '3']
# # print('\"'.join(map(str, sq)))
# # print(sq)
# sq = 'My name is watson'
# # print('\n'.join(sq).splitlines())
# print(sq.rsplit(None, maxsplit=1)[-1])
# print('{}    {}'.format(10, 20))
#####################################################
# num1 = input("Please input a number: ").strip().lstrip('0')
# num = ""
# len_num1 = len(num1)
# print(len_num1)
# for i in range(len_num1):
#     if num.find(num1[i]) == -1:
#         print("{}   {}".format(num1[i], num1.count(num1[i], i)))
#         num += num1[i]
# num2 = list(num1)
# for i in range(1, len_num1+1):
#     print(num2[-i], end=' ')
#####################################################
num1 = input("Please input a number: ").strip().lstrip('0')
num = ""
len_num1 = len(num1)
print(len_num1)
count = [0] * 10
for i in range(len_num1):
    count[int(num1[i])] += 1
for i in range(10):
    if count[i] != 0:
        print("{}\t{}次".format(i, count[i]), end='\t')
num2 = list(num1)
print()
for i in range(1, len_num1+1):
    print(num2[-i], end=' ')

