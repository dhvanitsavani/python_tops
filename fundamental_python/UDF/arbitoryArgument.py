def test(a, b, *c, **d):
    print("a:", a, " b:", b, " c:", c, " d:", d)

test(1, 2, 3, 4, 5, 6, 7, x=10, y=20, z=30)

# one * is to store more arguments while calling function in a tuple and two * are to store in dictionary.
#arbitory arguments always must be in last of parameters, if both are here first * and then **.
