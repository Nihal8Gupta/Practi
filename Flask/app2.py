from flask import Flask,render_template

FAI = Flask(__name__)

@FAI.route('/')
def home():
    return render_template('home.html')

@FAI.route('/form')
def std():
    return render_template('studentreg.html')

if __name__=='__main__':
    FAI.run(debug=True)