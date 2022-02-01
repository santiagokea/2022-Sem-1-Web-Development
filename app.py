from bottle import get, run, static_file, view

# dictionary
person = {"id":"1", "name":"Santiago"}
  # person["last_name"] = "Donoso"

##############################
@get("/person/<person_id>")
def _(person_id):
  return person_id



##############################
@get("/app.css")
def _():
  return static_file("app.css", root=".")


##############################
@get("/")
@view("index.html")
def _():
  return 







##############################
@get("/items")
@view("items")
def _():
  letters = ["a", "c", "x"]
  # ternary
  return "yes" if "x" in letters else "no"





  # print(type(letters))
  # letters.append("d")
  # print( dir(letters) )
  # is_b_in_list = "no"
  # if "b" in letters: is_b_in_list = "yes"

  # if "b" in letters:
  #   pass
  # else:
  #   pass

  # letters = ["a", "b", "c"]
  # print("#"*30)
  # print(letters)
  # return letters

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






















