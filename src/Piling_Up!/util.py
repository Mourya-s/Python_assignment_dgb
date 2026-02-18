#my approach for the code

def my_approach():
        
    n = int(input("enter the number of rows: "))
    arr = []

    for i in range(n):
        num = int(input("enter the numners one"))
        ar1 = list(map(int, input().split()))
        arr.append(ar1)

    for i in range(len(arr)):
        tes = float('inf')   #first iteration is always TRUE--> (value updated) ||| Or ta a big value 
                                # tes=1000
        dec = "Yes"

        while arr[i]:
            a = arr[i][0]
            b = arr[i][-1]

            if a >= b:
                if a <= tes:
                    tes = a
                    arr[i].pop(0)
                else:
                    dec = "No"
                    break
            else:
                if b <= tes:
                    tes = b
                    arr[i].pop()
                else:
                    dec = "No"
                    break

        print(dec)


#chat gpt code ---> uses stacK for this code approach