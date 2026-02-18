
#my approach for the code
def my_approach():
        
    import numpy 
    li=[]

    n=int(input("enter the number "))
    for i in range(n):
        x=list(map(int,input().split()))
        li.append(x)

        
    li1= numpy.min(li, axis = 1)      
    print(max(li1))


