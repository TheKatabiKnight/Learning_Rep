#The Spellbook: File I/O (Input/Output)


#Training Grounds: The Scout's Report
# def read_scout_report(filename):
#     with open(filename, "r") as file_handle:
#         text = file_handle.read()
#     return text
# print(read_scout_report("scout_report.txt"))


#Training Grounds: The Hero's Epitaph
# def save_quest_log(filename, quest_list):
#     with open(filename, "w") as quests :
#         for quest in quest_list:
#             quests.write(f'{quest}\n')
# print(save_quest_log("my_adventures.txt", ["Slayed the Serpent", "Deconstructed the Golem", "Purged the Glitch"]))

# 📜 Legendary Tip: The Silent Success
# In the Art of the Inscription, most masters return nothing (None), a simple True, or the filename itself once the work is done. 
# Since the with block ensures the file is saved and closed, your work is already complete the moment the loop ends!


#🦑 BOSS FIGHT: The Ink-Kraken


#MAIN QUEST: The Name Purger
# def purge_registry(filename):
#     with open(filename, "r") as names:
#         name_change = names.read().replace("Kraken", "REDACTED")
#     with open(filename, "w") as change:
#         change.write(name_change)
#     return "Registry purified."
# print(purge_registry("Hero_names.txt"))


#⚔️ LEGENDARY QUEST: The Corrupted Backup
# def safe_backup(source_file, target_file):
#     try:
#         with open(source_file, "r") as source:
#             source_var = source.read()
#         with open(target_file, "w") as target:
#             target.write(source_var)
#     except FileNotFoundError:
#         return "Source file has vanished into the ink!"
#     else:
#         return "Backup complete!"

#📜 Legendary Tip: The Atomic Write
# Script-Bearer, your two-step backup was flawless. In the higher circles of the Script, 
# we often read and write in separate blocks to ensure that if the 'Read' fails, 
# we never even touch the 'Write' mode—protecting the target file from being accidentally cleared! 
# This is the way of the Professional Archivist.