
data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]
resalt = list(filter(lambda n: type(n) == str and len(n) > 5,
                     data))
print(resalt)