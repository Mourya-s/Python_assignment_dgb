#my approach for the code
def my_approach():
        
    n=int(input("enter the number of lapha"))
    arr=input().split()
    key=int(input())   #the index that need to ckecked
    arr1=[]
    for i in range(len(arr)):
        for j in range((i+1),n):     #NOT all combination needede
            
            arr1.append([arr[i],arr[j]])
    print(arr1)
    non=0
    for i in range(len(arr1)):
        if arr[key-1] in arr1[i]:
            non+=1
    print(non)
    print(len(arr1))
    print(non/len(arr1))
            



# Better approach for that code with the help of chat gpt
def better_approach():
        
    n = int(input())
    arr = input().split()
    key = int(input()) - 1

    count = 0
    total = 0

    for i in range(n):
        for j in range(i+1, n):        # count as soon as you create a nested arrays
            total += 1
            if arr[key] == arr[i] or arr[key] == arr[j]:  
                count += 1

    print(count / total)
