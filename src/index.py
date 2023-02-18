from flask import Flask, render_template, request
from operations import infixToPostfix
from operations import infixToPrefix

'''
Se crea la instancia de la clase Flask, que como primer argumento contiene el nombre del módulo principal, que en este caso es index.py
Como segundo argumento recibe el directorio donde se encuetran los archivos estáticos.
'''
app = Flask(__name__, static_url_path = '/static')

'''
Utilizando el decorador route(), nos permite decirle al programa que cuando el usuario visite nuestra pagina en cierta ruta, ejecute la funcion landing()
Se definen las operaciones que nuestra pagina va a realizar, en este caso usaremos POST
'''
@app.route('/', methods=['GET', 'POST']) 
def landing():
	#Si recibe una solicitud del formulario, primero evalua si proviene de los botones mediante 'action' y de igual forma de que boton proviene mediante 'value' en el html
	if request.method == 'POST':
		#Si el bóton es postfija
		if request.form['action'] == 'pos':
			#Obtiene y asigna a una variable el valor de entrada
			entry = request.form['expression']
			#Procesa el resultado y lo asigna
			resultado = infixToPostfix(entry)
			#Carga la página de inicio sustituyendo en el html los espacios reservados para la entrada original, el tipo de conversion y el resultado final
			return render_template('landing.html', original = entry , conversion = "postfija",resultado = resultado)
		#Si el boton es prefija
		elif request.form['action'] == 'pre':
			#Obtiene y asigna a una variable el valor de entrada
			entry = request.form['expression']
			#Procesa el resultado y lo asigna
			resultado = infixToPrefix(entry)
			#Carga la página de inicio sustituyendo en el html los espacios reservados para la entrada original, el tipo de conversion y el resultado final
			return render_template('landing.html', original = entry , conversion = "prefija", resultado = resultado)
			
	return render_template('landing.html')

@app.route('/Manual')
def manual():
	return render_template('manual.html')


#Si se esta ejecutando el modulo principal, ejecuta la aplicación.
if __name__ == '__main__':
	app.run(debug=False)