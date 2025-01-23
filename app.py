from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to your To-Do List App!"

if __name__ == '__main__':
    app.run(debug=True)