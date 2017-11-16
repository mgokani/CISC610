a = []
e = int(input("insert how many elements you want:"))
for n in range(0, e):
    a.append(int(input("Enter next no :")))
print(a)


def selectionSort():
    for i in range(0, (len(a) - 1)):
        imin = i
        for j in range((i + 1), len(a)):
            if a[j] < a[imin]:
                imin = j
        temp = a[i]
        a[i] = a[imin]
        a[imin] = temp


selectionSort()
for m in range(0, len(a)):
    print(a[m])

