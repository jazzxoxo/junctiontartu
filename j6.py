n = int(input())
summa = 0
for i in range(1, n + 1):
  if n % i == 0:
      summa = summa + 1

if summa % 2 == 0:
    print('even')
else:
    print('odd')
