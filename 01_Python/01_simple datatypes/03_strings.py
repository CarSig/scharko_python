# String formatting
name = "John"
age = 25
print("My name is {} and I am {} years old".format(name, age))
print(f"My name is {name} and I am {age} years old")

# String methods

upper_case = "hello".upper()
lower_case = "HELLO".lower()
strip = "   hello   ".strip()
replace = "hello".replace("h", "j")
split = "hello,world".split(",")
join = ",".join(["hello", "world"])

print(join)

# excercise
original = ['this=', 'is=', 'a=', 'sentence']
new_must_be = "this is a sentence"
