from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

app = Flask(__name__)

app.config["SECRET_KEY"] = "1234"
    
class RegisterForm(FlaskForm):
    nombre = StringField("Nombre",
validators=[DataRequired(), Length(min=3)])
    
    correo = StringField('Correo Electrónico', 
validators=[DataRequired(), Email(message="Correo Electrónico invalido")])

    password = PasswordField("Contraseña",
validators=[DataRequired(), Length(min=6)])
    
    submit = SubmitField("Registrar")
    
@app.route("/registro", methods=["GET", "POST"])
def registro():
    form = RegisterForm()
    if form.validate_on_submit():
        return f"Nombre: {form.nombre.data}, Correo: {form.correo.data}, Contraseña: {form.password.data}"
    return render_template("registro.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)