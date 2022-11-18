

from flask import Flask, request,render_template
from app_data.utils import IrisPrediction

app = Flask(__name__)



@app.route('/')
def new():
    print('hello')
    return render_template('user.html')

@app.route('/submit',methods =['POST'])
def submit():
    data= request.form
    SepalLengthCm = float(data['SepalLengthCm'])
    SepalWidthCm = float(data['SepalWidthCm'])
    PetalLengthCm = float(data['PetalLengthCm'])
    PetalWidthCm = float(data['PetalWidthCm'])

    iris = IrisPrediction(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)
    S=iris.predict()

    return '''<html>
    <head></head>
    <center>
    <body style="background-color:rgb(204, 128, 141);">
    <p style="font-size:50px ; ">
    
        <label>Species: %(S)s </label>
        <br>            
    </body>
    </center>
</html>
''' % locals()

if __name__ == '__main__':
    app.run(debug=True,port=8080)