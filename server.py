from flask import Flask, request

from flask import Flask, request
import requests

app = Flask(__name__)

ACCESS_TOKEN = "EAASNmaBFTkMBAIlZCeW8VXDL2n78sjFvd0OZCayzJx2m2kZARJ2MnSZBhjJbDdxC8PZBxPHOlwCAvwBgFspvSp5vuXlNEUbJGqffp5jM6oZA7PQhsYosiCOFFQ8K4lWCwRMrLQ4m94wrqID4Ig7ZCZBnMUJ3GVkkHUZCVlPEA3ZAch7QZDZD"


def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)


@app.route('/', methods=['POST'])
def handle_incoming_messages():
    data = request.json
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']
    reply(sender, message[::-1])

    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
