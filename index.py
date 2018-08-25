# Pythom idioms

# Recursive function
def fib(n):
    return 1 if n < 2 else fib(n-2) + fib(n-1)

# List comprehension
seq = [fib(x) for x in range(10)]
seq = [fib(x) for x in range(10) if x % 2 == 0]

# Dictionary comprehension
powers = {x: x**2 for x in (2, 4, 6)}

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

# Iterate sequence with index
for i, n in enumerate(['heart', 'spade', 'club', 'diamond']):
    print i, n

# Iterate dictionary
for k, v in powers.iteritems():
    print k, v
