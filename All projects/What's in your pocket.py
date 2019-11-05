items = []
for i in range(1,4):
    item = input("What's in your pocket? ")
    if item != "":
        items.append(item)
    else:
        break
else:
    print("Your pockets are full")


print("Your pocket contains:",items)
