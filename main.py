import json

from flask import Flask, make_response, request

server = Flask(__name__)

@server.route("/DevOps", methods=["POST"])
def devops():
    content = request.json
    response = make_response(
                    json.dumps({
                        "message" : "Hello {0} your message will be send".format(content['to'])
                    }),
                    200
                )
    response.headers['Content-Type'] = 'application/json'
    return response

@server.errorhandler(404)
def page_not_found(e):
    return "ERROR"

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=5000)
