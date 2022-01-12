from bottle import run, get



##############################
@get("/")
def do():
  return "xxx"






##############################
run(host="127.0.0.1", port=55555, debug=True, reloader=True)
