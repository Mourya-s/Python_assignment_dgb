# my approach to code
def my_approach():
        
    n=int(input("enter the number of alphabet:"))
    arr=[]
    for i in range(n):
        ar1=input()
        arr.append(ar1)
    se1=[]
    for i in arr:      # dont use set --> it will change the order
        if i not in se1 :
            se1.append(i)
    print(len(se1))

    for i in se1:
        print(arr.count(i),end=" ")



# better approach for the code
def better_approach():
        
    n = int(input())

    words = {}
    for i in range(n):
        w = input()
        if w in words:
            words[w] += 1
        else:
            words[w] = 1

    print(len(words))
    print(*words.values())
