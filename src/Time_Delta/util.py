# code
def time_difference():
        
    from datetime import datetime

    t1 = input()
    t2 = input()

    #strptime()--> convert string to date time zone...
    d1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')  #z=> zone ahead or behind the standard time
    d2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')

    diff = int((d1 - d2).total_seconds())  
    print(diff)
