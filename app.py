from bottle import error, get, post, redirect, request, run, static_file, view
import uuid
import re

items = [
  {"id":"b0bafe8f-de0e-4fb2-b3cb-f284e9d5e2ce", "name":"a", "price": 10},
  {"id":"d097c638-83d5-4ec5-a1db-51e1a09767a7", "name":"b", "price": 20},
  {"id":"43119a37-98a0-4e77-8ff4-b724cbaf0d3d", "name":"c", "price": 30}
]


# must have an id and an email
users = []

regex_email = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'

##############################
@get("/app.css")
def _():
  return static_file("app.css", root=".")

##############################
@get("/")
@view("index")
def _():
  return

##############################
@get("/admin")
@view("admin")
def _():
  return


##############################
@get("/items")
@view("items")
def _():
  return dict(items=items)

##############################
@get("/users")
@view("users")
def _():
  return dict(users=users)


##############################
@get("/signup")
@view("signup")
def _():
  return

##############################
# query string expected with user-email
@get("/signup-ok") 
@view("signup-ok")
def _():
  user_email = request.params.get("user-email")
  user_name = request.params.get("user-name")
  return dict(user_email=user_email, user_name=user_name)


##############################
# Query string will be used in this route
# Eg: /login?error=user_email
# Eg: /login?error=user_password
# Eg: /login?error=user_password&user_email=a@a.cm
@get("/login")
@view("login")
def _():
  error = request.params.get("error")
  user_email = request.params.get("user_email")
  return dict(error=error, user_email=user_email)


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















