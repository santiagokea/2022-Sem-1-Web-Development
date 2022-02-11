from bottle import get, view, request

##############################
# Query string will be used in this route
# Eg: /login?error=user_email
# Eg: /login?error=user_password
# Eg: /login?error=user_password&user_email=a@a.cm
@get("/login")
@view("login")
def _():
  error = request.params.get("error")
  user_email = request.params.get("user_email")
  return dict(error=error, user_email=user_email)