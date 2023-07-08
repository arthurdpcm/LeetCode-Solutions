
def isPalindrome(x):
    # Transform to string to have the length.
    number = str(x)
    for i in range(len(number)):
        # Check if the i° char is equal to the last-i. If in some case fail, return false
        if(number[i] != number[len(number)-(1+i)]):
            return False
    return True

print(isPalindrome(919))