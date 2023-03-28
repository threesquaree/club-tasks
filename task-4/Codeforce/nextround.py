n,k = map(int, input().split(' '))
list = list(map(int, input().split(' ')))
list_1 = list[k-1]
count = 0

for i in list:
    if i >= list_1 and (i>0 and list_1>0):
        count += 1
print(count)