from random import randint

def g_uid():
    return randint(0000,9999)

class creature():
    def __init__(self, name, mhp, c_dmg, c_affinity):
        self.name = name.lower
        self.mhp:int = mhp
        self.c_dmg:int = c_dmg
        self.c_hex = []
        self._c_uid = g_uid
        self.c_affinity = c_affinity

a1 = creature('Azilo',6,3,'dark')
a2 = creature('Beam',12,2,'light')
a3 = creature('crustEr',20,1, 'stone')

index = open('cindex.txt','r')

for line in index:
    print(line)
