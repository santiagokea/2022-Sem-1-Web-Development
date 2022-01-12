from bottle import run, get



##############################
@get("/")
def do():
  xxx
  return "x"






##############################
run(host="127.0.0.1", port=55555, debug=True, reloader=True)
