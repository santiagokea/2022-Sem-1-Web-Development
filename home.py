from bottle import get, view

@get("/")
@view("index")
def _():
  return
