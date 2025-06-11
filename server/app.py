from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

@app.route('/request-demo')
def request_demo():
    user_agent = request.headers.get('User-Agent')  
    method = request.method  
    return f"""
        <h1>Request Info</h1>
        <p><strong>HTTP Method:</strong> {method}</p>
        <p><strong>User Agent:</strong> {user_agent}</p>
    """

if __name__ == '__main__':
    app.run(port=5555, debug=True)