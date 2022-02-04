from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user_model import User
from flask_app.models.word_model import Word
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/register', methods=['POST'])
def register():
    if not User.validate_register(request.form):
        return redirect('/')
    data = {  
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id

    return redirect('/displayword/food/1')

@app.route('/login')
def login_page():
    return render_template("login.html")

@app.route('/login/validate', methods=['POST'])
def login_validate():
    results = User.validate_login(request.form)
    if not results:
        return redirect('/login')

    session['user_id'] = results.id
    return redirect('/displayword/food/1')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    return render_template("dashboard.html", log_user=User.get_by_id(data))
    # , word=Word.get_word(word_data), pagenum=pagenum

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

