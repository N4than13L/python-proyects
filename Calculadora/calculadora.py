class Calculadora: 
    def Suma(self, a,b):
        S = a + b
        return S
    def Resta(self, a,b):
        R = a - b
        return R
    def Multiplicacion(self, a,b):
        M = a * b
        return M
    def Division(self, a,b):
        D = a / b
        return D

a = float(input('introduce el primer valor: '))
operador = str(input('introduce el oprador a ejecutar \n + \n - \n * \n / \n :'))
b = float(input('introduce el segundo valor: '))

calcular = Calculadora()

while True:
    try:
        if a and b >= 0 and operador == '+':
            print(calcular.Suma(a,b))
#---volver a inicial variables para poder ejecutar el codigo mas falcilmente--
            a = float(input('introduce el primer valor: '))
            operador = str(input('introduce el oprador a ejecutar \n + \n - \n * \n / \n :'))
            b = float(input('introduce el segundo valor: '))
    

        elif a and b >= 0 and operador == '-':
            print(calcular.Resta(a,b))
#---volver a inicial variables para poder ejecutar el codigo mas falcilmente--           
            a = float(input('introduce el primer valor: '))
            operador = str(input('introduce el oprador a ejecutar \n + \n - \n * \n / \n :'))
            b = float(input('introduce el segundo valor: '))
            
        elif a and b >= 0 and operador == '*':
            print(calcular.Multiplicacion(a,b))
#---volver a inicial variables para poder ejecutar el codigo mas falcilmente--
            a = float(input('introduce el primer valor: '))
            operador = str(input('introduce el oprador a ejecutar \n + \n - \n * \n / \n :'))
            b = float(input('introduce el segundo valor: '))

        elif a and b >= 0 and operador == '/':
            print(calcular.Division(a,b))
#---volver a inicial variables para poder ejecutar el codigo mas falcilmente--
            a = float(input('introduce el primer valor: '))
            operador = str(input('introduce el oprador a ejecutar \n + \n - \n * \n / \n :'))
            b = float(input('introduce el segundo valor: ')) 
        else:
            print('error')
            break
    except ValueError:
        print('error')
        break
    