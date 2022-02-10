from bottle import error, get, post, redirect, request, run, static_file, view
import uuid
import re

regex_email = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'


##############################
import home_get         # GET  
import signup_get       # GET   
import login_get        # GET
import users_get        # GET
import items_get        # GET
import admin_get        # GET
import signup_ok_get    # GET


##############################
@get("/app.css")
def _():
  return static_file("app.css", root=".")



##############################
##############################
##############################
@post("/delete-item")
def _():
  # VALIDATE
  item_id = request.forms.get("item_id")
  # Delete the item for if enumarate
  for index, item in enumerate(items):
    if item["id"] == item_id:
      items.pop(index)
      return redirect("/items")

  return redirect("/items")

##############################
@post("/signup")
def _():
  # VALIDATE


  user_id = str(uuid.uuid4())
  user_email = request.forms.get("user_email")
  user_name = request.forms.get("user_name")
  user = {"id":user_id, "email":user_email, "name":user_name}
  users.append(user)
  return redirect(f"/signup-ok?user-email={user_email}&user-name={user_name}")


##############################
@post("/login")
def _():
  # VALIDATE
  # FIRST THING: Always check if the vriable was passed in the form
  if not request.forms.get("user_email"):
    return redirect("/login?error=user_email")    
  if not re.match(regex_email, request.forms.get("user_email")):
    return redirect("/login?error=user_email")

  user_email = request.forms.get("user_email")

  # FIRST THING: Always check if the vriable was passed in the form
  if not request.forms.get("user_password"):
    return redirect(f"/login?error=user_password&user_email={user_email}")
  if len(request.forms.get("user_password")) < 6:
    return redirect(f"/login?error=user_password&user_email={user_email}")
  if len(request.forms.get("user_password")) > 50:
    return redirect(f"/login?error=user_password&user_email={user_email}")

  # SUCCESS
  return redirect("/admin")

##############################
@error(404)
@view("404")
def _(error):
  print(error)
  return

##############################
run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")















