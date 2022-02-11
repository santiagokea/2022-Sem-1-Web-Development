from bottle import get, post, redirect, response, request, run, view
import uuid


cookie_secret = "this is the secret key"
sessions = []

##############################
@get("/logout")
def _():
  user_session_id = request.get_cookie("uuid4")
  sessions.remove(user_session_id)
  return redirect("/login")



##############################
@get("/login")
@view("login")
def _():
  return 

##############################
@get("/admin")
@view("admin")
def _():
  user_session_id = request.get_cookie("uuid4")
  # compare the uuid from the cookie to the uuid from the sessions
  if user_session_id not in sessions:
    return redirect("/login")
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
  sessions.append(user_session_id)
  response.set_cookie("uuid4", user_session_id)
  return redirect("/admin")


##############################
run(host="127.0.0.1", port=3333, debug=True, reloader=True)

