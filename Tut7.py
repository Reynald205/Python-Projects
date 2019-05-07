class Enemy:

    def __init__(self, x):
        self.life = x

    def get_energy(self):
        print(self.life)

    def attack(self):  # Self means to use from its own class
        print("Ouch")
        self.life -= 1

    def check_life(self):
        if self.life <= 0:
            print("Arrgh I have been slain.")
        else:
            print(str(self.life)+" life left")
enemy1 = Enemy(3)  # How objects are made to call class functions
enemy2 = Enemy(8)  # With this init a value must be entered for the class
enemy1.attack()
enemy1.get_energy()
enemy1.attack()
enemy2.get_energy()
enemy1.check_life()
enemy2.check_life()