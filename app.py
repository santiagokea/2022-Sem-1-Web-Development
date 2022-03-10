from bottle import default_app, delete, get, post, put, request, response, run, view
import uuid

##############################
@get("/")
@view("index")
def _():
  return


##############################
@post("/tweet")
def _():
  # Validate
  # Connect to the db
  # Insert the tweet in the tweets table
  # response.status = 200
  tweet_id = str(uuid.uuid4())
  return tweet_id


















##############################
try:
  # Production
  import production
  application = default_app()
except:
  # Development
  run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")






