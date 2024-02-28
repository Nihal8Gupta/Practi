from flask import Flask

FAI = Flask(__name__)

@FAI.route('/home')
def home():
    return '<h1>Welecome Home</h1>'

if __name__=='__main__':
    FAI.run(debug=True)