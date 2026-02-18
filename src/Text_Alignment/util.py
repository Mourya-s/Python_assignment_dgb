# my approach to code
def my_approach():
    for i in range(6):
        x="H"*((2*i)-1)
        print(f"{x:^10}")

    for i in range(6):
        print("  "+"H"*6, end=" ")
        print(" "*6, end=" ")
        print("  "+"H"*6)

    for i in range(3):
        print("  "+"H"*28)

    for i in range(6):
        print("  "+"H"*6, end=" ")
        print(" "*6, end=" ")
        print("  "+"H"*6)
    for i in range(6,0,-1):
        x="H"*((2*i)-1)

        print(f"{" "*16}{x:^10}")



# Better approach for that code
def better_approach():
    thickness = int(input())  # must be odd
    c = 'H'

    # Top Cone
    for i in range(thickness):
        print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

    # Top Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

    # Middle Belt
    for i in range((thickness+1)//2):
        print((c*thickness*5).center(thickness*6))

    # Bottom Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

    # Bottom Cone
    for i in range(thickness):
        print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# use this code better understanding  --> ITS DETAILED
def for_better_understanding():
    thickness =5 # must be odd
    c = 'H'

    # Top Cone
    for i in range(thickness):
        print((c*i).rjust(thickness-1,"-") + "o" + (c*i).ljust(thickness-1,"-"))

    # Top Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2,"-") + (c*thickness).center(thickness*6,"-"))

    # Middle Belt
    for i in range((thickness+1)//2):
        print((c*thickness*5).center(thickness*6))
        
    # Bottom Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

    # Bottom Cone
    for i in range(thickness):
        print(((c*(thickness-i-1)).rjust(thickness,"-") + "o" + (c*(thickness-i-1)).ljust(thickness,"x")).rjust(thickness*6,"p"))