from bottle import post, request, response, run
import os
import uuid
import imghdr

##############################
@post("/upload-image")
def _():
  image = request.files.get("my_image")
  print( dir(image) )
  print(image.filename)
  file_name, file_extension = os.path.splitext(image.filename) # .png .jpeg .zip .mp4
  print(file_name)
  print(file_extension)
  
  # Validate extension
  if file_extension not in (".png", ".jpeg"):
    return "image not allowed"

  image_id = str(uuid.uuid4())
  # Create new image name
  image_name = f"{image_id}{file_extension}"
  print(image_name)
  # Save the image
  image.save(f"images/{image_name}")

  # Make sure that the image is actually a valid image
  # by readinf its mime type
  if file_extension != imghdr.what(f"images/{image_name}"):
    print("mmm... suspicious ... it is not really an image")
    # remove the invalid image from the folder
    os.remove(f"images/{image_name}")
    return "mmm... got you! It was not an image"

  # SUCCESS
  return "yes"


##############################
run(host="127.0.0.1", port=3333, debug=True, reloader=True)





