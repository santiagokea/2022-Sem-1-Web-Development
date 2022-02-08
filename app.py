from bottle import error, get, run, static_file, view

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
  return

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
@error(404)
@view("404")
def _(error):
  print(error)
  return

##############################
run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")















