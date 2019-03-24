def my_generator():
    while True:
        try:
            yield 'a'
            yield 'b'
            yield 'c'
            yield 'd'
            yield 'e'
        except ValueError:
            print('Cause ValueError')
        except TypeError: 
            print('Cause TypeError')

g = my_generator()
print(next(g))
print(next(g))  
print('----------------------------')
print(g.throw(ValueError))
print('----------------------------')
print(next(g))
print(next(g))
print('----------------------------')
print(g.throw(TypeError))
print('----------------------------')
print(next(g))