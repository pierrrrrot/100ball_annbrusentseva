f = open('1_27_A.txt')
N = int(f.readline())
nums = [int(i) for i in f]

K = 4
max_sum = 0
channel1 = 0
channel2 = 0
for i in range(N - K):
    for j in range(i + K, N):

        if (nums[i] + nums[j]) % 12 == 0:
            if nums[i] + nums[j] > max_sum:
                max_sum = nums[i] + nums[j]
                channel1 = nums[i]
                channel2 = nums[j]

if max_sum == 0:
    print(-1)
else:
    print(max_sum)
    print(channel1, channel2)

