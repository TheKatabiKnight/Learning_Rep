import asyncio



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

###Skill Cooldowns###
async def cooldown_timer(skill_name, seconds):
    print(f"{skill_name} on cooldown...")
    await asyncio.sleep(seconds)
    print(f"{skill_name} is ready!")
async def main_combat_loop(skills):
    await asyncio.gather(*(cooldown_timer(s) for s in skills))



