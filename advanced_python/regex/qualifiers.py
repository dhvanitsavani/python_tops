import re

# + :-
print("-"*30)
print(re.match(r"a+", "aa"))
print(re.match(r"a+", ""))

# * :-
print("-"*30)
print(re.match(r"a*", "aa"))
print(re.match(r"a*", ""))

# {n} :-
print("-"*30)
print(re.match(r"a{3}", "aa"))
print(re.match(r"a{3}", "aaa").group())
print(re.match(r"a{3}", "aaaa").group())

# {n,} :-
print("-"*30)
print(re.match(r"a{3,}", "aa"))
print(re.match(r"a{3,}", "aaa").group())
print(re.match(r"a{3,}", "aaaa").group())


# {n, m} :-
print("-"*30)
print(re.match(r"a{3,5}", "aa"))
print(re.match(r"a{3,5}", "aaa").group())
print(re.match(r"a{3,5}", "aaaa").group())
print(re.match(r"a{3,5}", "aaaaa").group())
print(re.match(r"a{3,5}", "aaaaaaaaa").group())
