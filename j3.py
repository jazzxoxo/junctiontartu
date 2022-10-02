n = int(input())
if n % 3 == 0 and n % 5 == 0:
    print("JumpStart")
elif n % 3 == 0:
    print("Jump")
elif n % 5 == 0:
    print("Start")
else:
    print(n)
