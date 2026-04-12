def get_welcome_message():
    return "Welcome to the Alpha of :"
def Training_Grounds():
    while True:
        choice = input("Would you like to start your training? (Y/N) : ").lower()
        if choice == "y":
            print("Welcome to the training grounds!")
            break
        elif choice == "n":
            print("Closing game!")
            break
        else:
            print("Invalid input!")