import functools
import uuid
import datetime
from flask import (Blueprint, 
                   render_template, 
                   session, 
                   redirect, 
                   request, 
                   current_app, 
                   url_for, 
                   abort,
                   flash)

from movie_library.forms import (MovieForm, 
                                 ExtendedMovieForm, 
                                 RegisterForm, 
                                 LoginForm)

from dataclasses import asdict
from movie_library.models import Movie, Users
from passlib.hash import pbkdf2_sha256

pages = Blueprint("pages",__name__, template_folder="templates", static_folder="static")

#This login_required decorator can be used with any endpoint as a security measure that checks if the user is logged in, before granting access to the said endpoint
#If the user isn't logged in, it'll redirect user to the login page; otherwise it'll run the original function of the endpoint as usual
def login_required(route):
    @functools.wraps(route)
    def route_wrapper(*args,**kwargs):
        if session.get("email") is None:
            return redirect(url_for(".login"))
        return route(*args, **kwargs)
    return route_wrapper


@pages.route("/")
@login_required
def index():

    #Fetches the database info of currently logged-in user
    user_data = current_app.db.user.find_one({"email":session["email"]})
    user = Users(**user_data)
    #Makes sure that only the movies added by logged-in user are displayed
    movie_data = current_app.db.movie.find({"_id": {"$in":user.movies}})
    movies = [Movie(**movie) for movie in movie_data]
    return render_template("index.html", 
                           title="Movies Watchlist",
                           movies_data = movies)

@pages.route("/add", methods = ["GET","POST"])
@login_required
def add_movie():
    form = MovieForm()

    #Checks if the wtform has been submitted successfully or not
    if form.validate_on_submit():

        #We're using the movie class instead of dictionary so that we can also insert data with default values into the database
        movie = Movie(
            _id= uuid.uuid4().hex,
            title= form.title.data,
            director= form.director.data,
            year= form.year.data,
            )
        
        #We use 'asdict' to convert the "movie" object into a dictionary before inserting it into the database
        current_app.db.movie.insert_one(asdict(movie))
        current_app.db.user.update_one({"_id":session["user_id"]}, {"$push": {"movies":movie._id}})

        return redirect(url_for(".index"))

    return render_template("new_movie.html",title ="Movie Watchlist- Add movie", form = form)

@pages.route("/edit/<string:_id>/", methods = ["GET","POST"])  
@login_required
def edit_movie(_id:str):
    movie = Movie(**current_app.db.movie.find_one({"_id":_id}))

    #Populating the "ExtendedMovieForm() class with fields from "MovieForm" class"
    form = ExtendedMovieForm(obj=movie)

    if form.validate_on_submit():
        movie.title = form.title.data
        movie.director = form.director.data
        movie.year = form.year.data
        movie.cast = form.cast.data
        movie.series = form.series.data
        movie.tags = form.tags.data
        movie.description = form.description.data
        movie.video_link = form.video_link.data

        current_app.db.movie.update_one({"_id":movie._id},{"$set":asdict(movie)})

        return redirect(url_for(".movie",_id = movie._id))
    
    return render_template("movie_form.html", movie = movie, form = form)

@pages.get("/movie/<string:_id>")
def movie(_id: str):
    movie_data = current_app.db.movie.find_one({"_id": _id})
    if not movie_data:
        abort(404)
    movie = Movie(**movie_data)

    return render_template("movie_details.html", movie = movie)

@pages.get("/movie/<string:_id>/rate")
@login_required
def rate_movie(_id):
    rating = int(request.args.get("rating"))
    current_app.db.movie.update_one({"_id":_id}, {"$set":{"rating":rating}})

    return redirect(url_for(".movie", _id = _id))

@pages.get("/movie/<string:_id>/watch")
@login_required
def watch_today(_id):
    current_app.db.movie.update_one({"_id":_id}, {"$set":{"last_watched": datetime.datetime.today()}})

    return redirect(url_for(".movie", _id = _id))



@pages.get("/toggle-theme")
def toggle_theme():
    current_theme = session.get('theme')

    if current_theme == "dark":

        #We're setting the theme in session as light here so that the next time the user clicks on the "dark-mode" button, it'll switch back to light mode by changing the class name in 'layout.html'
        session['theme'] = "light"

    else:
        session['theme'] = "dark"

    #Returns the current page the user is on, so that the theme change is reflected in the same page
    return redirect(request.args.get("current_page"))

@pages.route("/register", methods = ["GET","POST"])
def register():

    #If the user is already logged in with the email they're using to register to the website
    if session.get("email"):
        return redirect(url_for(".index"))
    
    form = RegisterForm()

    if form.validate_on_submit():
        user = Users(
            _id = uuid.uuid4().hex,
            email= form.email.data,
            password= pbkdf2_sha256.hash(form.password.data),
        )

        current_app.db.user.insert_one(asdict(user))
        flash("User successfully registered", category="success")

        return redirect(url_for(".login"))

    return render_template("Register.html", title = "Movie Watchlist - Register User", form = form)

@pages.route("/login", methods = ["GET", "POST"])
def login():
    if session.get("email"):
        return redirect(url_for(".index"))
    
    form = LoginForm()

    if form.validate_on_submit():
        user_data = current_app.db.user.find_one({"email":form.email.data})

        if not user_data:
            flash("Incorrect login credentials!", category="danger")
            return redirect(url_for(".login"))
        
        user = Users(**user_data)

        if user and pbkdf2_sha256.verify(form.password.data,user.password):
            session["email"] = user.email
            session["user_id"] = user._id
            return redirect(url_for(".index"))
        
        flash("Incorrect login credentials!", category="danger")
    
    return render_template("Login.html",title = "Movie Watchlist - Login", form = form)

@pages.route("/logout")
def logout():

    #Preserves the current theme when the user was logged-in; otherwise the theme will default to light-mode after logout
    current_theme= session.get("theme")
    session.clear()
    session["theme"] = current_theme

    return redirect(url_for(".login"))