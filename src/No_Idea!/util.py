# my approach for the code
def my_approach():
        
    first_input=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    arr2=[]
    for i in range(first_input[1]):
        a=list(map(int,input().split()))
        arr2.append(a)

    happy=0
    for i in arr2[0]:
        if i in arr:
            happy+=1
            
    for i in arr2[1]:
        if i in arr:
            happy-=1

    print(happy)

# better approach for the code
def better_approach():
        
    n, m = map(int, input().split())

    arr = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    happiness = 0

    for i in arr:     # note : we have to checfor each element in array
        if i in A:
            happiness += 1
        elif i in B:
            happiness -= 1

    print(happiness)

