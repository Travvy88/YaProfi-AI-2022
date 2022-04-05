import sys

print('?', i)
ans = int(input())
if ans == 2:

minn = 0
last_ans = -1
flag1 = False
for i in range(1, 1000):
    print('?', i)
    ans = int(input())

    if ans == 1 and not minn:
        minn = i

    elif ans == 2 and last_ans == -1:
        print('!', 1, 1)
        break

    elif ans == 2 and last_ans == 0:
        print('!', i, minn)
        break

    elif ans == 2 and last_ans > 0:
        print('!', int(i / minn), minn)
        break

    last_ans = ans
