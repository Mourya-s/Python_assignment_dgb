# my approach for the code
def my_approach():

    # function to check valid email
    def fun(s):
        # regex for email validation        # instead of using regular expression (re)
        return s[(len(s)-4): ]==".com"
            

    # input number of emails
    n = int(input())
    emails = []

    # read emails and filter valid ones
    for _ in range(n):
        s = input()
        if fun(s):
            emails.append(s)

    # sort emails lexicographically
    emails.sort()

    print(emails)






# better approach for the code with chat gpt 
def better_approach():
        
    import re  # to match regular expression

    # function to check valid email
    def fun(s):
        # regex for email validation
        pattern = r'^[a-zA-Z0-9_.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
        return re.match(pattern, s)

    # input number of emails
    n = int(input())
    emails = []

    # read emails and filter valid ones
    for _ in range(n):
        s = input()
        if fun(s):
            emails.append(s)

    # sort emails lexicographically
    emails.sort()

    print(emails)
