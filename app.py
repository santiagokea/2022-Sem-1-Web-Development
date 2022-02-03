from bottle import run, get, response, request, post
import json


items = [
  {"id":"1", "name":"a"},
  {"id":"2", "name":"b"},
  {"id":"3", "name":"c"}
]


##############################
# decorator
@get("/")
def _():
  return "Home"

##############################
@get("/items")
def _():
  return json.dumps(items)
  # return str(items)

##############################7
# Query strings
# Every other variable after the 1st one start with & (ampersant)
# 127.0.0.1:4444/test?id=1&name=a
# from postman pass the following variables to the server via 
# Query String      year, school-name, age
# The server will reply with this:
# Hi, you are at KEA. The year is 2022 and you are 20 years old
#                ___              ____             __

@get("/test")
def _():
  year = request.params.get("year")
  school_name = request.params.get("school-name") 
  age = request.params.get("age") 
  return f"Hi year: {year} school name: {school_name} age: {age}"

##############################
# 127.0.0.1:4444/friendly/brand/xxxx/color/xxx
@get("/friendly/brand/<brand_name>/color/<item_color>")
def _(brand_name, item_color):
  return f"You brand: {brand_name} color is: {item_color}"



##############################
@post("/items")
def _():
  user_name = request.forms.get("name")
  return f"Hi {user_name}"


##############################
#KWARGS
# ports 0 to 65535
# ports 0 to 1024 are reserved
run(host="127.0.0.1", port=4444, debug=True, reloader=True)







