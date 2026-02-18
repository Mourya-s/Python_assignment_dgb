# my approach for the code
def my_approach():
        
    n=int(input('enter the number of students: '))
    x=input("enter the clo_names").split()
    ind=x.index("mar")

    total=0
    for i in range(n):
        values_ip=input().split()
        total+=int(values_ip[ind])
    print(f"average marks of students is {total/n}")
        

#Better approach for the code with the help of chat gpt
def better_approach():
        
    n = int(input())
    columns = input().split()
    index = columns.index("MARKS")

    total = 0
    for _ in range(n):
        total += int(input().split()[index])

    print(f"{total/n:.2f}")
