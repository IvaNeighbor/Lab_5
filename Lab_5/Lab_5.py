n = 7
bim=7
arr=[[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i==j:
            arr[i][j]=7
        elif i>j:
            arr[i][j]=bim-i+j
        elif i<j:
            arr[i][j]=bim+i-j

for r in arr:
        print(*r)