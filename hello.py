#!C:\Users\Paul\Anaconda3\python.exe
from flask import Flask
app = Flask(__name__)

@app.route("/")

def hellobis():
    import nltk
    return "Hello bis!"
    
def hellobis():
    return "hello"

if __name__ == "__main__":
    app.run()