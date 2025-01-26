from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "Welcome to the API"}, 200

@app.route('/heart')
def heart():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    app.run(debug=True)
