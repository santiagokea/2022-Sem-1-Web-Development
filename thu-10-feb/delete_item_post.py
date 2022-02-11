from bottle import post, redirect, request
import g

##############################
##############################
##############################
@post("/delete-item")
def _():
  # VALIDATE
  item_id = request.forms.get("item_id")
  # Delete the item for if enumarate
  for index, item in enumerate(g.ITEMS):
    if item["id"] == item_id:
      g.ITEMS.pop(index)
      return redirect("/items")

  return redirect("/items")