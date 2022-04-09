from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/python')
def python():
    return render_template('indexp.html')       

@app.route('/generic')
def generic():
    return render_template('genericp.html')              

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html')

if __name__ == '__main__':
    app.run(host='222.101.33.71',port=80, debug=True)