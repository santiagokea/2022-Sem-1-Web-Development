from bottle import get, view
# from g import ITEMS
import g

##############################
@get("/items")
@view("items")
def _():
  return dict(items=g.ITEMS)