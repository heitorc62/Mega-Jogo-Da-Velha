import sys
x = 2
y = 6

#assert(x + y == 7), "You have chosen invalid teams!"


try:
    assert(x + y == 7), "You have chosen invalid teams! The game will be interrupted."
except Exception as e:
    print(e)
    sys.exit(1)

    
if x + y != 7:
    print("You have chosen invalid teams! The game will be interrupted.")
    sys.exit(1)

print("AQUI")