import cindex

class dex:
    def __init__(self):
        self.creatures = []

    def search_dex(self, var_name):
        Results = []
        for cr in self.creatures:
            if cr.name == var_name.lower():
                Results.append(cr)
        return Results

    def print_list_dex(self):
        for cr in self.creatures:
            print(cr.name)
