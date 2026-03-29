import re

# ignorecase :-
print(re.findall(r"hello", "Hello, hello, HELLO"))
print(re.findall(r"hello", "Hello, hello, HELLO", re.IGNORECASE))

# multiline :-
print(re.findall(r"^world", "hello\nworld"))
print(re.findall(r"^world", "hello\nworld", re.MULTILINE))

# dotall :-
print(re.findall(r"hello.*world", "hello\nworld"))
print(re.findall(r"hello.*world", "hello\nworld", re.DOTALL))
