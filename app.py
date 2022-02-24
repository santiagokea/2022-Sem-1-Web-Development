from bottle import get, post, request, response, run
import os
import uuid
import imghdr
from password import gmail_password

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

##############################
@get("/send-email")
def _():
  sender_email = "2022webemail@gmail.com"
  receiver_email = "2022webemail@gmail.com"
  password = gmail_password

  message = MIMEMultipart("alternative")
  message["Subject"] = "My Company"
  message["From"] = sender_email
  message["To"] = receiver_email

  # Create the plain-text and HTML version of your message
  text = """\
  Hi,
  Thank you.
  """

  html = """\
  <html>
    <body>
      <p>
        Hi,<br>
        <b style="color: blue;">How are you?</b><br>
      </p>
    </body>
  </html>
  """

  # Turn these into plain/html MIMEText objects
  part1 = MIMEText(text, "plain")
  part2 = MIMEText(html, "html")

  # Add HTML/plain-text parts to MIMEMultipart message
  # The email client will try to render the last part first
  message.attach(part1)
  message.attach(part2)

  # Create secure connection with server and send email
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    try:
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message.as_string())
      return "yes, email sent"
    except Exception as ex:
      print("ex")
      return "uppps... could not send the email"






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
  if file_extension not in (".png", ".jpeg", ".jpg"):
    return "image not allowed"
  
  # overwrite jpg to jpeg so imghdr will pass validation
  if file_extension == ".jpg": file_extension = ".jpeg"

  image_id = str(uuid.uuid4())
  # Create new image name
  image_name = f"{image_id}{file_extension}"
  print(image_name)
  # Save the image
  image.save(f"images/{image_name}")

  # Make sure that the image is actually a valid image
  # by reading its mime type
  print("imghdr.what", imghdr.what(f"images/{image_name}"))   # imghdr.what png
  print("file_extension", file_extension)                     # file_extension .png
  imghdr_extension = imghdr.what(f"images/{image_name}")
  if file_extension != f".{imghdr_extension}":
    print("mmm... suspicious ... it is not really an image")
    # remove the invalid image from the folder
    os.remove(f"images/{image_name}")
    return "mmm... got you! It was not an image"

  # SUCCESS
  return "yes"


##############################
run(host="127.0.0.1", port=3333, debug=True, reloader=True)





