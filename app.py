from bottle import get, post, response, request, run, view
import uuid

cookie_secret = "this is the secret key"

##############################
@get("/login")
@view("login")
def _():
  return 

##############################
@get("/admin")
@view("admin")
def _():
  user_email = request.get_cookie("user_email", secret=cookie_secret)
  return dict(user_email=user_email)



##############################
@post("/login")
def _():
  # VALIDATE
  user_email = request.forms.get("user_email")
  print(user_email)
  response.set_cookie("user_email", user_email, secret=cookie_secret)
  user_session_id = str(uuid.uuid4())
  response.set_cookie("uuid4", user_session_id)
  return "x"


##############################
run(host="127.0.0.1", port=3333, debug=True, reloader=True)

