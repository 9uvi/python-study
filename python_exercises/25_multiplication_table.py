print("|".rjust(3), end="")

for i in range(1, 11):
    print(f"{i}".rjust(3), end="")

print()
print('--+-------------------------------')

for i in range(1, 11):
    print(f"{i}|".rjust(3), end="")
    for j in range(1, 11):
        if j == 10 and i == 10:
            print(f"{i * j}".rjust(4), end="")
        else:
            print(f"{i * j}".rjust(3), end="")
    print()