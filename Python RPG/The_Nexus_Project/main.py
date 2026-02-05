from utils import get_welcome_message
from config import NexusConfig
from Entities import Warrior, CombatEntity

import persistence

###Game Start###
if __name__ == "__main__" :
    print(get_welcome_message())
    print(NexusConfig.format_header(NexusConfig.WORLD_NAME))
    difficulty = NexusConfig.update_difficulty(input("Please Choose difficulty (Easy/Normal/Hard)"))
    print(f"{difficulty} difficulty chosen!!")

###Character Creation###
if __name__ == "__main__" :
    New_Player = input("Please choose a name for your character! : ")
    character_created = CombatEntity(New_Player, 100, 100)
    print(f"Welcome {New_Player} to {NexusConfig.WORLD_NAME}!")
    
    while True:
        Player_Class = input("Please choose your class (Warrior only for now):").lower()
        match Player_Class:
            case  "warrior":
                chosen_class = Warrior(New_Player)
                break
            case _:
                print("invalid input! try again")
        
    print("Find bellow your character status :")
    print(character_created)
    print(f"Class : {chosen_class.get_role()}")
    

    