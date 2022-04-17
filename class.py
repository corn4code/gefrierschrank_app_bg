class Item:
    def __init__(self, name, mhd, dof, kategorie):
        self.name = name
        self.mhd = mhd
        self.dof = dof
        self.kategorie = kategorie

obj_list = []
obj = Item("Pizza Speziale", "15.05.2022","17.04.2022","Pizza")
obj_list.append(obj)
obj = Item("Brezeln", "15.05.2022","17.04.2022", "Backwaren")
obj_list.append(obj)

for obj in obj_list:
    print(obj.name,obj.mhd)