# import socket

# s = socket.create_connection(("10.167.217.10", 796))
# s.send(b"""HI""")

# while True:
#     b = s.recv(4096)
#     if len(b) > 0:
#         print(b)

import flask
app = flask.Flask('hi')

@app.route("/")
def home():
    return "https://github.com/sqz269/AntiLanSchool"

app.run("0.0.0.0", 8080)