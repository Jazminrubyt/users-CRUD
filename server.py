from flask import Flask, render_template, request, redirect
from user import Users

app = Flask(__name__)


@app.route("/")
@app.route("/users")
def index():
    """This route displays all users"""
    users = Users.retrieve_info()
    return render_template("index.html", users=users)


@app.get("/users/new")
def new_user():
    """This route displays new user"""
    return render_template("new_users.html")


@app.get("/users/<int:user_id>")
def user_details(user_id):
    """This route displays a users info"""

    user = Users.retrieve_info_id(user_id)
    if user == None:
        return "No user information found"
    return render_template("user_details.html", user=user)


@app.post("/users/create")
def create_user():
    """The route that processes the form"""

    print(request.form)
    user_id = Users.create(request.form)
    print("New User:" + str(user_id))
    return redirect("/users")


@app.get("/users/<int:user_id>/edit")
def edit_user(user_id):
    """This route displays edit form"""

    user = Users.retrieve_info_id(user_id)
    if user == None:
        return "No user information found"
    return render_template("edit_user.html", user=user)


@app.post("/users/update")
def update_user():
    """This route processes the Edit form"""

    user_id = request.form["user_id"]
    Users.update(request.form)
    return redirect(f"/users/{user_id}")


@app.post("/users/<int:user_id>/delete")
def delete_user(user_id):
    """Deletes a pet"""

    Users.delete_by_id(user_id)
    return redirect("/users/")


if __name__ == "__main__":
    app.run(debug=True)
