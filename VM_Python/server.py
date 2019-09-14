import random
from flask import Flask
app = Flask(__name__)

@app.route('/')

def index():
    rn = random.randint(1,1000000)
    return str(rn)

if __name__ == "__main__":
    app.run(host = '0.0.0.0',port=80)
