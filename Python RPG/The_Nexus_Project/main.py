from progression.utils import get_welcome_message, Training_Grounds
from config import NexusConfig
from src.entities.Entities import Warrior, CombatEntity, Stats
from progression.story import training_part1
import asyncio
import src.core.persistence as ps

###Game Start###
if __name__ == "__main__" :
    print(get_welcome_message())
    print(NexusConfig.format_header(NexusConfig.WORLD_NAME))
    #difficulty for later#
    # difficulty = NexusConfig.update_difficulty(input("Please Choose difficulty (Easy/Normal/Hard)"))
    # print(f"{difficulty} difficulty chosen!!")

###Character Creation###
if __name__ == "__main__" :
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
###Training Grounds###
if __name__ == "__main__" :
    Training_Grounds()
    asyncio.run(training_part1())
    


    
    

    