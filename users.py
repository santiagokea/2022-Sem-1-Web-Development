from bottle import get, view
import g



##############################
@get("/users")
@view("users")
def _():
  return dict(users=g.USERS)