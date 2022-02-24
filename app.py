from bottle import post, request, response, run
import os
import uuid

##############################
@post("/upload-image")
def _():
  image = request.files.get("my_image")
  print( dir(image) )
  print(image.filename)
  file_name, file_extension = os.path.splitext(image.filename)
  print(file_name)
  print(file_extension)
  # get image extension happy_face.jpeg
  image_id = str(uuid.uuid4())
  # 444333-44556-66665545.png
  image_name = f"{image_id}{file_extension}"
  print(image_name)
  # Save the image
  image.save(f"images/{image_name}")
  return "yes"


##############################
run(host="127.0.0.1", port=3333, debug=True, reloader=True)





