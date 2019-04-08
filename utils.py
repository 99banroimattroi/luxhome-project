from db import datahome_collection, datafeedback_collection
from bson import ObjectId
import re
def add_data(name, summary, introduction, unique_features, special_note, rating, featured_photo,Mon_to_thurs,Fri_to_sun,Phi_tang_them,So_dem_toi_thieu,So_dem_toi_da,checkin_time,checkout_time,address_line,search_data,city,state,country,full_address,photos_1,photos_2,photos_3,photos_4,photos_5,photos_6,photos_7,photos_8):
    data = {
        "name": name,
        "summary": summary,
        "introduction": introduction,
        "unique_features":unique_features,
        "special_note": special_note,
        "rating": rating,
        "featured_photo": featured_photo,
 
        "Mon_to_thurs": Mon_to_thurs,
        "Fri_to_sun": Fri_to_sun,
        "Phi_tang_them": Phi_tang_them,
        "So_dem_toi_thieu": So_dem_toi_thieu,
        "So_dem_toi_da": So_dem_toi_da,
        "checkin_time": checkin_time,
        "checkout_time": checkout_time, 

        "address_line": address_line,
        "search_data": search_data,
        "city": city,
        "state": state,
        "country": country,
        "full_address": full_address,

        "photos_1": photos_1,
 

        "photos_2": photos_2,

  
        "photos_3": photos_3,
  
  
        "photos_4": photos_4,

 
        "photos_5": photos_5,
 
 
        "photos_6": photos_6,
  
 
        "photos_7": photos_7,
     
   
        "photos_8": photos_8,
       

    }
    datahome_collection.insert_one(data)

def contact(name,email,note):
    add_feedback = {
        "Name": name,
        "Email": email,
        "Enternote": note,
    }
    datafeedback_collection.insert_one(add_feedback)

def get_by_id(id_it):
    found = datahome_collection.find_one({"_id": ObjectId(id_it)})
    return found

def get(query):
    f = datahome_collection.find(query)
    return f

def cleanhtml(raw_html):
    cleaner = re.compile('<.*?>')
    cleantext = re.sub(cleaner, ' ', raw_html)
    return cleantext

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
#lay du lieu nhung dia diem can tim
    for i in all_data:
        for j in new_list:
            if i["search_data"] == j:
                list_dulieucuadiadiemcantim.append(i)
    return list_dulieucuadiadiemcantim


def search_address(address):
    address = datahome_collection.find( {  "search_data": { "$regex": address } } )
    return address

def data_review():
    data = datafeedback_collection.find({})
    return data