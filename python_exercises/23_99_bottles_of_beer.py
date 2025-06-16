bottles = 99

for i in range(100, 2, -1):
    print(f"{bottles} bottles of beer on the wall,\n{bottles} bottles of beer,\nTake one down,\nPass it around,")
    print()
    bottles -= 1

print(f"{bottles} bottle of beer on the wall,\n{bottles} bottle of beer,\nTake one down,\nPass it around")
print()

print("No more bottles of beer on the wall!")