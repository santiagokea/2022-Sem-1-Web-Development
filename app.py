from bottle import error, get, post, redirect, request, run, static_file, view

items = [
  {"id":"b0bafe8f-de0e-4fb2-b3cb-f284e9d5e2ce", "name":"a", "price": 10},
  {"id":"d097c638-83d5-4ec5-a1db-51e1a09767a7", "name":"b", "price": 20},
  {"id":"43119a37-98a0-4e77-8ff4-b724cbaf0d3d", "name":"c", "price": 30}
]


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
@get("/items")
@view("items")
def _():
  return dict(items=items)

##############################
@get("/signup")
@view("signup")
def _():
  return

##############################
@get("/login")
@view("login")
def _():
  return

##############################
@post("/delete-item")
def _():
  # VALIDATE
  item_id = request.forms.get("item_id")
  return redirect("/items")



##############################
@error(404)
@view("404")
def _(error):
  print(error)
  return

##############################
run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")















