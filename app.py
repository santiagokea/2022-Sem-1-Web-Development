from bottle import get, run 

##############################
@get("/")
def _():
  print("I am here")
  return "Home"

##############################
@get("/items")
def _():
  return "items"

##############################
@get("/item")
def _():
  return "item"

##############################
# port from 0 to 65535
# reservedfrom 0 to 1024

run( host="127.0.0.1", port=3333, debug=True, reloader=True  )






















