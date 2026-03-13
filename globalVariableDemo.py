def myfun():
    global name
    print("1st ", name)
    name = "python language"
    print("2nd ", name)

name = "python"

myfun()

print("3rd ", name)
