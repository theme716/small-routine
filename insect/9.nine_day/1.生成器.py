def foo():
    yield 1
    yield 2
    yield 3

g = foo()
# print(next(g))
# print(next(g))
# print(next(g))

for num in g:
    print(num)
