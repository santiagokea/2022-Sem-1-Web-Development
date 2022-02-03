from bottle import run, get

##############################
# decorator
@get("/")
def _():
  return "Home"

##############################
@get("/items")
def _():
  return "items"


##############################
#KWARGS
# ports 0 to 65535
# ports 0 to 1024 are reserved
run(host="127.0.0.1", port=4444, debug=True, reloader=True)











