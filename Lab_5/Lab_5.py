n=int(input("Enter size of array:"))
arr=[int(input(f"Enter elements[{i}]:")) for i in range(n)]
sum=0
for i in range(len(arr)):
    if arr[i]%3==0 and arr[i]>0:
        sum+=arr[i]
        print("Sum:", sum)
    else:
        print(f"This elements[{i}] dont more than 0 and divisible by 3")
