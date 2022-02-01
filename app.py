from bottle import get, run 

##############################
@get("/")
def show_index_page():
  print("I am here")
  return "Home"

##############################
# port from 0 to 65535
# reservedfrom 0 to 1024

run( host="127.0.0.1", port=3333, debug=True, reloader=True  )






















