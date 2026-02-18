#My capproach for the code
def my_approach():
        
    import numpy

    li=[]
    num=list(map(int,input().split()))

    for i in range(num[1]):
        li1=list(map(int,input().split()))
        li.append(li1)
    print (numpy.mean(li, axis = 1))
    print (numpy.var(li, axis = 0))
    print (numpy.std(li, axis = None))


# Better approach by chat gpt gor the code
def better_approach():
        
    import numpy

    numpy.set_printoptions(precision=11)

    li=[]
    num=list(map(int,input().split()))

    for i in range(num[0]):   # rows
        li1=list(map(int,input().split()))
        li.append(li1)

    print(numpy.mean(li, axis=1))
    print(numpy.var(li, axis=0))
    print(numpy.std(li, axis=None))
