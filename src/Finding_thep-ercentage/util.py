# My INITIAL approach
def my_approach():

    dic={}
    num=int(input("Enter the value: "))

    for i in range(num):
        x=input("enter the student name: ")
        dic[x]=[]
        for i in range(3):
            y=int(input("enter the marks one by one"))
            dic[x].append(y)

    name= input("enter the name you want to Know the average")
    if name in dic.keys():
        avg=sum(dic[name])/len(dic[name])
    else:
        print("Enter the name you have entered")

    print(dic)
    print(f"{avg:.2f}")

#NOTE: we can use .split() also , but there we have to use extend not append--> this will
# create nested list 


#Better version of code with the helpof Chat-Gpt
def better_approach():
    dic = {}

    num = int(input())

    for i in range(num):
        data = input().split()
        name = data[0]
        marks = list(map(float, data[1:]))
        dic[name] = marks

    query_name = input()

    avg = sum(dic[query_name]) / len(dic[query_name])
    print(f"{avg:.2f}")

