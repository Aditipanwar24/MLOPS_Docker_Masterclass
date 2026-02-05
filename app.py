from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return '''
           <html>
           <body>
           <h1>Welcome to the Flask App!</h1>
           <p>Click the button below to go to the next page.</p>
           </body>
           </html>
        '''

@app.route('/greet', methods=['POST'])
def greet():
    user_input = request.form['username']
    return f"Hello, {user_input}, Welcome to this app for Docker demonstration."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)
    