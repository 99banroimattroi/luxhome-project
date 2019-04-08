
from db import*
from decode import *

def search_(name):
    #lay du tat ca du lieu datahome_collection tren mongo
    abc = datahome_collection.find()
    all_data = []
    for i in abc:
        all_data.append(i)

    
#lay list cua search_data
    tatcadiadiem = []
    for ab in all_data:
        a = ab["search_data"]
        tatcadiadiem.append(a)
#name a cua dia diem can tim
    diadiemcuthe = name
#lay nhung du lieu tu tat ca dia diem
    new_list = []
    for i in tatcadiadiem:
        if i.find(diadiemcuthe)!= None:
            new_list.append(i)
    list_dulieucuadiadiemcantim = []

    for i in all_data:
        # print(i["search_data"])
        for j in new_list:
            if i["search_data"] == j:
                list_dulieucuadiadiemcantim.append(i)
    return list_dulieucuadiadiemcantim









