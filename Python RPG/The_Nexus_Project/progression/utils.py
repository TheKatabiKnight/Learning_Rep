from progression.utils import get_welcome_message, Training_Grounds
from config import NexusConfig
from src.entities.Entities import Warrior, CombatEntity, Stats







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

def character_creation():
    New_Player = input("Please choose a name for your character! : ")
    character_created = CombatEntity(New_Player, 100, 100)
    strength = Stats(5)
    accuracy = Stats(4)
    constitution = Stats(3)
    print(f"Welcome {New_Player} to {NexusConfig.WORLD_NAME}!")
    
    while True:
        Player_Class = input("Please choose your class (Warrior only for now):").lower()
        match Player_Class:
            case  "warrior":
                chosen_class = Warrior(New_Player)
                break
            case _:
                print("invalid input! try again")
        
    print(f"character status : \n{character_created} \nClass : {chosen_class.get_role()} \nStats :\nStrength : {strength.stat} \nAccuracy : {accuracy.stat} \nConsitution : {constitution.stat}")