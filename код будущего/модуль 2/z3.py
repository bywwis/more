import sys

list_nums = list(map(lambda x: int(x.rstrip('\n')), sys.stdin.readlines()))
if len(list_nums) != 0:
    print(sum(list_nums)/len(list_nums))
else:
    print(-1)