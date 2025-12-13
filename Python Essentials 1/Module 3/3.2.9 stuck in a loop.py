word = input("Whats the word? ")

while word:
  if word != "chupacabra":
    word = input("Whats the word? ")
  else:
    break

print("You've successfully left the loop.")