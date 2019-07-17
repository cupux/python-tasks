from flask import Flask

app = Flask(__name__)

def index():
    return 'hello world'

if __name__ == '__main__':
    app.run(debug=True, host = '127.0.0.1')
    

@app.route('/whereami')
def whereami():
    return 'Ghana:'