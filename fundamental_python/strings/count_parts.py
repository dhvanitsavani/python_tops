count_alpha = 0
count_lower = 0
count_upper = 0
count_num = 0
count_space = 0

s = input("Enter a string : ")

for i in s:
    if(i.isalpha()):
        count_alpha += 1

        if(i.islower()):
            count_lower += 1
        else:
            count_upper += 1

    elif(i.isspace()):
        count_space += 1

    elif(i.isdecimal()):
        count_num += 1
    
    

print("alphabets : ", count_alpha)
print("lower : ", count_lower)
print("upper : ", count_upper)
print("space : ", count_space)
print("numerical : ", count_num)
