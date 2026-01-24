#📖 The Spellbook: Context Managers (__enter__ & __exit__)

#⚔️ Training Grounds: The Session Log
class GameSession():
    def __init__(self, player_name):
        self.player_name = player_name
    def __enter__(self):
        print(f"Player {self.player_name} has entered the Nexus.")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Player {self.player_name} has left the Nexus. Progress saved.")


#📜 Legendary Tip: The Suppression Silence
# Grand Architect, if your __exit__ method ever returns the boolean value True, it acts as a Silence Spell. 
# It tells Python: 'I have handled the error, do not let it crash the program.' If it returns None or False, 
# the error will continue to rise and potentially end the game!


class PersistenceManager():
    def __init__(self, filename):
        self.filename = filename
    def __enter__(self):
        self.file = open(self.filename, 'a')
        return  self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Ledger safely sealed.")
        self.file.close()



#📜 BOSS FIGHT: The Curator of the Eternal Log

#Side Quest: The Combat Logger
class CombatContext():
    def __init__(self):
        pass
    def __enter__(self):
        print("--- COMBAT LOG START ---")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("--- COMBAT LOG END ---")


#Main Quest: The Atomic Transaction
class GoldTransaction():
    def __init__(self, player_obj, cost):
        self.player_obj = player_obj
        self.cost = cost
    def __enter__(self):
        if self.player_obj["gold"] >= self.cost:
            return self.player_obj
        else:
            raise ValueError("Too poor!")
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("Gold safe. Transaction aborted.")
        else:
            print("Gold deducted. Transaction finalized.")



#⚔️ LEGENDARY QUEST: The "Atomic" Save-Point
import os
class AtomicSave():
    def __init__(self, filename):
        self.filename = filename
    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type:
            print(f"CRITICAL SAVE ERROR: {exc_val}. Deleting corrupted file.")
            os.remove(self.filename)
        else:
            print("Save Successful.")
