
threeSizedNums = list(range(100, 1000, 1))
products = []

for i in threeSizedNums:
    calc = 0
    for x in threeSizedNums:
        calc = i * x
        if str(calc) == str(calc)[::-1]:
            products.append(calc)
    calc = 0

print(max(products))
