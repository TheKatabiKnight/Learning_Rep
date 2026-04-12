hp = 100
inventory = []
max_inv = 2

while True:
    print(f"HP: {hp} | Bag: {inventory}")
    action = input("Action (take/hazard/exit): ").lower()
    if action == "take":
        if len(inventory) < max_inv:
            inventory.append("Relic")
        else:
            print("Bag full!")
    elif action == "hazard":
        hp -= 50
    elif action == "exit":
        print("Exiting...")
        break
    else:
        print("Unknown command!")
    if hp <= 0:
        print("Game Over")
        break