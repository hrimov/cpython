print("Until x >= 5")
x = 0
until x >= 5:
    print(x)
    x += 1
else:
    print("else")
print()

print("Until with early return (condition falsy)")
until True:
    print("Inside a falsy block")
print()

print("Until x >= 10 with break if x == 5")
x = 0
until x >= 10:
    if x == 5:
        break
    print(x)
    x += 1
else:
    print("break else")
print()
