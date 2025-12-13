my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new = []

for i in my_list:
  if i not in new:
    new.append(i)

my_list = new

print("The list with unique elements only:")
print(my_list)