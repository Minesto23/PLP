"""
    Variables in Python
"""

# Creating Variables

x = 1
y= 10.5
letter = 'a'
phrase = 'This is a phrase'

print(x)
print(y)
print(letter)
print(phrase)

# Casting

n = int(10)
m = str(10)
o = float(10)

print(n)
print(m)
print(o)


# Get the Type

print(f"The type of x is : {type(x)}")
print(f"The type of x is : {type(y)}")
print(f"The type of x is : {type(phrase)}")


# Assign multiple variable

w,e,r = "orange", "grapes", "apples"
print(w)
print(e)
print(r)

# one value to multiple varables

b1 = b2 = b3 = "The value of b"
print(b1)
print(b2)
print(b3)


# Unpack a collection

computers = ['Dell', "Asus", 'Mac']
c1,c2,c3 = computers

print(c1)
print(c2)
print(c3)

# the global Keyword

def myfunc():
    global v
    v = "Global Variable"

myfunc()
print(v)
