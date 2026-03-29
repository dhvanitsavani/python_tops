import re

pattern = r"hello"
s = "hello world hello"

print(re.match(pattern, s))
print(re.match("world", s))
print(re.search("world", s))
print(re.findall(pattern, s))
