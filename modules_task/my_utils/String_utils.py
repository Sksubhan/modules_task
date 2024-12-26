vowels=['A','E','I''O','U','a','e','i','o','u']
def count_vowels(s):
    c=0
    for i in s:
        if i in vowels:
            c+=1
    return c
