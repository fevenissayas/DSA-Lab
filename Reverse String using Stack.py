def reverse_string(input_str):
    lst = []
    reverse_str = ""
    
    
    for i in (input_str):
        lst.append (i)
    
    count = len (lst)
    
    while count > 0:
        reverse_str += lst [count-1]
        count-=1
        print (reverse_str)
    return reverse_str

print(reverse_string ("Hey!"))