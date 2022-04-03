from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html')


if __name__ == '__main__':
   app.run(host='0.0.0.0',port=80, debug=True)
