def test(a=10, b=10, c=10, d=10):
    print("a=", a, " b=", b, " c=", c, " d=", d)

test()
test(b=100,d=200)

#this is default arguments. if we give default argument before last argument, we have to give all arguments till last default.
