import datetime
import random
now = datetime.datetime.now()
# nums = random.randrange(10)
nums = [11, 7, 5, 11, 7, 6, 11]
length = len(nums)
same = []
nums = [nums, [0]*length]
for i in range(length):
    if nums[1][i] == 0:
        for j in range(i+1, length):
            if nums[1][j] == 0:
                if nums[0][i] == nums[0][j]:
                    nums[1][j] = 1
                    if nums[1][i] == 0:
                        nums[1][i] = 1
                        same.append(nums[1][i])
t = (datetime.datetime.now()-now).total_seconds()
print(t)
print(same)
# print(nums)

