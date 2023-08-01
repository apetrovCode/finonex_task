from flask import Flask
import random

app = Flask(__name__)

names = ["Alice", "Bob", "Charlie", "David", "Eve"]

@app.route('/')
def get_random_name():
    return random.choice(names)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

