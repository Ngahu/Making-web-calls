from flask import Flask
import twilio.twiml

app = Flask(__name__)

#adding of your numbers to the list!!
caller = "+254704104008"


@app.route("/", methods= ['GET', 'POST'])
def hello_monkey():
    """responds to the incoming requests."""
    resp = twilio.twiml.Response()
    resp.say("Hello monkey")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)