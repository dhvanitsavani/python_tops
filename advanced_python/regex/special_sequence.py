import re

s1 = "hello world $ good morning 1234"
s2 = "low blow lower blower"

pattern1 = r"\w+"
pattern2 = r"\W+"
pattern3 = r"\d+"
pattern4 = r"\D+"
pattern5 = r"\s+"
pattern6 = r"\S+"
pattern7 = r"\blow"
pattern8 = r"low\b"
pattern9 = r"\blow\b"
pattern10 = r"\Blow\B"

print(re.findall(pattern1, s1))
print(re.findall(pattern2, s1))
print(re.findall(pattern3, s1))
print(re.findall(pattern4, s1))
print(re.findall(pattern5, s1))
print(re.findall(pattern6, s1))
print(re.findall(pattern7, s2))
print(re.findall(pattern8, s2))
print(re.findall(pattern9, s2))
print(re.findall(pattern10, s2))
