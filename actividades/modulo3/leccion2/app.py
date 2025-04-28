from flask import Flask, request, redirect, url_for, session, render_template
from flask_principal import Principal, Permission, RoleNeed, Identity, identity_changed, identity_loaded, AnonymousIdentity

app = Flask(__name__)
app.secret_key = 'secreto123'  # Para manejar sesiones

# Inicializar Principal
Principal(app)

# Definimos permisos
admin_permission = Permission(RoleNeed('admin'))
editor_permission = Permission(RoleNeed('editor'))
user_permission = Permission(RoleNeed('user'))

# Simular usuarios (nombre: rol)
usuarios = {
    "admin": "admin",
    "editor": "editor",
    "usuario": "user"
}

# Home
@app.route('/')
def index():
    return render_template('index.html')

# Login
@app.route('/login/<username>')
def login(username):
    if username in usuarios:
        session['user'] = username
        identity_changed.send(app, identity=Identity(username))
        return f'Logueado como {username} ({usuarios[username]})'
    return 'Usuario no encontrado', 404

# Logout
@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    identity_changed.send(app, identity=AnonymousIdentity())
    return redirect(url_for('index'))

# Protegido para Admin
@app.route('/admin')
@admin_permission.require(http_exception=403)
def admin_area():
    return 'Área de Administración: Solo Admins'

# Protegido para Editor
@app.route('/editor')
@editor_permission.require(http_exception=403)
def editor_area():
    return 'Área de Edición: Solo Editores'

# Protegido para Usuarios normales
@app.route('/user')
@user_permission.require(http_exception=403)
def user_area():
    return 'Área de Usuario: Solo Usuarios Registrados'

# Manejar identidad cargada
@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    username = identity.id
    if username and username in usuarios:
        role = usuarios[username]
        identity.provides.add(RoleNeed(role))

# Error 403
@app.errorhandler(403)
def acceso_denegado(e):
    return 'Acceso denegado: No tienes permisos.', 403

if __name__ == '__main__':
    app.run(debug=True)