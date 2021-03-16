from random import randint
def g_id():
    return randint(0000,9999)

class dex():
    creatures = []

class creature():
    def __init__(self, name, mhp, c_dmg, c_affinity):
        self.name = name
        self.mhp = mhp
        self.c_dmg = c_dmg
        self. c_hex = []
        self.c_id = g_id
        self.c_affinity = c_affinity

a1 = creature('Azilo',10,1,'dark')

print(a1.c_id())