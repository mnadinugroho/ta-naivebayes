from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def  data():

    return render_template('frontend.html')

@app.route('/', methods=['GET', 'POST'])
def post(datat):
    data = request.data()
    print(data)
    return render_template('frontend.html', data=data)