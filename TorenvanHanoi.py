from stack import Stack

print("\nLet's play Towers of Hanoi!!")

# Definitie van de drie stapels
stacks = []
left_stack = Stack("left")
right_stack = Stack("right")
middle_stack = Stack("middle")

stacks.append(left_stack)
stacks.append(right_stack)
stacks.append(middle_stack)
# of stacks += (left_stack, right_stack, middle_stack)

# Aantal disks: user input
num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))

# Beginwaarde
for disk in range(num_disks, 0, -1):
  left_stack.push(disk)

# Formule voor perfecte oplossing Hanoi
num_optimal_moves = 2 ** num_disks - 1
print("\nThe fastest you can solve this game is in {0} moves\n".format(num_optimal_moves))

# Functie user input voor interactie met de stapels
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]
  
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {0} for {1}".format(letter, name))
    user_input = input("")
    
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]
        
num_user_moves = 0

# Spelregels, winconditie: 
while right_stack.get_size() != num_disks:
  print("\n\n\n ...Current Stacks...")
  [stack.print_items() for stack in stacks]

# User interactie 
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()

# Spelregels, pakken van een lege stapel    
    if from_stack.is_empty():
      print("\nInvalid move. Try again.")

# Spelregels, valide interacties      
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break

# Grote disk op een kleinere disk proberen te zetten   
    else:
      print("\nInvalid move. Try again.")

# Klaar!
print("\nYou completed the game in {0} moves. The number of optimal moves was {1}.".format(num_user_moves, num_optimal_moves))
