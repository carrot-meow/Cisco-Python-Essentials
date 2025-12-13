steps = 0

c0 = int(input("Choose a number: "))

while c0 != 1:
  if c0 % 2 == 0:
    c0 = c0 // 2
    print(c0)
    steps += 1
  elif c0 % 2 != 0:
    c0 = c0 * 3 + 1
    print(c0)
    steps += 1
  elif c0 != 1:
    c0 = c0 * 3 + 1
    print(c0)
    steps += 1


print(f"steps= {steps}")