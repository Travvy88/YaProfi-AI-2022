import sys

def check():
    minn = 0
    last_ans = -1
    for i in range(1, 5):
        print('?', i)
        ans = int(input())
        sys.stdout.flush()
        if ans == 1 and not minn:
            minn = i

        elif ans == 2 and last_ans == -1:
            print('!', 1, 1)
            return 1
        elif ans == 2 and minn == 0:
            print('!', i, i)
            return 1

        elif ans == 2 and last_ans == 0 and minn:
            print('!', minn, i)
            return 1

        elif ans == 2 and last_ans > 0 and minn:
            print('!', int(i / minn), minn)
            return 1

        last_ans = ans
    return i

i = check()
if i != 1:
    print('!', 1, i)