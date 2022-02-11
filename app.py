from bottle import get, run, view

##############################
@get("/login")
@view("login")
def _():
  return 

##############################



##############################
run(host="127.0.0.1", port=3333, debug=True, reloader=True)

