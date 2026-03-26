l = [1, 2, 3, 4, 5, 6]

ans = filter(lambda x : x*x*x % 2 == 0, l)
print(list(ans))
