test_str = "GeeksforGeeks"
 
# using join() + bytearray() + format()
# Converting String to binary
bit = ''.join(format(i, '08b') for i in bytearray(test_str, encoding ='utf-8'))
 
# printing result
print("The string after binary conversion : " + str(bit))