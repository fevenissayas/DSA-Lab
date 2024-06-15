def palindrome (word):
    stack = Stack ()
    for i in word:
        stack.push(i)

    count = 0
    while not stack.is_empty():
        if word[count] != stack.pop():
            return False
        count += 1
    return True
print (palindrome("hey"))
