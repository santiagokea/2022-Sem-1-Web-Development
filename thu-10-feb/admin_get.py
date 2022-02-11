from bottle import get, view

##############################
@get("/admin")
@view("admin")
def _():
  return