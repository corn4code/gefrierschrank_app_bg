from item_class import *

obj_list = []
obj = Item("Kroketten", "30.12.22", "Kartoffeln")
obj_list.append(obj)
obj = Item("Pommes riffel", "31.12.2024","Pommes")
obj_list.append(obj)
obj = Item("Brezeln", "15.05.2022", "Backwaren")
obj_list.append(obj)
obj = Item("Steak", "13.5.22", "Fleisch")
obj_list.append(obj)
for obj in obj_list:
    print(obj.name,"\t",obj.mhd,"\t",obj.compair_mhd,"\t",obj.dof,"\t",obj.compair_dof,"\t",obj.kategorie)


def sort_mhd_low_high(obj_list):
    rank_list = []
    for obj in obj_list:
        platz = 0
        if len(rank_list) == 0:
            rank_list.append(obj)
        else:
            for i in range(len(rank_list)):
                for j in range(3):
                    if obj.compair_mhd[j] > rank_list[i].compair_mhd[j]:
                        platz += 1
                        break
                    if obj.compair_mhd[j] < rank_list[i].compair_mhd[j]:
                        platz += 0
                        break
                    if obj.compair_mhd[j] == rank_list[i].compair_mhd[j]:
                        continue
            rank_list.insert(platz, obj)
    for obj in rank_list:
        print(obj.name, obj.mhd)
    return rank_list


def sort_mhd_high_low(obj_list):
    rank_list = []
    for obj in obj_list:
        platz = 0
        if len(rank_list) == 0:
            rank_list.append(obj)
        else:
            for i in range(len(rank_list)):
                for j in range(3):
                    if obj.compair_mhd[j] < rank_list[i].compair_mhd[j]:
                        platz += 1
                        break
                    if obj.compair_mhd[j] > rank_list[i].compair_mhd[j]:
                        platz += 0
                        break
                    if obj.compair_mhd[j] == rank_list[i].compair_mhd[j]:
                        continue
            rank_list.insert(platz, obj)
    for obj in rank_list:
        print(obj.name, obj.mhd)
    return rank_list

def sort_dof_low_high(obj_list):
    rank_list = []
    for obj in obj_list:
        platz = 0
        if len(rank_list) == 0:
            rank_list.append(obj)
        else:
            for i in range(len(rank_list)):
                for j in range(3):
                    if obj.compair_dof[j] > rank_list[i].compair_dof[j]:
                        platz += 1
                        break
                    if obj.compair_dof[j] < rank_list[i].compair_dof[j]:
                        platz += 0
                        break
                    if obj.compair_dof[j] == rank_list[i].compair_dof[j]:
                        continue
            rank_list.insert(platz, obj)
    for obj in rank_list:
        print(obj.name, obj.dof)
    return rank_list

def sort_dof_high_low(obj_list):
    rank_list = []
    for obj in obj_list:
        platz = 0
        if len(rank_list) == 0:
            rank_list.append(obj)
        else:
            for i in range(len(rank_list)):
                for j in range(3):
                    if obj.compair_dof[j] < rank_list[i].compair_dof[j]:
                        platz += 1
                        break
                    if obj.compair_dof[j] > rank_list[i].compair_dof[j]:
                        platz += 0
                        break
                    if obj.compair_dof[j] == rank_list[i].compair_dof[j]:
                        continue
            rank_list.insert(platz, obj)
    for obj in rank_list:
        print(obj.name, obj.dof)
    return rank_list


print(sort_mhd_low_high(obj_list))
print("-----------")
print(sort_mhd_high_low(obj_list))
print("<!-----------!>")
print(sort_dof_low_high(obj_list))
print("-----------")
print(sort_dof_high_low(obj_list))