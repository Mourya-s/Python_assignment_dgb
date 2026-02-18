# my approavh for the code

def my_approach():
    import numpy

    A = list(map(float, input().split()))

    print(numpy.floor(A))
    print(numpy.ceil(A))
    print(numpy.rint(A))

# Better approach for the code
def better_approach():
        
    import numpy

    numpy.set_printoptions(sign=' ')   # --> for spacing evenly

    A = numpy.array(list(map(float, input().split())))

    print(numpy.floor(A))
    print(numpy.ceil(A))
    print(numpy.rint(A))
