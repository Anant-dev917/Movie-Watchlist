from typing import Any
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, TextAreaField, URLField, PasswordField
from wtforms.validators import InputRequired, NumberRange, Email, EqualTo, Length

class MovieForm(FlaskForm):

    #The "Name" is the label for the name field and validators are a list of requirements that must be fulfilled in case of each inputs
    title = StringField("Title",validators=[InputRequired()])
    year = IntegerField("Year",validators=[InputRequired(),NumberRange(min=1878, message="Please enter a valid date")])
    director = StringField("Director", validators=[InputRequired()])
    submit = SubmitField("Add Movie")

class StringListField(TextAreaField):

    def _value(self):
        if self.data:

            #Joins all the list element into a string, with "\n" (newline) as the separator
            return "\n".join(self.data)
        
        else:
            return ""


    def process_formdata(self, valuelist):

        #Checking if the valuelist exist and that it has data, i.e the textarea is empty or not
        if valuelist and valuelist[0]:

            #strip() removes any leading or trailing whitespaces from the textarea content; split() separates each line of the textarea into a list element
            #Overall, this line converts each line of the textarea into individual list elements and stores them as a list 
            self.data = [line.strip() for line in valuelist[0].split("\n")]

        else:
            self.data = []

class ExtendedMovieForm(MovieForm):

    cast = StringListField("Cast")
    series = StringListField("Series")
    tags = StringListField("Tags")
    description = TextAreaField("Description")
    video_link = URLField("Video Link")
    submit = SubmitField("Submit")

class RegisterForm(FlaskForm):

    #Email() validator checks if the email is properly formatted (in the form "abc@gmail.com")
    email = StringField("Email", validators=[InputRequired(), Email()])

    password = PasswordField("Password", 
                             validators=[InputRequired(),
                                         Length(
                                             min=4,
                                             message="Password must be at least 4 characters long"
                                               ), 
                                        ],
                            )
    
    confirm_password = PasswordField("Repeat Password", 
                                    validators=[InputRequired(),
                                     EqualTo("password",
                                             message="Passwords do not match"
                                             ),
                                        ],
                                    )

    submit = SubmitField("Register")

class LoginForm(FlaskForm):

    email = StringField("Email", validators=[InputRequired(), Email()])

    password = PasswordField("Password", validators=[InputRequired()])

    submit = SubmitField("Login")