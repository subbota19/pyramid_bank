import sys

total = int(sys.stdin.readline().strip())
list_ = []
for i in range(0, total):
    number = sys.stdin.readline().strip()[:-1]
    if len(set(number)) == 1 and '1' in set(number):
        list_.append(number)
if len(list_) != 0:
    sys.stdout.write(str(max(list(map(lambda x: len(x), list_)))))
else:
    sys.stdout.write('0')