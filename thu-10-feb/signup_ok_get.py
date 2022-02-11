from bottle import get, view, request

##############################
# query string expected with user-email
@get("/signup-ok") 
@view("signup-ok")
def _():
  user_email = request.params.get("user-email")
  user_name = request.params.get("user-name")
  return dict(user_email=user_email, user_name=user_name)