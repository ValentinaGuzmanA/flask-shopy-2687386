from flask_wtf import  FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Email


class ClientForm():
    username = StringField("Ingrese su usuario",
                            validators=[InputRequired(
                                message="username"
                            )])
    password = StringField("Ingrese su contraseña",
                            validators=[InputRequired(
                                message="password"
                            )])
    email = StringField("Ingrese su email",
                            validators=[InputRequired(
                                message="email"
                        ),
                                        ])
    
class NewClientForm(FlaskForm,ClientForm):
    submit = SubmitField("Guardar")

class EditClientForm(FlaskForm,ClientForm):
    submit = SubmitField("Actualizar")