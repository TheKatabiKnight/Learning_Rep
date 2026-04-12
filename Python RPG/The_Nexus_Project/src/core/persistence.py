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

def save_player_state(file_name, player):
    with AtomicSave(f"{file_name}") as f:
        f.write(f"{str(player.data.current_hp)}\n")
        f.write(f"{str(player.x)}\n")
        f.write(f"{str(player.y)}\n")
        f.write(f"{str(player.z)}\n")

def load_player_state(file_name):
    try:
        with open(f"{file_name}", "r") as f:
            lines = f.readlines()
            if len(lines) >= 4:
                hp = float(lines[0])
                x = float(lines[1])
                y = float(lines[2])
                z = float(lines[3])
                return {"player_current_hp": hp, "position": (x, y, z)}
        
        
    except :
        pass
    
    return {f"player_current_hp": 100, "position": (0, 1.5, 0)}
        