# My approach for the code
def my_approach():

    arr = []

    length = int(input())
    num = list(map(int, input().split())) # OR use the for loop itself
    arr.extend(num)
    print(arr)

    arr1=list(set(arr))

    arr1.remove(max(arr))

    print(max(arr1))



# Better approach with Chat-Gpt
def better_approach():

    n = int(input())
    arr = list(map(int, input().split()))

    arr = list(set(arr))   # remove duplicates
    arr.remove(max(arr))   # remove highest

    print(max(arr))        # second highest
