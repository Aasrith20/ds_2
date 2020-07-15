n = int(input())
a = [0]*n
b = []
for i in range(n):
    q = list(input().split(" "))
    b.append(q)
index = 0
for p in b:
    if p[0][1] == "u":
        index += 1
        if int(p[1]) > int(a[index-1]):
           a[index] = int(p[1])
        else:
            a[index] = a[index-1]
    elif p[0][1] == "o":
        a.pop()
        index-=1
    else:
        print(a[index])
