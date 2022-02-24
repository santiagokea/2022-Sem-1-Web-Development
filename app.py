from bottle import default_app, get, run, view

##############################
@get("/")
@view("index")
def _():
  return

##############################
@get("/about-us")
@view("about-us")
def _():
  return 

##############################
@get("/contact-us")
@view("contact-us")
def _():
  return


##############################
try:
  # Production
  import production
  application = default_app()
except:
  # Development
  run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")






