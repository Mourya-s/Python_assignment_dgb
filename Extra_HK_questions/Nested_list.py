if __name__ == '__main__':
    di={}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        di[name]=score
    d1=dict(sorted(di.items()))
    li=list(set(d1.values()))
    
    li.sort()
    
    for key,value in d1.items():
        if  d1[key]==li[1]:
            print(key)
    
