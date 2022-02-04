from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user_model import User
from flask_app.models.word_model import Word




@app.route('/displayword/<category>/<int:pagenum>')
def display_word(category, pagenum):
    word_data = {
        "category": category,
        "pagenum": pagenum - 1
    }
    word = Word.get_word(word_data)
    if not word:
        return redirect("/dashboard")
    return render_template("dashboard.html", word=word, pagenum=pagenum)



# @app.route('/create/band', methods=['POST'])
# def create_band():
#     if 'user_id' not in session:
#         return redirect('/logout')
#     if not Band.validate_band(request.form):
#         return redirect('/new/band')
#     print(request.form)
#     data = {
#         "name": request.form["name"],
#         "home_city": request.form["home_city"],
#         "music_genre": request.form["music_genre"],
#         "user_id": session["user_id"]
#     }
#     Band.save(data)
#     return redirect('/dashboard')

# @app.route('/edit/band/<int:id>')
# def edit_band(id):
#     if 'user_id' not in session:
#         return redirect('/logout')
#     data = {
#         "id":id
#     }
#     user_data = {
#         "id":session['user_id']
#     }
#     return render_template("edit_band.html", edit=Band.get_one(data), user=User.get_by_id(user_data))

# @app.route('/update/band',methods=['POST'])
# def update_band():
#     if 'user_id' not in session:
#         return redirect('/logout')
#     if not Band.validate_band(request.form):
#         return redirect('/new/band')
#     data = {
#         "id": request.form["id"],
#         "name": request.form["name"],
#         "home_city": request.form["home_city"],
#         "music_genre": request.form["music_genre"],
#         "user_id": session["user_id"]
#     }
#     Band.update(data)
#     return redirect('/dashboard')

# @app.route('/band/<int:id>')
# def show_my_bands(id):
#     if 'user_id' not in session:
#         return redirect('/logout')
#     data = {
#         "id":id
#     }
#     user_data = {
#         "id":session['user_id']
#     }
#     return render_template("display_bands.html", bands=Band.get_my_bands(data), user=User.get_by_id(user_data))

# @app.route('/destroy/band/<int:id>')
# def destroy_band(id):
#     if 'user_id' not in session:
#         return redirect('/logout')
#     data = {
#         "id":id
#     }
#     Band.destroy(data)
#     return redirect('/dashboard')