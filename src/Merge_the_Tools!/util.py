# My approach for the code
def my_approach():
        
    alp="aacdefyty"
    k=3
    for i in range(0,len(alp),k):
        sub=alp[i:i+k]       # important step
        sen=""

        for letter in sub:
            if letter not in sen:
                sen+=letter

        print(sen)








# better code approach with chatgpt
def better_approach():

    def merge_the_tools(string, k):
        for i in range(0, len(string), k):
            sub = string[i:i+k]
            sen = ""

            for letter in sub:
                if letter not in sen:
                    sen += letter

            print(sen)
        

    if __name__ == '__main__':
        string, k = input(), int(input())
        merge_the_tools(string, k)