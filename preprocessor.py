import os
import sys
import email
import re

# Define population and sample sizes
n = 75419
training = 0.6 * n

# Define directories
#dest_dir = os.path.join(os.getcwd(), "mp3data", "preprocessed")
#src_dir = os.path.join(os.getcwd(), "trec07p", "data")

# Precompilation of regexes
pp_html = re.compile('<[^>]+?>')
pp_spaces = re.compile('(\s)\s+')
pp_nonword = re.compile('[^a-zA-Z0-9]+')

def payload_preprocess(part):
    raw_payload = part.get_payload()

    # Preprocess if HTML
    if part.get_content_subtype() == "html":
        raw_payload = re.sub(pp_html, '', raw_payload)

    # Remove nonwords
    raw_payload = re.sub(pp_nonword, ' ', raw_payload)

    # Remove extra spaces
    raw_payload = re.sub(pp_spaces, r'\1', raw_payload)

    return raw_payload

# Takes in an email object, returns a string containing the parsed email
def parse_email(msg):
    # Get the email header
    payload = ""
    if msg['Subject']:
        payload = msg['Subject']

    # MIME parsing
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_maintype() in ["text", "message"] and not part.is_multipart():
                payload += payload_preprocess(part)
    else:
        payload += payload_preprocess(msg)

    return payload


def preprocess(src_dir, dest_dir):
    # For each of the files:
    ctr = 0
    filename = ""
    try:
        for f in range(n):
            filename = "inmail.{}".format(f+1)
            msg = email.message_from_string(open(os.path.join(src_dir, filename), encoding='utf-8', errors='replace').read())

            # Open file for writing
            fo = open(os.path.join(dest_dir, filename), "w")

            # Get the payload
            payload = parse_email(msg)

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
        raise e

    print('')
