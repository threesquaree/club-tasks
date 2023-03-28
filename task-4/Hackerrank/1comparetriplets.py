a = []
b = []

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
a.append(a0)
a.append(a1)
a.append(a2)

b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
b.append(b0)
b.append(b1)
b.append(b2)

a_points = 0
b_points = 0

if a[0] > b[0]:
    a_points += 1
elif a[0] < b[0]:
    b_points += 1

if a[1] > b[1]:
    a_points += 1
elif a[1] < b[1]:
    b_points += 1

if a[2] > b[2]:
    a_points += 1
elif a[2] < b[2]:
    b_points += 1

if a[0] == b[0]:
    a_points += 0
    b_points += 0

if a[1] == b[1]:
    a_points += 0
    b_points += 0

if a[2] == b[2]:
    a_points += 0
    b_points += 0

score_array = [a_points,b_points]
score_string = " ".join(str(score) for score in score_array)
print(score_string)


