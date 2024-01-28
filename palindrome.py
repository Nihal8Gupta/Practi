#12 WAP by function that check whether a passed string is palindrome or not 
def palindrome(s):
    l = "".join(s.split())
    return True if l == l[::-1] else False

s = input()
if palindrome(s):
    print('Palindrome')
else:
    print('Not Palindrome')