from flask import Flask, request, session, redirect, url_for, jsonify
import os

app = Flask(__name__)
app.secret_key = "clave123"

usuarios = {"admin": "password123", "usuario1": "abc456"}

@app.route("/")
def inicio():
    if "usuario" in session:
        return f"<h1>Bienvenido, {session['usuario']}</h1><a href='/logout'>Cerrar sesion</a><br><a href='/datos'>Ver datos sensibles</a>"
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        contrasena = request.form.get("contrasena")
        if usuario in usuarios and usuarios[usuario] == contrasena:
            session["usuario"] = usuario
            return redirect(url_for("inicio"))
        return "<h1>Credenciales incorrectas</h1><a href='/login'>Intentar de nuevo</a>"
    return """
    <h1>Inicio de sesion</h1>
    <form method='POST'>
        Usuario: <input type='text' name='usuario'><br>
        Contrasena: <input type='password' name='contrasena'><br>
        <input type='submit' value='Ingresar'>
    </form>
    """

@app.route("/datos")
def datos():
    if "usuario" not in session:
        return redirect(url_for("login"))
    return "<h1>Datos sensibles de tesoreria</h1><p>Saldo: S/ 125,000.00</p><p>Cuenta: 001-456789</p>"

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/api/transaccion", methods=["POST"])
def transaccion():
    datos = request.get_json()
    if not datos or "token" not in datos or "monto" not in datos:
        return jsonify({"error": "Solicitud invalida"}), 400
    if datos["token"] == "TOKEN_ESTATICO_123":
        return jsonify({"estado": "aprobado", "monto": datos["monto"], "mensaje": "Transaccion procesada"})
    return jsonify({"error": "Token invalido"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
