x = 0
n = int(input())
for i in range(n):
    op = input()
    if op == "++X" or op == "X++":
        x += 1
    else:
        x -= 1
print(x)

