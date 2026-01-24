import os




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