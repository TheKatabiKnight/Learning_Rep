###Game name/Difficulty governance###
class NexusConfig:
    WORLD_NAME = "The Nexus"
    DIFFICULTY = "Normal"
    @classmethod
    def update_difficulty(cls, new_diff):
        cls.DIFFICULTY = new_diff
        return cls.DIFFICULTY
    @staticmethod
    def format_header(title):
        return f"--- {title} ---"