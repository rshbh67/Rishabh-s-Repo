
import pywhatkit as kit

# Specify the phone number (with country code) and the message
phone_number = "+918579878939"
message = "Hello from Python! This is an instant WhatsApp message."

# Send the message instantly
kit.sendwhatmsg_instantly(phone_number, message)