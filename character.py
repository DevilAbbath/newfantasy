class Character:
    
    def __init__(self, name, pclass, level=1, exp=0):
        self.name = name
        self.level = level
        self.exp = exp
        self.pclass = pclass
    
    @property
    def status(self):
        return (
            f"NAME: {self.name.capitalize()}\n"
            f"LVL: {self.level}\n"
            f"EXP: {self.exp}\n"
            f"CLASS: {self.pclass}"
        )
    
    @status.setter
    def status(self, exp: int):
        temp_exp = self.exp + exp

        while temp_exp < 0:
            if self.level > 1:
                temp_exp += 100
                self.level -= 1
            else:
                temp_exp = 0

        while temp_exp >= 100:
            temp_exp -= 100
            self.level += 1

        self.exp = temp_exp

    def __lt__(self, other):
        return self.level < other.level

    def __gt__(self, other):
        return self.level > other.level

    def __eq__(self, other):
        return self.level == other.level
    
    def winprobability(self, creature):
        base_prob = 0.50
        if self > creature:
            base_prob = 0.66
        elif self < creature:
            base_prob = 0.33

        # Ajustar probabilidad basada en la clase del personaje
        settings = {
            "Orco": {"Paladin": 0.05, "Druid": -0.10, "Mage": 0.10, "Necromancer": -0.05},
            "Lobo": {"Paladin": -0.10, "Druid": 0.20, "Mage": -0.05, "Necromancer": 0.15},
            "Dragón": {"Paladin": 0.15, "Druid": -0.05, "Mage": 0.25, "Necromancer": -0.25}
        }

        adjustment = settings.get(creature.name, {}).get(self.pclass, 0)
        probability = base_prob + adjustment
        return min(max(probability, 0), 1)  # Asegura que esté entre 0 y 1

    @staticmethod
    def fightmode(mobname, probability, exp_gain, exp_loss):
        print(f"\nThe probability of winning against the {mobname} is {int(probability * 100)}%.")
        print(f"If you win, you will receive {exp_gain} experience points, and the creature will lose {exp_loss}.")
        print(f"If you lose, you will lose {exp_loss} experience points, and the creature will gain {exp_gain}.")
        return int(input("What do you want to do? (1: Attack, 2: Run): "))