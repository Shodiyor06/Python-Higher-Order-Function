text = ["apple", "34", "banana", "100", "abc", "75"]
resalt = filter(lambda n: n.isdigit(),
                text)
print(list(resalt))