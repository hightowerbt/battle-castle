print("Please tell me your name, warrior: ", end="")
player_name = str(input())

print("Please choose your profession.")
print("1. Knight")
print("2. Slayer")
print("3. Mystic")
print("4. Rascal")
print("5. Mender")
print("Enter the name or number of your profession: ", end="")
player_class_num = int(input())

if player_class_num == 1:
    player_class = "Knight"
elif player_class_num == 2:
    player_class = "Slayer"
elif player_class_num == 3:
    player_class = "Mystic"
elif player_class_num == 4:
    player_class = "Rascal"
elif player_class_num == 5:
    player_class = "Mender"
else:
    print("The profession you chose does not exist!")
    exit(0)

print("Welcome, " + player_name + " the " + player_class + ", to the Battle Castle!")