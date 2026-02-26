import random

counter = 0

while True:
    choice = input("Roll the dice (y/n): ").lower()
    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"{die1}, {die2}")
        counter = counter + 1
    elif choice == 'n':
        print("Thanks for playing!")
        print("The time dice rolled: ", counter)
        break
    else:
        print("Invalid choice!")