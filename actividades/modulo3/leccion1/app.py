from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = '987ghrtwyi154gdh26fj3fg46'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

usuarios = {
    'admin': {
        'password': generate_password_hash('admin123'),
        'rol': 'admin'
    },
    'user': {
        'password': generate_password_hash('user123'),
        'rol': 'user'
    }
}

class Usuario(UserMixin):
    def __init__(self, username):
        self.id = username
        self.rol = usuarios[username]['rol']

@login_manager.user_loader
def load_user(user_id):
    if user_id in usuarios:
        return Usuario(user_id)
    return None

@app.route('/')
def index():
    return 'Inicio público. <a href="/login">Login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = usuarios.get(username)
        if user and check_password_hash(user['password'], password):
            usuario = Usuario(username)
            login_user(usuario)
            flash('Inicio de sesión exitoso.')
            return redirect(url_for('dashboard'))
        else:
            flash('Nombre de usuario o contraseña incorrectos.')

    return '''
        <form method="post">
            Usuario: <input type="text" name="username"><br>
            Contraseña: <input type="password" name="password"><br>
            <input type="submit" value="Iniciar Sesión">
        </form>
    '''

@app.route('/dashboard')
@login_required
def dashboard():
    return f'Hola {current_user.id}! Rol: {current_user.rol}. <a href="/logout">Cerrar Sesión</a>'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
