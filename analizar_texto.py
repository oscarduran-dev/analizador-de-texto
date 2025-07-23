import string  
# Importando Counter para contar la frecuencia de palabras
from collections import Counter  

#Definiendo la clase AnalizadorTexto
class AnalizadorTexto:
    
    #Creando el constructor que recibe una variable texto
    def __init__(self, texto):
        self.texto = texto
        
    #Método para contar cuántas palabras hay en el texto
    def contar_palabras(self):
        palabras = self.texto.split()  #Divide el texto por espacios para obtener las palabras
        return len(palabras)  #Devuelve la cantidad total de palabras
    
    #Método para contar cuántas oraciones hay en el texto
    def contar_oraciones(self):
        oraciones = self.texto.split(".")  #Divide el texto por puntos, que indican el final de una oracion
        oraciones = [o for o in oraciones if o.strip() != '']  #Elimina oraciones vacías (espacios en blanco)
        return len(oraciones)  #Devuelve la cantidad de oraciones encontradas
    
    #Método que devuelve la palabra más larga del texto
    def palabra_mas_larga(self):
        palabras = self.texto.split()  #Divide el texto en palabras
        palabra_larga = max(palabras, key= len)  #Busca la palabra mas larga
        return palabra_larga  #Devuelve la palabra encontrada
    
    #Método para calcular el promedio de letras en las palabras del texto
    def promedio_longitud_palabra(self):
        palabras = self.texto.split()  #Divide el texto en palabras
        #Quita signos de puntuación al inicio y final de cada palabra
        palabras_limpias = [palabra.strip(string.punctuation) for palabra in palabras]
        #Suma la cantidad de letras de todas las palabras limpias (ignora vacías)
        total_letras = sum(len(p) for p in palabras_limpias if p)
        total_palabras = len(palabras_limpias)  #Cuenta cuántas palabras hay
        #Calcula el promedio y lo redondea a 2 decimales (evita división por cero)
        return round(total_letras / total_palabras if total_palabras > 0 else 0, 2)
    
    #Método que devuelve las n palabras más frecuentes del texto (por defecto 5)
    def palabras_frecuentes(self, n=5):
        palabras = self.texto.lower().split()  #Convirtiendo el texto a minúsculas y lo divide en palabras
        #Quitando signos de puntuación al inicio y final de cada palabra
        palabras_limpias = [palabra.strip(string.punctuation) for palabra in palabras]
        contador = Counter(palabras_limpias)  #Creando un diccionario con el conteo de cada palabra
        return contador.most_common(n)  #Devuelve una lista con las n palabras más comunes


# Función principal que muestra el menú interactivo para analizar textos
def menu():
    #Solicitando al usuario que ingrese un texto
    texto_usuario = input("Ingresa un texto: ")
    #Creando una instancia de la clase AnalizadorTexto con el texto ingresado
    analizador = AnalizadorTexto(texto_usuario)
        
    #Iniciando un ciclo infinito para mantener el menú activo hasta que el usuario seleciione salir
    while True:
        #Mostrando el menú de opciones disponibles para el usuario
        print("""Hola, bienvenido al menú interactivo de mi analizador de textos.
            Elige una opción:
            1. Contar palabras
            2. Contar oraciones
            3. Mostrar la palabra mas larga
            4. Promedio de longitud de palabras
            5. Mostrar palabras frecuentes
            6. Cambiar texto
            7. Salir
            """)
        
        try:
            #Solicitando al usuario elegir una opcion del menu y convirtiendolo a entero
            opcion = int(input("Ingresa una opción (Solo números entre el 1 y el 7): "))
            
            #opción 1: contar palabras del texto
            if opcion == 1:
                print(f"Total de palabras: {analizador.contar_palabras()}")
            
            #opción 2: contar oraciones del texto   
            elif opcion == 2:
                print(f"Total de oraciones: {analizador.contar_oraciones()}")
                
            #opción 3: mostrar la palabra mas larga
            elif opcion == 3:
                print(f"La palabra mas larga es: {analizador.palabra_mas_larga()}")
                
            #opción 4: mostrar el promedio de longitud de las palabras
            elif opcion == 4:
                print(f"El promedio de letras por palabra es: {analizador.promedio_longitud_palabra()}")
            
            #opción 5: mostrar las palabras mas frecuentes del texto
            elif opcion == 5:
                try:
                    #pidiendo al usuario cuantas palabras frecuentes quiere ver
                    n = int(input("¿Cuántas palabras frecuentes quieres ver?: "))
                    #muestra cada palabra con su frecuencia
                    for palabra, frecuencia in analizador.palabras_frecuentes(n):
                        print(f"{palabra}: {frecuencia} veces")
                except ValueError:
                    #captura error si el usuario no ingresa un número
                    print(" Por favor, ingresa un número válido.")
                    
            #opción 6: perimite al usuario cambiar el texto
            elif opcion == 6:
                #pide al usuario el nuevo texto
                texto_usuario = input("Ingrese un nuevo texto: ")
                analizador = AnalizadorTexto(texto_usuario)
            
            #opción 7: salir del programa   
            elif opcion == 7:
                print("Saliendo del analizador. Hasta luego.")
                break
            
            #si el usuario inserta un número fuera del rango de opciones
            else:
                print("Ingrese una opción válida...")
        
        #si el usuario ingresa algo que no es un numero entero
        except ValueError:
            print("Por favor, ingresa un número entero válido.")
            
        #captura cualquier error y lo muestra
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")


#Llamando a la función principal para ejecutar el programa
menu()
