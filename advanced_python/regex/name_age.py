import re

name_age_dictionary = {}
t = 0

name_pattern = r"[A-Z][a-z]+"
age_pattern = r"\d{1,2}"

string = "Yogi is 50 years old, Modi is 70 years old, Amit is 60 years old"

names = re.findall(name_pattern, string)
ages = re.findall(age_pattern, string)

for name in names:
    name_age_dictionary[name] = ages[t]

print(name_age_dictionary)
