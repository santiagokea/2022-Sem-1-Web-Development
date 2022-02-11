from bottle import get, view

@get("/signup")
@view("signup")
def _():
  return