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
  name = "Santiago" # string - text
  year = 2022 # integer
  return f"Hi {name} the year is {year}" # f string 
  # return "Hi " + name + " it is " + str(year) 
  # return str(year) # type-cast or cast


##############################
# port from 0 to 65535
# reservedfrom 0 to 1024

run( host="127.0.0.1", port=3333, debug=True, reloader=True  )






















