blocks = int(input("Enter the number of blocks: "))

height = 0
number = 1

while blocks >= number:
  blocks -= number
  number += 1
  height += 1

print("The height of the pyramid:", height)