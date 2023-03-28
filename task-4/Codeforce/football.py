
formation = (input())
stat = False
for i in range(len(formation)):
    if formation[i:i+7] == "0000000" or formation[i:i+7] == "1111111":
        stat = True
        break
if stat:
    print("YES")
else:
    print("NO")