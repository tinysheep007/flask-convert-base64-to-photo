from flask import Flask
from flask import request
from datetime import datetime
import base64
import re

app = Flask(__name__)

@app.route('/test')
def test():
    return "hello Ending recevied"

@app.route('/picToBase64',methods=['POST'])
def picToBase64():
    data = request.data.decode("utf-8") 
    splitData = data.split("\",\"")
    # index 0 - pic1base64
    # index 1 - pic1ID
    # index 2 - pic2base64
    # index 3 - pic2ID
    pic1base64 = splitData[0].replace("{\"pic1base64\":\"","")
    pic1ID = splitData[1].replace("pic1ID\":\"","")
    pic2base64 = splitData[2].replace("pic2base64\":\"","")
    pic2ID = splitData[3].replace("pic2ID\":\"","").replace("\"}","")

    # print(splitData)
    # print(result)
    
    # convert base64 to img 
    r = base64.b64decode((pic1base64))
    image = open("pic1.jpg","wb")
    image.write(r)
    image.close()

    r = base64.b64decode((pic2base64))
    image = open("pic2.jpg","wb")
    image.write(r)
    image.close()
    return "image receiving"

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content


if __name__ == "__main__":
    app.run(debug=True)
