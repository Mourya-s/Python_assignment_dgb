# my approach for the code
def my_approach():
    word=input("Enter the word: ")
    xx=list(input("1st --> position , 2nd -->letter").split())

    new_str=word[:int(xx[0])]+str(xx[1])+word[int(xx[0])+1:]
    print(new_str)

    # another approach by me
    word = input("Enter the word: ")
    xx = input("1st --> position , 2nd -->letter: ").split()

    pos = int(xx[0])
    letter = xx[1]

    new_str = word[:pos] + letter + word[pos+1:]
    print(new_str)





# better code approach with chat GPT
def better_approach():
    def mutate_string(string, position, character):
        new_str = string[:position] + character + string[position+1:]
        return new_str

    if __name__ == '__main__':
        s = input()
        i, c = input().split()
        s_new = mutate_string(s, int(i), c)
        print(s_new)