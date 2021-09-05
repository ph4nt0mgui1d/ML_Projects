shoppingList = []

while(True):
    items = input("Add items: ")
    if(items == "DONE"):
        break
    
    shoppingList.append(items)

# print(shoppingList)                           (or)

for item in shoppingList:
    print(item)
