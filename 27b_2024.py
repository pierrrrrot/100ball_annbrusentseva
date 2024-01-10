f = open('27_B.txt')
N = int(f.readline())
nums = [int(i) for i in f]

K = 4
ostatki = [0] * 12
max_sum = 0
channel1 = 0
channel2 = 0

for i in range(K, N):

    ost1 = nums[i - K] % 12
    ostatki[ost1] = max(ostatki[ost1], nums[i - K])

    second_chan = nums[i]
    ost2 = (12 - (second_chan % 12)) % 12
    first_chan = ostatki[ost2]

    if ((second_chan + first_chan) > max_sum) and (first_chan > 0):
        max_sum = first_chan + second_chan
        channel1, channel2 = first_chan, second_chan

if max_sum == 0:
    print(-1)
else:
    print(max_sum)
    print(channel1, channel2)

