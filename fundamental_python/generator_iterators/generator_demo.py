def demo_gen():
    yield 1
    yield 2
    yield 3

demo = demo_gen()

print(next(demo))
print(next(demo))
print(next(demo))

# generator is a function that produces values one at a time, it can return more than one value, it don't execute all the staments at once - but execute when it's called
# generator function is used to handle larger data
# generator returns a generator object when demo = demo_gen() is called but don't execute all statement like functions
