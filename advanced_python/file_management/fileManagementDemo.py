file = open("demoFile.txt", "w")
file.write("This is file management demo using python")
file.close()
print("file written successfully\n")

file = open("demoFile.txt", "r")
print(file.read(), "\n")
file.close()

file = open("demoFile.txt", "a")
file.write("\nthis file is appended")
file.close()
print("appended successfully\n")

file = open("demoFile2.txt", "w+")
file.write("this is w+ operation")
print("current file position : ", file.tell())
file.seek(0)
print(file.read(), "\n")
file.close()

#file.seek(pos) set cursor to position. if we don't do that cursor was on last position so any data couldn't be readed.
#file.tell() returns position of cursor in file
