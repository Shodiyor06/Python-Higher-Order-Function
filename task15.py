votes = [
  {"option": "A", "votes": 123},
  {"option": "B", "votes": 145},
  {"option": "C", "votes": 97}
]
resalt = max(votes, key=lambda n:  n['votes'])
print(resalt)