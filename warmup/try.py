# ran = range(0,5,1)

# for i in ran:
#     print(i)

# # print(ran.count(2))


# tup1 = (20,11,34,50) 
# print(tup1.count(100))

# list_array = [[1,2,3],[4,5,6],[7,8,9]]
# for item in list_array:
#   if item == [1,2,3]:
#     print("Hello!")
#     continue
#   print('item =',item)

# dic = {'a':10,'b':20,'c':30,'d':40}
# b = dic.get('f',100)
# print(b)

# dic = {'a': 10,'b': 20,'c': 30, 'd': 40}
# print(dic.popitem())

dic = {'w': 10,'x': 20,'y': 30}

for str,elemens in dic.items():
    if elemens > 10:
        print("Hello!")