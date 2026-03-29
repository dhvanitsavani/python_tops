import re

string = "python is a powerful language"

for i in re.finditer(r"power", string):
    print(i.span())
