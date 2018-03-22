from flask import Flask,request
from Handler.CardHandlerFactory import *

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['uploadfile']
	name = request.form['name']
	sex = request.form['sex']
	colleges = request.form['colleges']
	degree = request.form['degree']
	id_number = request.form['id_number']
        school = request.form['school']
	date = request.form['date']
	handler = getCardHandler(school)
	return handler.handleData(name,sex,colleges,degree,id_number,date, f)

if __name__ == '__main__':
    app.run()
