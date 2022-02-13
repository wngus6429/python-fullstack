from flask import Flask

app = Flask(__name__)

def add_file(data):
    return data + 5

@app.route("/")
def hello():                           
    return "<h1>Hello World!</h1>"

@app.route("/message/<int:message_id>")
def get_message(message_id):
    return "message id: %d" % message_id   # %d 는 int, %f 는 float, %s 는 string

@app.route("/first/<int:messageid>")
def get_first(messageid):
    data = add_file(messageid)
    return "<h1>%d</h1>" % (data)


if __name__ == "__main__":              
    app.run(host="0.0.0.0", port="8080")