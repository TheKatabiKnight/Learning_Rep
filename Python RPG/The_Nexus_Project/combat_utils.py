###Spell Usage###
def create_mana_pool(max_mana):
    def spend_mana(amount):
        nonlocal max_mana
        if amount <= max_mana:
            max_mana -= amount
            return max_mana
        else:
            return "Insufficient Mana!"
    return spend_mana