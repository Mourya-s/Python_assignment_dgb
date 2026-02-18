def swap_case(s):
    x=""
    for ch in s:
        if ch.islower():
            x+=ch.upper()
        else:
            x+=ch.lower()
            
    return x

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)