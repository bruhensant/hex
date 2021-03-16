from random import randint

def g_id():
    return randint(0000,9999)

class dex:
    def __init__(self):
        self.creatures = []

    def search_dex(self, var_name):
        Results = []
        for cr in self.creatures:
            if cr.name == var_name.lower():
                Results.append(cr)
        return Results

class creature():
    def __init__(self, name, mhp, c_dmg, c_affinity):
        self.name = name.lower
        self.mhp = mhp
        self.c_dmg = c_dmg
        self. c_hex = []
        self.c_id = g_id
        self.c_affinity = c_affinity

a1 = creature('Azilo',6,3,'dark')
a2 = creature('Beam',12,2,'light')
a3 = creature('cruster',20,1, 'stone')

