import os
import sys
import email
import re

#msg = email.message_from_string(open("sample/inmail.65062").read())
#payload = msg.get_payload()
n = 1000

# Precompilation of regexes
pp_html = re.compile('<[^>]+?>')
pp_spaces = re.compile('(\s)\s+')

def payload_preprocess(part):
    raw_payload = part.get_payload()

    # Preprocess if HTML
    if part.get_content_subtype() == "html":
        raw_payload = re.sub(pp_html, '', raw_payload)

    # Special rules that I'm too lazy to properly implement
    # Replace '=' with ' '
    raw_payload = re.sub('=', ' ', raw_payload)

    # Remove extra spaces
    raw_payload = re.sub(pp_spaces, r'\1', raw_payload)

    return raw_payload

# Define directories
sample_dir = os.path.join(os.getcwd(), "isolate")
pp1_dir = os.path.join(os.getcwd(), "pp1")

# For each of the files:
ctr = 0
filename = ""
try:
    for f in os.listdir(sample_dir):
        filename = f # For debugging
        msg = email.message_from_string(open(os.path.join(sample_dir, f), encoding='utf-8', errors='replace').read())

        # Open file for writing
        fo = open(os.path.join(pp1_dir, f), "w")

        # Get the email header
        payload = "Subject: {}".format(msg['Subject'])

        # MIME Parsing
        if msg.is_multipart():
            for part in msg.walk():
                # Filter out certain types of content (images, etc)
                # Update the whitelist sometimes
                print(part)
                print("===")
                if part.get_content_maintype() in ["text", "message"]:
                    payload += payload_preprocess(part)
        else:
            payload = payload_preprocess(msg)

        # Write payload and close file
        fo.write(str(payload))
        fo.write('\n')
        fo.close()

        # Print how many have been preprocessed so far
        ctr += 1
        sys.stdout.write("\r{}/{}".format(ctr, n))
        sys.stdout.flush()
except:
    e = sys.exc_info()[0]
    print("\nError at {}: {}".format(filename, str(e)))

print('')
