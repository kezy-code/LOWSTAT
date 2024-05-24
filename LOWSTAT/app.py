from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

# Codes d'accès autorisés (remplacez ceci par vos propres codes)
usern = 'karl'
passw = 'Teiwef74@2310'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']
    if username == usern and password == passw:
        response = make_response(redirect(url_for('index')))
        # Stocker le nom d'utilisateur dans un cookie pour indiquer l'authentification réussie
        response.set_cookie('username', username)
        return response
    else:
        return render_template('login.html', message='Identifiants incorrects')

@app.route('/index')
def index():
    # Vérifier si le cookie contenant le nom d'utilisateur existe
    username = request.cookies.get('username')
    if username:
        return render_template('index.html', username=username)
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
