from flask import Flask, render_template, request,redirect, session
import utils
from db import*
from decode import *

app = Flask(__name__)

@app.route("/")
def home():
  hs_l = utils.get({})
  return render_template("index.html", hs_list = hs_l)

@app.route("/search", methods =["GET","POST"])
def search_address():
  if request.method == "GET": 
    return render_template("search.html")
  elif request.method == "POST":
    form = request.form
    name = form["search"]
    name_search = no_accent_vietnamese(name).lower()
    
    # print(list_data)
 
  
    return redirect('/search/{}'.format(name_search))
    # return str(list_data[0])


@app.route("/search/<name_search>", methods = ["GET"])
def search_hotel(name_search):
  
  data_list_check = utils.search_address(name_search)
  data_list = []
  for i in data_list_check:
    data_list.append(i)
  for j in data_list:
    j["introduction_form"] = utils.cleanhtml(j["introduction"])
    
  if len(data_list) != 0:
    return render_template("searchdetail.html", data_list = data_list)
  else:
    return render_template("failsearchdetail.html", name = name_search)

  
  
# def search():
#   if request.method == "GET": 
#     return render_template("search.html",methods=["GET","POST"])
#   elif request.method == "POST":
#     form = request.form
#     name = form["search"]
#     name = no_accent_vietnamese(name)
#     list_data = utils.search_(name)
#     return "ok"
    # return render_template("searchdetail.html",lis_data = list_data)


@app.route("/searchdetail")
def searchdetail():
  return render_template("searchdetail.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/feedback", methods =["GET","POST"])
def contact():
  if request.method == "GET": 
    return render_template("feedback.html", methods=["GET","POST"])
  elif request.method == "POST":
    form = request.form

    name = form["name"]
    email = form["email"]
    note = form["Enternote"]

    utils.contact(name,email,note)
    return render_template("feedback.html")

@app.route("/detail/<id>")
def details(id):
  dt = utils.get_by_id(id)
  introduction = utils.cleanhtml(dt["introduction"])
  s_note = utils.cleanhtml(dt["special_note"])
  u_fts = utils.cleanhtml(dt["unique_features"])
  f_t = dt["featured_photo"]
  m_f = dt["Phi_tang_them"]
  min_ = dt["So_dem_toi_thieu"]
  max_ = dt["So_dem_toi_da"]
  c_in = dt["checkin_time"]
  c_out = dt["checkout_time"]
  add = dt["full_address"]
  m_t = dt['Mon_to_thurs']
  f_s = dt["Fri_to_sun"]
  pt_1 = dt["photos_1"]
  pt_2 = dt["photos_2"]
  pt_3 = dt["photos_3"]
  pt_4 = dt["photos_4"]
  return render_template("detail.html", introduction = introduction, name = dt["name"], pt_1 = pt_1, pt_2 = pt_2, pt_3 = pt_3, pt_4 = pt_4, s_note = s_note, u_f = u_fts, m_t = m_t, f_s = f_s, m_f = m_f, min = min_, max = max_, c_in = c_in, c_out = c_out, add = add, f_t = f_t)

app.config["SECRET_KEY"] = "fagsdhkfj shkfdjhkhkjh"
@app.route("/login", methods = ["GET", "POST"])
def login():
  if request.method == "GET":
    return render_template("login.html", methods=["GET","POST"])
  elif request.method == "POST":
    #login logic
    username = request.form["username"]
    password = request.form["password"]
    if username != "admin": #check xem user co ton tai khong ?
      return "No such users"
    elif password != "admin1":  #check xem passwords match
      return "Wrong password"
    else:
      session["token"] = username
      return render_template("admin.html")

@app.route("/logout", methods =["GET","POST"])
def logout():
  del session["token"] 



@app.route("/admin")
def admin():
  return render_template("admin.html")

@app.route("/receive")
def receive():
  return render_template("receive.html")

@app.route("/viewadmin")
def viewadmin():
  return render_template("viewadmin.html")

@app.route("/addadmin")
def addadmin():
  return render_template("addadmin.html")

@app.route("/detailadmin")
def detailadmin():
  return render_template("detailadmin.html")

@app.route("/fixadmin")
def fixadmin():
  return render_template("fixadmin.html")

@app.route("/fbfullin4")
def fbfullin4():
  data_feedback = utils.data_review()
  return render_template("fbfullin4.html", data_feedback = data_feedback)

@app.route("/fbnotfullin4")
def fbnotfullin4():
  return render_template("fbnotfullin4.html")

@app.route("/add_data", methods =["GET","POST"])
def add_data():
  if request.method == "GET": 
    return render_template("add_database.html", methods=["GET","POST"])
  elif request.method == "POST":
    form = request.form
    name = form["name"]
    summary =  form["summary"]
    introduction = form["introduction"]
    unique_features = form["unique_features"]
    special_note = form["special_note"]
    rating = form["rating"]
    featured_photo = form["featured_photo"]
    Mon_to_thurs = form["Mon_to_thurs"]
    Fri_to_sun = form["Fri_to_sun"]
    Phi_tang_them = form["Phi_tang_them"]
    So_dem_toi_thieu = form["So_dem_toi_thieu"]
    So_dem_toi_da = form["So_dem_toi_da"]
    checkin_time = form["checkin_time"]
    checkout_time = form["checkout_time"]
    address_line = form["address_line"]
    search_data = form["search_data"]
    city = form["city"]
    state = form["state"]
    country = form["country"]
    full_address = form["full_address"]
    photos_1 = form["photos_1"]

    photos_2 = form["photos_2"]

    photos_3 = form["photos_3"]

    photos_4 = form["photos_4"]

    photos_5 = form["photos_5"]
 
    photos_6 = form["photos_6"]
  
    photos_7 = form["photos_7"]

    photos_8 = form["photos_8"]

  

    utils.add_data(name,summary,introduction,unique_features,special_note,rating,featured_photo,Mon_to_thurs,Fri_to_sun,Phi_tang_them,So_dem_toi_thieu,So_dem_toi_da,checkin_time,checkout_time,address_line,search_data,city,state,country,full_address,photos_1,photos_2,photos_3,photos_4,photos_5,photos_6,photos_7,photos_8) 

    return "OK !"



if __name__ == '__main__':
  app.run(debug=True)