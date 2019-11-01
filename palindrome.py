def isPal(word):
    flip: str = ''
    for c in word:
        flip = c + flip
        #print(flip)
    if flip == word:
        return True
    else:
        return False

word = input("Enter a word\n")
if isPal(word):
    print("It is a palindrome")
else:
    print("Not a palindrome")