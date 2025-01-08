# i = 1
# while i <= 5:
#     print(i)
#     if(i == 3):
#         break
#     i+= 1

nums_tuple = (1,4,5,166,173,23,25,67,87,166,166)

i = 0
x = 166
while i < len(nums_tuple):
    if(nums_tuple[i] == x):
        print("Found at:",i)
        break
    else:
        print("Finding...")
    i+=1