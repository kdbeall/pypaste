from flask import Flask
app = Flask(__name__)

@app.route('/<string:paste_id>', methods=['GET'])
def get_paste(paste_id):
    pass

@app.route('/', methods=['GET'])
def home_page():
    pass

@app.route('/', methods=['POST'])
def post_paste(paste_txt):
    pass