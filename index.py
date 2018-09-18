# Pythom idioms

import sys

# Recursive function
def fib(n):
    return 1 if n < 2 else fib(n-2) + fib(n-1)

# List comprehension
seq = [fib(x) for x in range(10)]
seq = [fib(x) for x in range(10) if x % 2 == 0]

# Dictionary comprehension
powers = {x: x**2 for x in (2, 4, 6)}

# Default arguments, variable args, dictionary packed args
def upsert(name, title='Software Engineer', languages='Python', *args, **config):
    """Update object if it exist, or create a new one.

    Lookup object by name and update it with new values, else create new by name
    """
    function_args = locals()
    print function_args

# Keyword arguments
upsert('Joe', title='Developer')
upsert('Jim', 'Tester', 'Java', 'Big Corp')

# Argument unpacking
config = {'name': "My List", 'description': "Description"}
upsert(**config)

# Lambda
print (lambda x: x + 1)(5)

# String dictionary keys
dict(name='My List', title='Softwares')

# Set data structure
set([1, 2])

# Tuple packing and unpacking
metals = 'gold', 'silver'
g, s = metals

# Iterate sequence with index
for i, n in enumerate(['heart', 'spade', 'club', 'diamond']):
    print i, n

# Iterate dictionary
for k, v in powers.iteritems():
    print k, v

# Built in functions and variables
import __builtin__
for fv in dir(__builtin__):
    print fv

# Open, read and close file
with open('index.py') as f:
    line = f.read()

# JSON serialization and deserialization
import json
with open('data.json', 'w') as f:
    json.dump([
        dict(name='John', title='Manager'),
        dict(name='Joe', title='Accountant'),
        ], f)

with open('data.json') as f:
    data = json.load(f)
    print data

# Run module as script
if __name__ == "__main__":
    import sys
    print sys.argv
