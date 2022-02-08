from bottle import error, get, run, view

##############################
@get("/")
@view("index")
def _():
  return

##############################
@error(404)
@view("404")
def _(error):
  print(error)
  return

##############################
run(host="127.0.0.1", port=3333, debug=True, reloader=True)















