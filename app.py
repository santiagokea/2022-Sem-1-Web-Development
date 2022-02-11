from bottle import get, post, run, view

##############################
@get("/login")
@view("login")
def _():
  return 

##############################
@post("/login")
def _():
  return "x"


##############################
run(host="127.0.0.1", port=3333, debug=True, reloader=True)

