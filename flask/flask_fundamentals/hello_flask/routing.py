from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def triple(name):
    # print(name)
    return f"Hi {name.upper()}!"

@app.route('/repeat/<id>/<name>')
def multiple(id,name):
    str = ''
    # print(int(id))
    # print(name)
    for i in range(int(id)):
        str=str + f"|| HI {name.upper()} "
    return str+" ||"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)