prices = ["$120", "$340", "$50", "$90"]

resalt = list(map(
    lambda n: float(n[1:]),
    prices
    ))
print(resalt)