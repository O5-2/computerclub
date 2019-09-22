from sys import stdin
q = int(stdin.readline())
for i in range(0, q):
    n = int(stdin.readline())
    students = [int(i) for i in stdin.readline().split(' ')]
    way = students[0]-students[-1]
    broken = False
    if way in [1, 1-len(students)]:
        if set([students[j+1]-students[j] for j in range(0, n-1)]).issubset(set([1, 1-len(students)])):
            print("YES")
        else:
            print("NO")
    elif way in [-1, len(students)-1]:
        if set([students[j+1]-students[j] for j in range(0, n-1)]).issubset(set([-1, len(students)-1])):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
