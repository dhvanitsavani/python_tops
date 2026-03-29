import re

# + :-
print("-"*30)
print(re.match(r"a+b", "aab"))
print(re.match(r"a+b", "ab"))
print(re.match(r"a+b", "b"))

# * :-
print("-"*30)
print(re.match(r"a*b", "aab"))
print(re.match(r"a*b", "ab"))
print(re.match(r"a*b", "b"))

# ? :-
print("-"*30)
print(re.match(r"a?b", "aab"))
print(re.match(r"a?b", "ab"))
print(re.match(r"a?b", "b"))

# . :-
print("-"*30)
print(re.match(r"a.b", "a%b"))
print(re.match(r"a.b", "ab"))
print(re.match(r"a.b", "accb"))

# $ :-
print("-"*30)
print(re.search(r"er$", "power"))
print(re.search(r"ed$", "power"))

# ^ :-
print("-"*30)
print(re.search(r"^h", "hat bat"))
print(re.search(r"^b", "hat bat"))

# [] :-
print("-"*30)
print(re.findall(r"[aeiou]", "hello, how are you ?"))

# - :-
print("-"*30)
print(re.findall(r"[A-Z]", "Hello, Mr. Prakash"))

# () :-
print("-"*30)
print(re.findall(r"(hot)+", "holt, hot, hotted, host"))

