from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
     return "<h1>Hola Flask!<h1>"

@app.route("/about")
def about():
	return "Esto es una aplicacion de flask"

@app.route("/plantilla", methods=["GET", "POST"])
def plantilla():
	if request.method == "POST":
		nombre = request.form["firstname"]
		apellido = request.form["lastname"]
		return render_template("hola2.html", name=nombre, surname=apellido)
	return render_template("holamundo.html")

@app.route("/plantilla2/<name>")
def usando_plantilla2(name):
	lista = ["Arbol", "casa", "Pepe", "amigo"]
	return render_template("hola_base.html", nombre=name, cosas=lista)


if __name__ == '__main__':
    app.run(debug=True)

    
    
    
    
    
    
    
   
