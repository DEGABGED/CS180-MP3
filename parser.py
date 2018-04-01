import os
import sys
import email

#msg = email.message_from_string(open("sample/inmail.65062").read())
#payload = msg.get_payload()

sample_dir = os.path.join(os.getcwd(), "sample")
pp1_dir = os.path.join(os.getcwd(), "pp1")
for f in os.listdir(sample_dir):
  msg = email.message_from_string(open(os.path.join(sample_dir, f), encoding='utf-8', errors='replace').read())

  # Open file for writing
  fo = open(os.path.join(pp1_dir, f), "w")

  # Get the payload
  payload = ""
  if msg.is_multipart():
    for part in msg.walk():
      # Filter out certain types of content (images, etc)
      if part.get_content_maintype() in ["text", "message"]:
        payload += part.get_payload()
  else:
    payload = (msg.get_payload())

  fo.write(str(payload))
  fo.close()
