from bottle import get, post, response, request, run, view

##############################
@get("/login")
@view("login")
def _():
  return 


##############################
@get("/admin")
@view("admin")
def _():
  return



##############################
@post("/login")
def _():
  # VALIDATE
  user_email = request.forms.get("user_email")
  print(user_email)
  response.set_cookie("user_email", user_email)
  return "x"


##############################
run(host="127.0.0.1", port=3333, debug=True, reloader=True)

