# Pythom idioms

# Recursive function
def fib(n):
    return 1 if n < 2 else fib(n-2) + fib(n-1)

# List comprehension
seq = [fib(x) for x in range(10)]

# Keyword arguments, variable args, packing args
def upsert(name, title='Software Engineer', *args, **config):
    print config

config = {'name': "My List", 'description': "Description"}

# Dictionary keys
dict(name='My List', title='Sofwares')

# Argument unpacking
upsert(**config)

# Set data structure
set([1, 2])
