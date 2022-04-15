from flask_app import app
from flask import render_template, redirect,request, session
from flask_app.models.models_user import User




@app.route("/")
def index():
    users = User.get_all()
    return render_template("index.html", users = users)

@app.route("/user")
def enter_info():
    return render_template("create.html")

@app.route('/user/create', methods=["POST"])
def create_new_user():
    User.create(request.form)
    return redirect('/')

@app.route('/user/<int:id>/show')
def show(id):
    data ={
        "id":id
    }
    return render_template("show.html", user =User.get_one(data))

@app.route('/user/<int:id>/edit')
def edit(id):
    data={
        "id":id
    }
    return render_template("edit.html", user=User.get_one(data))

@app.route('/user/<int:id>/update', methods =["POST"])
def update(id):
    # user_data={
    #     "first_name":request.form["first_name"],
    #     "last_name":request.form["last_name"],
    #     "email":request.form["email"],
    #     "id":id
    # }
    user_data={
        **request.form, 
        "id":id
    }
    User.update(user_data)
    return redirect(f'/user/{id}/show')

@app.route('/user/<int:id>/delete')
def delete(id):
    User.delete({'id': id})
    return redirect('/')