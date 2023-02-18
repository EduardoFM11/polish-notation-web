#Clase que nos permite crear una pila para las operaciones.
class Stack:
    #Función de inicialización del objeto.
    def __init__(self):
        self.items = []

    #Función que verifica si la pila está vacía.
    def isEmpty(self):
        return self.items == []

    #Función para insertar elementos en la pila.
    def push(self, item):
        self.items.insert(0,item)

    #Función para eliminar elementos en la pila.
    def pop(self):
        return self.items.pop(0)

    #Función que nos regresa el primer elemento de la pila.
    def peek(self):
        return self.items[0]

    #Función que da el tamaño de la pila.
    def size(self):
        return len(self.items)

#Función que nos permitirá pasar de notación infija a notación posfija.
def infixToPostfix(string):
    infixexpr = string.upper() 
    prec = {}
    '''
    Se le da una ponderación a los operandos ya que unos tienen mayor precedencia que otros y 
    esto nos será útil al momento de querer pasar de una notación a otra.
    '''
    prec["¬"] = 4
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    #Se crea una pila vacía
    opStack = Stack()
    #se crea una pila que servirá para guardar el resultado final.
    postfixList = []
    tokenList = infixexpr.split()

    '''
    En todo este ciclo se hacen una serie de comparaciones entre los operandos y elementos permitidos con los 
    elementos que fueron ingresados por el usuario para poder determinar que se hará con ellos 
    y obtener la expresión postfija.
    '''
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

#Función para invertir una cadena.
def reverted_string(s):
    return s[::-1]

#Función para convertir expresión infija a prefija.
def infixToPrefix(string):
    final = " "
    #Invierte la cadena original.
    infix_reverted = reverted_string(string)
    linfix = infix_reverted.split()

    #Intercambia los ‘(‘ por ‘)’ y viceversa.
    for x in range(len(linfix)):
        if linfix[x] == '(':
            linfix[x] = ')'
        elif linfix[x] == ')':
            linfix[x] = '('

    #Se hace infija a postfija con la cadena del ciclo anterior
    prefix = infixToPostfix(final.join(linfix))

    #Se invierte nuevamente la cadena
    return reverted_string(prefix)