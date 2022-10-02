from random import randint

l = ["Rock", "Paper", "Scissors", "Spock", "Lizard"]
y = randint(0,4)

while True:
    a = input("Choose ur fighter?")
    if a in l:
        for i in range(5):
            if a == l[i]:
                x = i
        break

if x == y:
    print("Draw")
elif y == (x+2)%5 or y == (x+4)%5:
    print("Player won!")
elif y == (x+1)%5 or y == (x+3)%5:
    print("Ur no match for the machine!:(")
