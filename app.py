from bottle import default_app, delete, get, post, put, request, response, run, view
import g

tweets = {}

##############################
@post("/tweets")
def _():
  # Validate
  if not request.forms.get("tweet_text"):
    return "tweet_text missing"
  tweet_text = request.forms.get("tweet_text").strip()
  print(tweet_text)
  if len(tweet_text) < g.TWEET_MIN_LEN:
    return f"tweet min {g.TWEET_MIN_LEN}"
  if len(tweet_text) > g.TWEET_MAX_LEN:
    return f"tweet max {g.TWEET_MAX_LEN}"

  # Success  
  return "tweet created"

##############################
@put("/tweets/<id>")
def _(id):
  return "tweet updated"

##############################
@delete("/tweets/<id>")
def _(id):
  return "tweet deleted"

##############################
@get("/tweets/<id>")
def _(id):
  return "this is the tweet"

##############################
@get("/tweets")
def _():
  return tweets


##############################
try:
  # Production
  import production
  application = default_app()
except:
  # Development
  run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")






