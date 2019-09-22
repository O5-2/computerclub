from sys import stdin

T = int(stdin.readline())

for i in range(0, T):
    isPossible = False
    topFaces = stdin.readline() + ""
    bottomFaces = stdin.readline() + ""
    arrangements = ['012', '021', '102', '120', '201', '210']
    for i in arrangements:
        firstMatch = (topFaces[int(i[0])] == 'b') or (bottomFaces[int(i[0])] == 'b')
        secondMatch = (topFaces[int(i[1])] == 'o') or (bottomFaces[int(i[1])] == 'o')
        thirdMatch = (topFaces[int(i[2])] == 'b') or (bottomFaces[int(i[2])] == 'b')
        if ((firstMatch and secondMatch) and thirdMatch):
            isPossible = True
    if isPossible:
        print("yes")
    else:
        print("no")
