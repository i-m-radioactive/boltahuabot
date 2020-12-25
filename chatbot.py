#api
import flask
import os
from flask import request
from flask import render_template
from flask import send_file, send_from_directory


app = flask.Flask(__name__, static_folder='./build/', static_url_path='/')
app.config["DEBUG"] = True
app.config["bot_files"] = "./"


@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

@app.route('/api', methods=['GET'])
def chat_reply():
    parameter = request.args
    print(parameter['user_req'])
    bot_response = chatbot_response(parameter['user_req'])
    if bot_response == "time" :
        return date.today().strftime("%d %b %Y - %A ")
    elif bot_response == "ecsyll.pdf" :
        return send_from_directory(app.config["bot_files"],filename=bot_response, as_attachment=True)
        
    
    return bot_response

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))