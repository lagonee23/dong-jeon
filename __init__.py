from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<int:status>.html/')
def status(status):
    if status in (401, 404, 500):
        return render_template(f'{status}.html')
    
@app.route('/twitter.html/')
def twitter():
    return render_template('twitter.html')


if __name__ == '__main__':
    app.run(debug=True)