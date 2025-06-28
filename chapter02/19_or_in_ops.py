choice = "q"
# 1
if choice == 'q' or choice == 'Q':
    print("Quit")
else:
    print("Continue")

# 2
if choice.upper() == 'Q':
    print("Quit")
else:
    print("Continue")

# 3
if choice in ("q", 'Q'):
    print("Quit")
else:
    print("Continue")