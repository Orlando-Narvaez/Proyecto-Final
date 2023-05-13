'''
    Desarrollado por: Valentina Oviedo Sanchez, Orlando Narvaez Baracaldo y Eliana Yiset Hernandez Ortiz :)
    Aginatura: TLF
    Nombre: Analizador lexico
    Cadena a evaluar:
    me
    nmaydifigumenigumayiguyonegiguigusumiguresigumuligudivigumodigu˄˅<>EntRealCadenaCaracterPublicoPrivado$Persona1sumresdivmodmul15E3.5R%C%#C#~ciclodecidetipoAla1ala1@12ABCDEFHex
'''
from tkinter import *
from tkinter import messagebox

# Constantes referentes a los tipos de operadores del lenguaje
OPERADOR_RELACIONAL = 'Identificador de un operador relacional'
OPERADOR_LOGICO = 'Identificador de un operador Lógico'
OPERADOR_ASIGNACION = 'Identificador de un operador de Asignación'
INICIAL = 'Identificador para inicar una línea'
METODOS = 'Identificador de método' 
VARIABLES = 'Identificador de variable'
CLASETIPO = 'Identificador de clases'
DECISION = 'Identificador de decisión'
BUCLE = 'Identificador de ciclos'
SEPARADORSENTENCIAS = 'Identificador para separar sentencias'
SIMBOLO_ABRIR_PARENTESIS = 'Identificador para el símbolo de abrir parentesis'
SIMBOLO_CERRAR_PARENTESIS = 'Identificador para el símbolo de cerrar parentesis'
SIMBOLO_ABRIR_LLAVES = 'Identificador para el símbolo de abrir llaves'
SIMBOLO_CERRAR_LLAVES = 'Identificador para el símbolo de cerrar llaves'
TIPODATOENTERO = 'Identificador para los enteros'
TIPODATOREAL = 'Identificador para los reales'
TIPODATOCADENA = 'Identificador para las cadenas'
TIPODATOCARACTER = 'Identificador para los caracteres'
CLASE = 'Identificador para las clases'
OPERADORENTERO = 'Identificador para la asignacion de enteros'
OPERADORREAL = 'Identificador para la asignacion de reales'
OPERADORCADENA = 'Identificador para la asignacion para las cadenas'
OPERADORCARACTER = 'Identificador para la asignacion para los caracteres'
TIPOMODIFICADORACCESO = 'Identificador para los modificadores de acceso'
OPERADORHEXADECIMAL = 'Identificador para Hexadecimal'
OPERADORARITMETICO = 'Operadores aritmeticos'
NORECONOCIDO = 'PALABRA NO RECONOCIDA'

# Clase token
#
# Se compone de un constructor el cual recibe los parametros de:
# @self -> equivalente al this otros lenguajes - palabra reservada para referirse a si mismo
# @lexema -> parte de una palabra que lleva un significado referencial
# @indiceSiguiente -> indice del siguiente token a analizar
#
class Token:
    def __init__(self, lexema, tipo, indiceSiguiente):
        self.lexema = lexema
        self.tipo = tipo
        self.indiceSiguiente = indiceSiguiente
        
            
# Extrae una palabra que califique como identificador de decisión de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#     
def extraerDecision(texto, indice):
    
    if texto[indice] == 'd':
        j = indice+1
        if j < len(texto) and texto[j] == 'e':
            j= j+1
            if j < len(texto) and texto[j] == 'c':
                j= j+1
                if j < len(texto) and texto[j] == 'i':
                    j= j+1
                    if j < len(texto) and texto[j] == 'd':
                        j= j+1
                        if j < len(texto) and texto[j] == 'e':
                            j= j+1
                            lex= texto[indice:j]
                            token = Token(lex,DECISION,j)
                            return token
                      
                        
# Extrae una palabra que califique como bucle o ciclo de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado   
def extraerBucle(texto, indice):
    
    if texto[indice] == 'c':
        j = indice+1
        if j < len(texto) and texto[j] == 'i':
            j= j+1
            if j < len(texto) and texto[j] == 'c':
                j= j+1
                if j < len(texto) and texto[j] == 'l':
                    j= j+1
                    if j < len(texto) and texto[j] == 'o':
                        j= j+1
                        lex= texto[indice:j]
                        token = Token(lex,BUCLE,j)
                        return token
                    
# Extrae una palabra que califique como el operador <= de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#         
def extraerOperadorMenorIgual(texto, indice):
    
    if texto[indice] == 'm':
        j = indice+1
        if j < len(texto) and texto[j] == 'e':
            j= j+1
            if j < len(texto) and texto[j] == 'n':
                j= j+1
                if j < len(texto) and texto[j] == 'i':
                    j= j+1
                    if j < len(texto) and texto[j] == 'g':
                        j= j+1
                        if j < len(texto) and texto[j] == 'u':
                            j= j+1
                            lex= texto[indice:j]
                            token = Token(lex,OPERADOR_RELACIONAL,j)
                            return token
                               
# Extrae una palabra que califique como el operador >= de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#                               
def extraerOperadorMayorIgual(texto, indice):
    
    if texto[indice] == 'm':
        j = indice+1
        if j < len(texto) and texto[j] == 'a':
            j= j+1
            if j < len(texto) and texto[j] == 'y':
                j= j+1
                if j < len(texto) and texto[j] == 'i':
                    j= j+1
                    if j < len(texto) and texto[j] == 'g':
                        j= j+1
                        if j < len(texto) and texto[j] == 'u':
                            j= j+1
                            lex= texto[indice:j]
                            token = Token(lex,OPERADOR_RELACIONAL,j)
                            return token
                        

# Extrae una palabra que califique como el operador < de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#       
def extraerOperadorMenorQue(texto, indice):
    
    if texto[indice] == 'm':
        j = indice+1
        if j < len(texto) and texto[j] == 'e':
            j=j+1
            if j < len(texto) and texto[j] == 'n':
                j= j+1
                lex= texto[indice:j]
                token = Token(lex,OPERADOR_RELACIONAL,j)
                return token
            
# Extrae una palabra que califique como el operador > de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#       
def extraerOperadorMayorQue(texto, indice):
    
    if texto[indice] == 'm':
        j = indice+1
        if j < len(texto) and texto[j] == 'a':
            j=j+1
            if j < len(texto) and texto[j] == 'y':
                j= j+1
                lex= texto[indice:j]
                token = Token(lex,OPERADOR_RELACIONAL,j)
                return token
            
# Extrae una palabra que califique como el operador = de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#       
def extraerOperadorIgual(texto, indice):
    
    if texto[indice] == 'i':
        j = indice+1
        if j < len(texto) and texto[j] == 'g':
            j=j+1
            if j < len(texto) and texto[j] == 'u':
                j= j+1
                lex= texto[indice:j]
                token = Token(lex,OPERADOR_RELACIONAL,j)
                return token
            
# Extrae una palabra que califique como el operador != de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#       
def extraerOperadorDiferente(texto, indice):
    
    if texto[indice] == 'd':
        j = indice+1
        if j < len(texto) and texto[j] == 'i':
            j=j+1
            if j < len(texto) and texto[j] == 'f':
                j= j+1
                lex= texto[indice:j]
                token = Token(lex,OPERADOR_RELACIONAL,j)
                return token
                       
# Extrae una palabra que califique como el valor asignado para la separación de sentencias de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#       
def extraerSeparadorSentencias(texto, indice):
    
    if texto[indice] =='~':
        j = indice+1
        lex= texto[indice:j]
        token = Token(lex,SEPARADORSENTENCIAS,j)
        return token
         
# Extrae una palabra que califique como operador logico(&&,||,)de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#  
def extraerOperadoresLogicos(texto, indice):
    
    if texto[indice] == 'y':
        j = indice+1
        lex= texto[indice:j]
        token = Token(lex,OPERADOR_LOGICO,j)
        return token
    else:
        if texto[indice] == 'o':
            j = indice+1
            lex= texto[indice:j]
            token = Token(lex,OPERADOR_LOGICO,j)
            return token
        else:
            if texto[indice] == 'n':
                j = indice+1
                if j < len(texto) and texto[j] == 'e':
                    j=j+1
                    if j < len(texto) and texto[j] == 'g':
                        j= j+1
                        lex= texto[indice:j]
                        token = Token(lex,OPERADOR_LOGICO,j)
                        return token
                                                     
# Extrae una palabra que califique como el operador de asignación de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#            
def extraerOperadorAsignacion(texto, indice):
    
    if texto[indice] == 'i':
        j = indice+1
        if j < len(texto) and texto[j] == 'g':
            j= j+1
            if j < len(texto) and texto[j] == 'u':
                j= j+1
                if j < len(texto) and texto[j] == 'i':
                    j= j+1
                    if j < len(texto) and texto[j] == 'g':
                        j= j+1
                        if j < len(texto) and texto[j] == 'u':
                            j= j+1
                            lex= texto[indice:j]
                            token = Token(lex,OPERADOR_ASIGNACION,j)
                            return token     
                        
# Extrae una palabra que califique como el operador de asignación para sumas de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#          
def extraerOperadorSumaAsignacion(texto, indice):
    
    if texto[indice] == 's':
        j = indice+1
        if j < len(texto) and texto[j] == 'u':
            j= j+1
            if j < len(texto) and texto[j] == 'm':
                j= j+1
                if j < len(texto) and texto[j] == 'i':
                    j= j+1
                    if j < len(texto) and texto[j] == 'g':
                        j= j+1
                        if j < len(texto) and texto[j] == 'u':
                            j= j+1
                            lex= texto[indice:j]
                            token = Token(lex,OPERADOR_ASIGNACION,j)
                            return token   
                        
# Extrae una palabra que califique como el operador de asignación para restas de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#     
def extraerOperadorRestaAsignacion(texto, indice):
    
    if texto[indice] == 'r':
        j = indice+1
        if j < len(texto) and texto[j] == 'e':
            j= j+1
            if j < len(texto) and texto[j] == 's':
                j= j+1
                if j < len(texto) and texto[j] == 'i':
                    j= j+1
                    if j < len(texto) and texto[j] == 'g':
                        j= j+1
                        if j < len(texto) and texto[j] == 'u':
                            j= j+1
                            lex= texto[indice:j]
                            token = Token(lex,OPERADOR_ASIGNACION,j)
                            return token   
                        
# Extrae una palabra que califique como el operador de asignación para multiplicación de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#     
def extraerOperadorMultAsignacion(texto, indice):
    
    if texto[indice] == 'm':
        j = indice+1
        if j < len(texto) and texto[j] == 'u':
            j= j+1
            if j < len(texto) and texto[j] == 'l':
                j= j+1
                if j < len(texto) and texto[j] == 'i':
                    j= j+1
                    if j < len(texto) and texto[j] == 'g':
                        j= j+1
                        if j < len(texto) and texto[j] == 'u':
                            j= j+1
                            lex= texto[indice:j]
                            token = Token(lex,OPERADOR_ASIGNACION,j)
                            return token   
                        
# Extrae una palabra que califique como el operador de asignación para divisiones de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#     
def extraerOperadorDivAsignacion(texto, indice):
    
    if texto[indice] == 'd':
        j = indice+1
        if j < len(texto) and texto[j] == 'i':
            j= j+1
            if j < len(texto) and texto[j] == 'v':
                j= j+1
                if j < len(texto) and texto[j] == 'i':
                    j= j+1
                    if j < len(texto) and texto[j] == 'g':
                        j= j+1
                        if j < len(texto) and texto[j] == 'u':
                            j= j+1
                            lex= texto[indice:j]
                            token = Token(lex,OPERADOR_ASIGNACION,j)
                            return token  
                        

# Extrae una palabra que califique como el operador de asignación para modulos de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#     
def extraerOperadorModuloAsignacion(texto, indice):
    
    if texto[indice] == 'm':
        j = indice+1
        if j < len(texto) and texto[j] == 'o':
            j= j+1
            if j < len(texto) and texto[j] == 'd':
                j= j+1
                if j < len(texto) and texto[j] == 'i':
                    j= j+1
                    if j < len(texto) and texto[j] == 'g':
                        j= j+1
                        if j < len(texto) and texto[j] == 'u':
                            j= j+1
                            lex= texto[indice:j]
                            token = Token(lex,OPERADOR_ASIGNACION,j)
                            return token         
                    

# Extrae una palabra que califique como el valor asignado al inicial de una linea de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#     
def extraerInicialLinea(texto, indice):
    
    if texto[indice] == '@':
        j = indice+1
        lex= texto[indice:j]
        token = Token(lex,INICIAL,j)
        return token
    
    
# Extrae una palabra que califique como la asignación de tipo clase de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#     
def extraerClaseTipo(texto, indice):     
    
    if texto[indice] == 't':
        j=indice+1
        if j < len(texto) and texto[j] == 'i':
            j=j+1
            if j < len(texto) and texto[j] == 'p':
                j=j+1
                if j < len(texto) and texto[j] == 'o':
                    j=j+1
                    lex = texto[indice:j]
                    token = Token(lex,CLASETIPO,j)
                    return token
            
    
# Función auxiliar para identificar letras mayusculas
#
# @caracter -> caracter a analizar
# @return ->  retorna true o false, dependiendo si el caracter es una letra mayuscula
#    
def esMayuscula(caracter):
    return caracter >= 'A' and caracter <= 'Z'


# Función auxiliar para identificar letras que se manejan en un hexadecimal
#
# @caracter -> caracter a analizar
# @return ->  retorna true o false, dependiendo si el caracter cumple con la condición
#   
def hexadecimal(caracter):
    return caracter >= 'A' and caracter <= 'F'


# Función auxiliar para identificar letras minusculas
#
# @caracter -> caracter a analizar
# @return ->  retorna true o false, dependiendo si el caracter cumple con la condición
#   
def esMinuscula(caracter):
    return caracter >= 'a' and caracter <= 'z'


# Función auxiliar para identificar letras
#
# @caracter -> caracter a analizar
# @return ->  retorna true o false, dependiendo si el caracter cumple con la condición de ser una letra
#             no importa si es mayuscula o minuscula
#   
def esLetra(caracter):
    return caracter >= 'a' and caracter <= 'z' or caracter >= 'A' and caracter <= 'Z'


# Función auxiliar para identificar los digitos
#
# @caracter -> caracter a analizar
# @return ->  retorna true o false, dependiendo si el caracter cumple con la condición de ser un número
#   
def esDigito(caracter):
    return caracter >= '0' and caracter <= '9'         

# Extrae una palabra que califique como el nombre valido de una variable de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#     
def extraerNombresVariables(texto, indice):
    
    if esMayuscula(texto[indice]):
        j= indice+1
        if j < len(texto) and esLetra(texto[j]):
            j=j+1
            while j < len(texto) and esLetra(texto[j]):
                j=j+1
            if j < len(texto) and esDigito(texto[j]):
                j=j+1
                lex=texto[indice:j]
                token = Token(lex,VARIABLES,j)
                return token
        else:
            if j < len(texto) and esDigito(texto[j]):
                j=j+1
                lex=texto[indice:j]
                token = Token(lex,METODOS,j)
                return token

# Extrae una palabra que califique como el nombre valido de un método de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#
def extraerNombresMetodos(texto, indice):
    
    if esMinuscula(texto[indice]):
        j=indice+1
        if j < len(texto) and esLetra(texto[j]):
            while j < len(texto) and esLetra(texto[j]):
                j=j+1
            if j < len(texto) and esDigito(texto[j]):
                j=j+1
                lex = texto[indice:j]
                token = Token(lex,METODOS,j)
                return token
        else:
            if j < len(texto) and esDigito(texto[j]):
                j=j+1
                lex= texto[indice:j]
                token = Token(lex,METODOS,j)
                return token
            
# Extrae una palabra que califique como el simbolo de abrir parentesis de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#       
def extraerSimboloAbrir(texto, indice):
    
    if texto[indice] =='<':
        j = indice+1
        lex= texto[indice:j]
        token = Token(lex,SIMBOLO_ABRIR_PARENTESIS,j)
        return token
    
# Extrae una palabra que califique como el simbolo de cerrar de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#      
def extraerSimboloCerrar(texto, indice):
    
    if texto[indice] =='>':
        j = indice+1
        lex= texto[indice:j]
        token = Token(lex,SIMBOLO_CERRAR_PARENTESIS,j)
        return token

# Extrae una palabra que califique como el simbolo de abrir llaves de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#       
def extraerSimboloAbrirLlaves(texto, indice):
    
    if texto[indice] =='˄':
        j = indice+1
        lex= texto[indice:j]
        token = Token(lex,SIMBOLO_ABRIR_LLAVES,j)
        return token
    
# Extrae una palabra que califique como el simbolo de cerrar llaves de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#       
def extraerSimboloCerrarLlaves(texto, indice):
    
    if texto[indice] =='˅':
        j = indice+1
        lex= texto[indice:j]
        token = Token(lex,SIMBOLO_CERRAR_LLAVES,j)
        return token

# Extrae una palabra que califique para los enteros de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#
def extraerTipoEntero(texto, indice):
    
    if texto[indice] == 'E':
        j = indice+1
        if j < len(texto) and texto[j] == 'n':
            j=j+1
            if j < len(texto) and texto[j] == 't':
                j= j+1
                lex= texto[indice:j]
                token = Token(lex,TIPODATOENTERO,j)
                return token
            
# Extrae una palabra que califique como identificador para reales o tipo de dato real de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#
def extraerTipoReal(texto, indice):
    
    if texto[indice] == 'R':
        j = indice+1
        if j < len(texto) and texto[j] == 'e':
            j=j+1
            if j < len(texto) and texto[j] == 'a':
                j=j+1
                if j < len(texto) and texto[j] == 'l':
                    j= j+1
                    lex= texto[indice:j]
                    token = Token(lex,TIPODATOREAL,j)
                    return token
                
# Extrae una palabra que califique como cadena o el tipo de dato String de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#
def extraerTipoCadena(texto, indice):
    
    if texto[indice] == 'C':
        j = indice+1
        if j < len(texto) and texto[j] == 'a':
            j= j+1
            if j < len(texto) and texto[j] == 'd':
                j= j+1
                if j < len(texto) and texto[j] == 'e':
                    j= j+1
                    if j < len(texto) and texto[j] == 'n':
                        j= j+1
                        if j < len(texto) and texto[j] == 'a':
                            j= j+1
                            lex= texto[indice:j]
                            token = Token(lex,TIPODATOCADENA,j)
                            return token
                        
# Extrae una palabra que califique como caracter o el tipo caracter de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#
def extraerTipoCaracter(texto, indice):
    
    if texto[indice] == 'C':
        j = indice+1
        if j < len(texto) and texto[j] == 'a':
            j= j+1
            if j < len(texto) and texto[j] == 'r':
                j= j+1
                if j < len(texto) and texto[j] == 'a':
                    j= j+1
                    if j < len(texto) and texto[j] == 'c':
                        j= j+1
                        if j < len(texto) and texto[j] == 't':
                            j= j+1
                            if j < len(texto) and texto[j] == 'e':
                                j= j+1
                                if j < len(texto) and texto[j] == 'r':
                                    j= j+1
                                    lex= texto[indice:j]
                                    token = Token(lex,TIPODATOCARACTER,j)
                                    return token
                                
# Extrae una palabra que califique como el nombre valido de una clase de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#
def extraerNombreClase(texto, indice):
    
    if texto[indice] == '$':
        j=indice+1
        if j < len(texto) and esLetra(texto[j]):
            j=j+1
            while j < len(texto) and esLetra(texto[j]):
                j=j+1
            if j < len(texto) and esDigito(texto[j]):
                j+j+1
                lex= texto[indice:j]
                token= Token(lex,CLASE,j)
                return token
            
# Extrae una palabra que califique como el operador de enteros de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#     
def extraerAsignacionEntero(texto,indice):
    
    if esDigito(texto[indice]):
        j=indice+1
        while j < len(texto) and esDigito(texto[j]):
            j=j+1
        
        if j < len(texto) and texto[j] == 'E':
            j=j+1
            lex=texto[indice:j]
            token = Token(lex,OPERADORENTERO,j)
            return token
        
# Extrae una palabra que califique como el operador de reales de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#     
def extraerAsignacionReal(texto,indice):
    
    if esDigito(texto[indice]):
        j=indice+1
        while j < len(texto) and esDigito(texto[j]):
            j=j+1
        
        if j < len(texto) and texto[j] == '.':
            j=j+1
            if j < len(texto) and esDigito(texto[j]):
                j=j+1
                while j < len(texto) and esDigito(texto[j]):
                    j=j+1
                
                if j < len(texto) and texto[j] == 'R':
                    j=j+1
                    lex=texto[indice:j]
                    token = Token(lex,OPERADORREAL,j)
                    return token
                
# Extrae una palabra que califique como la asignación de los String de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#
def extraerAsignacionCadenas(texto, indice):
    
    if texto[indice] == '%':
        j=indice+1
        if j<len(texto) and texto[j] == 'C':
            j=j+1
            if j<len(texto) and texto[j] =='%':
                j=j+1
                lex=texto[indice:j]
                token=Token(lex,OPERADORCADENA,j)
                return token
            
# Extrae una palabra que califique como la asignación de los caracteres de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#              
def extraerAsignacionCaracter(texto, indice):
    
    if texto[indice] == "#":
        j=indice+1
        if j<len(texto) and texto[j] == 'C':
            j=j+1
            if j<len(texto) and texto[j] =="#":
                j=j+1
                lex=texto[indice:j]
                token=Token(lex,OPERADORCARACTER,j)
                return token
            
# Extrae una palabra que califique como modificador de acceso de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#
def extraerTipoModificadorAcceso(texto,indice):
    
    if texto[indice] == 'P':
        j=indice+1
        if j<len(texto) and texto[j]=='u':
            j=j+1
            if j<len(texto) and texto[j]=='b':
                j=j+1
                if j<len(texto) and texto[j]=='l':
                    j=j+1
                    if j<len(texto) and texto[j]=='i':
                        j=j+1
                        if j<len(texto) and texto[j]=='c':
                            j=j+1
                            if j<len(texto) and texto[j]=='o':
                                j=j+1
                                lex= texto[indice:j]
                                token=Token(lex,TIPOMODIFICADORACCESO,j)
                                return token
        else:
            if j<len(texto) and texto[j]=='r':
                j=j+1
                if j<len(texto) and texto[j]=='i':
                    j=j+1
                    if j<len(texto) and texto[j]=='v':
                        j=j+1
                        if j<len(texto) and texto[j]=='a':
                            j=j+1
                            if j<len(texto) and texto[j]=='d':
                                j=j+1
                                if j<len(texto) and texto[j]=='o':
                                    j=j+1
                                    lex= texto[indice:j]
                                    token=Token(lex,TIPOMODIFICADORACCESO,j)
                                    return token
                                
# Extrae una palabra que califique como identificador hexadecimal de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#
def extraerTipoHexadecimal(texto, indice):
    
    if texto[indice] == 'H':
        j = indice+1
        if j < len(texto) and texto[j] == 'e':
            j=j+1
            if j < len(texto) and texto[j] == 'x':
                j= j+1
                lex= texto[indice:j]
                token = Token(lex,OPERADORHEXADECIMAL,j)
                return token
            
# Extrae una palabra que califique como un valor hexadecimal de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#     
def extraerHexadecimal(texto,indice):
    
    if esDigito(texto[indice]):
        j=indice+1
        while j < len(texto) and esDigito(texto[j]):
            j=j+1
        
        while j < len(texto) and hexadecimal(texto[j]):
            j=j+1
        
        lex=texto[indice:j]
        token = Token(lex,OPERADORHEXADECIMAL,j)
        return token
    
# Extrae una palabra que califique como operadores aritmeticosde la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#           
def extraerOperadoresAritmeticos(texto, indice):
    
    if texto[indice] == 'm':
        j = indice+1
        if j < len(texto) and texto[j] == 'o':
            j=j+1
            if j < len(texto) and texto[j] == 'd':
                j= j+1
                lex= texto[indice:j]
                token = Token(lex,OPERADORARITMETICO,j)
                return token
    else:
        if texto[indice] == 's':
            j = indice+1
            if j < len(texto) and texto[j] == 'u':
                j=j+1
                if j < len(texto) and texto[j] == 'm':
                    j= j+1
                    lex= texto[indice:j]
                    token = Token(lex,OPERADORARITMETICO,j)
                    return token
        else:
            if texto[indice] == 'r':
                j = indice+1
                if j < len(texto) and texto[j] == 'e':
                    j=j+1
                    if j < len(texto) and texto[j] == 's':
                        j= j+1
                        lex= texto[indice:j]
                        token = Token(lex,OPERADORARITMETICO,j)
                        return token
            else:
                if texto[indice] == 'm':
                    j = indice+1
                    if j < len(texto) and texto[j] == 'u':
                        j=j+1
                        if j < len(texto) and texto[j] == 'l':
                            j= j+1
                            lex= texto[indice:j]
                            token = Token(lex,OPERADORARITMETICO,j)
                            return token
                else:
                    if texto[indice] == 'd':
                        j = indice+1
                        if j < len(texto) and texto[j] == 'i':
                            j=j+1
                            if j < len(texto) and texto[j] == 'v':
                                j= j+1
                                lex= texto[indice:j]
                                token = Token(lex,OPERADORARITMETICO,j)
                                return token
                            
# Extrae un valor no reconocido de la cadena texto a partir de la posición del incide
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
# El Token se compone del lexema, el tipo de operador y la posición del siguiente lexema o final del analizado
#     
def extraerNoReconocido (texto, indice):
    j= indice+1
    lex = texto[indice:j]
    token = Token(lex,NORECONOCIDO,j)
    return token
                    
# Extrae el token de la cadena texto a partir de la posición indice
#
# @texto -> cadena de la cual se extrae un identficador
# @indice -> posición a partir de la cual se va a extraer el identificador
# @return ->  retorna el token respectivo al tipo entero 
#
def extraerSiguienteToken(texto, indice):
    
    token= extraerOperadorMenorIgual(texto,indice)
    if token != None:
        return token
    
    token= extraerOperadorMayorIgual(texto,indice)
    if token != None:
        return token
    
    token= extraerOperadorMenorQue(texto,indice)
    if token != None:
        return token
    
    token= extraerOperadorMayorQue(texto,indice)
    if token != None:
        return token
    
    token= extraerOperadorDiferente(texto,indice)
    if token != None:
        return token
    
    token= extraerOperadoresLogicos(texto,indice)
    if token != None:
        return token
    
    token= extraerOperadorSumaAsignacion(texto,indice)
    if token != None:
        return token
    
    token= extraerOperadorRestaAsignacion(texto,indice)
    if token != None:
        return token
    
    token= extraerOperadorMultAsignacion(texto,indice)
    if token != None:
        return token
    
    token= extraerOperadorDivAsignacion(texto,indice)
    if token != None:
        return token
    
    token= extraerOperadorModuloAsignacion(texto,indice)
    if token != None:
        return token
    
    token= extraerOperadorAsignacion(texto,indice)
    if token != None:
        return token
    
    token= extraerOperadorIgual(texto,indice)
    if token != None:
        return token
    
    token= extraerSimboloAbrir(texto,indice)
    if token != None:
        return token
    
    token= extraerSimboloAbrirLlaves(texto,indice)
    if token != None:
        return token
    
    token= extraerSimboloCerrar(texto,indice)
    if token != None:
        return token
    
    token= extraerSimboloCerrarLlaves(texto,indice)
    if token != None:
        return token
    
    token= extraerTipoEntero(texto,indice)
    if token != None:
        return token
    
    token= extraerTipoReal(texto,indice)
    if token != None:
        return token
    
    token= extraerTipoCadena(texto,indice)
    if token != None:
        return token
    
    token= extraerTipoCaracter(texto,indice)
    if token != None:
        return token
    
    token= extraerTipoModificadorAcceso(texto,indice)
    if token != None:
        return token
    
    token= extraerNombreClase(texto,indice)
    if token != None:
        return token
    
    token= extraerOperadoresAritmeticos(texto,indice)
    if token != None:
        return token
    
    token= extraerAsignacionEntero(texto,indice)
    if token != None:
        return token
    
    token= extraerAsignacionReal(texto,indice)
    if token != None:
        return token
    
    token= extraerAsignacionCadenas(texto,indice)
    if token != None:
        return token
    
    token= extraerAsignacionCaracter(texto,indice)
    if token != None:
        return token
    
    token= extraerSeparadorSentencias(texto,indice)
    if token != None:
        return token
    
    token= extraerBucle(texto,indice)
    if token != None:
        return token
    
    token= extraerDecision(texto,indice)
    if token != None:
        return token
    
    token= extraerDecision(texto,indice)
    if token != None:
        return token
    
    token= extraerClaseTipo(texto,indice)
    if token != None:
        return token
    
    token= extraerNombresVariables(texto,indice)
    if token != None:
        return token
    
    token= extraerNombresMetodos(texto,indice)
    if token != None:
        return token
    
    token= extraerInicialLinea(texto,indice)
    if token != None:
        return token
    
    token= extraerHexadecimal(texto,indice)
    if token != None:
        return token
    
    token= extraerTipoHexadecimal(texto,indice)
    if token != None:
        return token
    
    token= extraerNoReconocido(texto,indice)
    if token != None:
        return token
    
# Extrae los tokens de un texto dado y los almacena en una lista
#
# @texto -> cadena de la cual se extraen los identificadores
# @return ->  retorna la lista de tokens analizados
#
def extraerTokens(texto):
    
    indice=0
    listTokens=[]
    token=lambda:None
   
    while indice < len(texto):
        token = extraerSiguienteToken(texto,indice)
        listTokens.append(token)
        indice = token.indiceSiguiente
        
    return listTokens

# Función que analiza y plasma la respuesta analizada en la interfaz de usuario
#
# @texto -> cadena de la cual se extraen los identificadores
#
def mainBotAnalizador(texto):   
    
    listTokens=[]
    analisis=''
    
    if texto!= '' and texto != ' ':
        chatLog.insert(END, "    ")
        chatLog.image_create(END, image = imgRU, pady=20)
        chatLog.insert(END, '   CADENA A ANALIZAR')
        chatLog.insert(END, '\n')
        chatLog.insert(END, '  ' + texto + '\n')

        listTokens = extraerTokens(texto)
        for i in listTokens:
            analisis= analisis + '  Lexema: ' + i.lexema + ' ------> Tipo: ' + i.tipo + '\n'
            
        chatLog.insert(END, "    ")
        chatLog.image_create(END, image = imgRB, pady=20)
        chatLog.insert(END, '   RESPUESTA ANALIZADOR')
        chatLog.insert(END, '\n')
        chatLog.insert(END, analisis+ '\n')
    
    else:
        messagebox.showerror("Error", "Por favor ingrese un texto valido")
        
        
# Diseño de interfaz de usuario por medio de tkinder
#
# @botonEnviar -> botón que invoca en la acción la función que añade los mensajes al componente text o chatLog
# @img -> imagen general de la interfaz
# @imgRB -> imagen de respuesta del analizador 
# @imgRu -> imagen de usuario
# @scrollbar -> componente que permite dar scroll en la interfaz
# @Label -> componente donde ingresan el texto a analizar
# @texto -> variable que almacena el valor ingresado en el label
# @entradaTexto -> almacena y envia los datos a la varible texto
##
root = Tk()
root.title("Analizador léxico")
root.geometry("685x600")
root.resizable(width=False, height=False)

img = PhotoImage(file='./img/bot.png')
imgRB = PhotoImage(file='./img/botR.png')
imgRU = PhotoImage(file='./img/usuario.png')

chatLog = Text(root, bd=0, bg="white", height="10", width="50", font="Helvetica", pady=10, )
scrollbar = Scrollbar(root, command=chatLog.yview, cursor="heart")  
chatLog['yscrollcommand'] = scrollbar.set
chatLog.config(foreground="#2C3E50", font=("Verdana", 12 ))
chatLog.pack(expand= 1, fill= BOTH)
frame = Frame(root)
frame.pack(fill="x")
Label(frame, image=img).pack(side=TOP, pady=20)
Label(frame, text="Analizador Léxico", font=("Helvetica", 12, "bold")).pack(anchor="center", pady=10)
texto = StringVar()
entradaTexto = Entry(frame)
entradaTexto.config(bd=5, font=("Verdana", 10), width=50, textvariable=texto)
entradaTexto.pack(padx=20)
botonEnviar = Button(frame, text="Analizar", font= 'currier 13 bold', width= 15 , fg= '#17202A', bg= '#A6B2B3', highlightbackground= 'black', highlightthickness = 2)
botonEnviar.config(bd=3, font=("Helvetica", 10, "bold"), command=lambda:mainBotAnalizador(texto.get()))
botonEnviar.pack(pady=10)
root.mainloop()


# menmaydifigumenigumayiguyonegiguigusumiguresigumuligudivigumodigu˄˅<>EntRealCadenaCaracterPublicoPrivado$Persona1sumresdivmodmul15E3.5R%C%#C#~ciclodecidetipoAla1ala1@12ABCDEFHex