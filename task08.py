people = [
  {"name": "Ali", "age": 25},
  {"name": "Sami", "age": 19},
  {"name": "Lola", "age": 31}
]
resalt = sorted(people, key=lambda person: person["age"], reverse=True)
print(resalt)