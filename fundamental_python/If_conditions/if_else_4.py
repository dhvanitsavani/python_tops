rno = int(input("enter roll no : "))
name = input("enter name : ")
s1 = int(input("enter subject 1 marks : "))
s2 = int(input("enter subject 2 marks : "))
s3 = int(input("enter subject 3 marks : "))

total = s1 + s2 + s3
per = total / 3

print("roll no : ", rno)
print("name : ", name)
print("total : ", total)
print("per : ", per)

if(per >= 70):
    print("distinction")
elif(per >= 60):
    print("first class")
elif(per >= 50):
    print("second class")
elif(per >= 40):
    print("pass class")
else:
    print("fail")
