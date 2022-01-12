from bottle import run, get, static_file, template, view


##############################
@get("/app.css")
def do():
  return static_file("app.css", root=".")

##############################
@get("/")
# @view("index.html")
def do():
  return template("index.html", title="My App")






##############################
run(host="127.0.0.1", port=5555, debug=True, reloader=True)
