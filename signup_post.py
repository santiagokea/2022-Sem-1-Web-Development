from bottle import post, request, redirect
import uuid
import g

##############################
@post("/signup")
def _():
  # VALIDATE


  user_id = str(uuid.uuid4())
  user_email = request.forms.get("user_email")
  user_name = request.forms.get("user_name")
  user = {"id":user_id, "email":user_email, "name":user_name}
  g.USERS.append(user)
  return redirect(f"/signup-ok?user-email={user_email}&user-name={user_name}")