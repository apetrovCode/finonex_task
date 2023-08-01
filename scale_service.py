from flask import Flask
import time

app = Flask(__name__)

@app.route('/start')
def start_load():
    while True:
        fibonacci(30)  # Adjust number as needed to increase/decrease load
    return "Started intensive task"

@app.route('/health')
def health_check():
    return "Healthy", 200

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

