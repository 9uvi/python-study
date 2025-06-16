first_range = [i % 12 for i in range(24)]
second_range = ("00", "15", "30", "45")

switch = False

for item in first_range:
    for second in second_range:
        if item == 0:
            item = 12
            
        if item == 11 and second == "45":
            switch = True
        
        if switch:
            print(f"{item}:{second} pm")
        else:
            print(f"{item}:{second} am")