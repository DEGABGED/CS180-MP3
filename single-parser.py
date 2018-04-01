import os, sys, email

msg = email.message_from_string(open(os.path.join(os.getcwd(), sys.argv[1]), encoding='utf-8', errors='replace').read())

payload = ""
if msg.is_multipart():
  # traverse the tree preorder
  # my existence is a joke
  for part in msg.walk():
    print(str(part.get_content_maintype()))
else:
  payload = (msg.get_payload())
  print(payload)

"""

    stack = msg.get_payload()[::-1]
    while stack:
      msg = stack.pop()
      if isinstance(msg, email.message.Message):
        msg = (msg.get_payload())

      if isinstance(msg, (list,)):
        stack += msg
      else:
        payload += str(msg)
        """
