# My approach for the code 
def my_approach():

    def print_formatted(number):
        # your code goes here
        
        for i in range(number):
            dec=str(i)
            oc=oct(i)
            he=hex(i)
            bi=bin(i)
            print(f"{dec:>10} {oc:>10} {he:>10} {bi:>10}")
        
    print_formatted(10)


# better code approach with chat Gpt
def better_approach():

    def print_formatted(number):
        pad = len(bin(number)[2:])
        
        for i in range(1, number + 1):
            dec = str(i).rjust(pad)
            oc = oct(i)[2:].rjust(pad)
            he = hex(i)[2:].upper().rjust(pad)
            bi = bin(i)[2:].rjust(pad)

            print(dec, oc, he, bi)

    if __name__ == '__main__':
        n = int(input())
        print_formatted(n)
        