import itertools
res = "1211"
for digit, group in itertools.groupby(res):
    print(digit, list(group))
