def even_generator():
    for i in range(1, 11):
        yield i * 2

even_nums = even_generator()

for even_num in even_nums:
    print(even_num)
