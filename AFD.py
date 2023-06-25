import string

#--------------CONSTANTES-------------------#
#Pongo las palabras reservadas en una lista
P_RESERVADAS = ['si','sino','finsi','repetir','hasta','equal','func','finfunc','oprel','opsuma','opmult']
#Usando el módulo string, hago una lista con las caracters de la a hasta la z (minusculas y mayusculas)
LETRAS_lower = list(string.ascii_lowercase)
LETRAS_upper = list(string.ascii_uppercase)
#Creo una lista con los numeros del 0 al 9
NUMEROS = list(range(10))

#-------------------------------------------#

ESTADO_ACEPTADO = "ESTADO ACEPTADO"
ESTADO_NO_ACEPTADO = "ESTADO NO ACEPTADO"
ESTADO_TRAMPA = "ESTADO TRAMPA"

#-------------------------------------------#

#Automatas para c/token

#AFD ID'S

def afd_id(cadena):
    estado_actual = 0
    estados_aceptados = [1]
    
    for caracter in string:
        if estado_actual == 0 and ((caracter in LETRAS_lower) or (caracter in LETRAS_upper)):
            estadoActual = 1
        elif estadoActual == 1 and ((caracter in LETRAS_lower) or (caracter in LETRAS_upper) or (caracter in NUMEROS)):
            estadoActual = 1
        else:
            estadoActual = -1
            return ESTADO_TRAMPA
    
    if estadoActual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

#AFD NUM
def afd_num(string):
    estado_actual = 0
    for caracter in string:
        if caracter in NUMEROS and estado_actual == 0:
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    if estado_actual == 0:
        try:
            value = int(string)
            return ESTADO_ACEPTADO
        except:
            return ESTADO_TRAMPA
    
#AFD "si"
def afd_si(string):
    estado_actual = 0
    estados_aceptados =[2]
    
    for caracter in string:
        if estado_actual == 0 and caracter == 's':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'si':
            estado_actual = 2
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        
    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO
    
#AFD "sino"
def afd_sino(string):
    estado_actual = 0
    estados_aceptados = [4]
    
    for caracter in string:
        if estado_actual == 0 and caracter == 's':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'i':
            estado_actual = 2
        elif estado_actual == 2 and caracter == 'n':
            estado_actual = 3
        elif estado_actual == 3 and caracter == 'o':
            estado_actual = 4
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        
    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO
            
#AFD "finsi"   
def afd_finsi(string):
    estado_actual = 0
    estados_aceptados = [5]
    
    for caracter in string:
        if estado_actual == 0 and caracter == 'f':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'i':
            estado_actual = 2
        elif estado_actual == 2 and caracter == 'n':
            estado_actual = 3
        elif estado_actual == 3 and caracter == 's':
            estado_actual = 4
        elif estado_actual == 4 and caracter == 'i':
            estado_actual = 5
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        
    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

#AFD "repetir"   
def afd_repetir(string):
    estado_actual = 0
    estados_aceptados = [7]
    
    for caracter in string:
        if estado_actual == 0 and caracter == 'r':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'e':
            estado_actual = 2
        elif estado_actual == 2 and caracter == 'p':
            estado_actual = 3
        elif estado_actual == 3 and caracter == 'e':
            estado_actual = 4
        elif estado_actual == 4 and caracter == 't':
            estado_actual = 5
        elif estado_actual == 5 and caracter == 'i':
            estado_actual = 6
        elif estado_actual == 6 and caracter == 'r':
            estado_actual = 7
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        
    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

#AFD "hasta"   
def afd_hasta(string):
    estado_actual = 0
    estados_aceptados = [5]
    
    for caracter in string:
        if estado_actual == 0 and caracter == 'h':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'a':
            estado_actual = 2
        elif estado_actual == 2 and caracter == 's':
            estado_actual = 3
        elif estado_actual == 3 and caracter == 't':
            estado_actual = 4
        elif estado_actual == 4 and caracter == 'a':
            estado_actual = 5
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        
    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

#AFD "equal"   
def afd_equal(string):
    estado_actual = 0
    estados_aceptados = [5]
    
    for caracter in string:
        if estado_actual == 0 and caracter == 'e':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'q':
            estado_actual = 2
        elif estado_actual == 2 and caracter == 'u':
            estado_actual = 3
        elif estado_actual == 3 and caracter == 'a':
            estado_actual = 4
        elif estado_actual == 4 and caracter == 'l':
            estado_actual = 5
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        
    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

#AFD "func"
def afd_func(string):
    estado_actual = 0
    estados_aceptados = [4]
    
    for caracter in string:
        if estado_actual == 0 and caracter == 'f':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'u':
            estado_actual = 2
        elif estado_actual == 2 and caracter == 'n':
            estado_actual = 3
        elif estado_actual == 3 and caracter == 'c':
            estado_actual = 4
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        
    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

#AFD "finfunc"
def afd_finfunc(string):
    estado_actual = 0
    estados_aceptados = [7]
    
    for caracter in string:
        if estado_actual == 0 and caracter == 'f':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'i':
            estado_actual = 2
        elif estado_actual == 2 and caracter == 'n':
            estado_actual = 3
        elif estado_actual == 3 and caracter == 'f':
            estado_actual = 4
        elif estado_actual == 4 and caracter == 'u':
            estado_actual = 5
        elif estado_actual == 5 and caracter == 'n':
            estado_actual = 6
        elif estado_actual == 6 and caracter == 'c':
            estado_actual = 7
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        
    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

#AFD "oprel"   
def afd_oprel(string):
    estado_actual = 0
    estados_aceptados = [5]
    
    for caracter in string:
        if estado_actual == 0 and caracter == 'o':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'p':
            estado_actual = 2
        elif estado_actual == 2 and caracter == 'r':
            estado_actual = 3
        elif estado_actual == 3 and caracter == 'e':
            estado_actual = 4
        elif estado_actual == 4 and caracter == 'l':
            estado_actual = 5
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        
    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

#AFD "opsuma"   
def afd_opsuma(string):
    estado_actual = 0
    estados_aceptados = [6]
    
    for caracter in string:
        if estado_actual == 0 and caracter == 'o':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'p':
            estado_actual = 2
        elif estado_actual == 2 and caracter == 's':
            estado_actual = 3
        elif estado_actual == 3 and caracter == 'u':
            estado_actual = 4
        elif estado_actual == 4 and caracter == 'm':
            estado_actual = 5
        elif estado_actual == 5 and caracter == 'a':
            estado_actual = 6
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        
    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

#AFD "opmult"   
def afd_opmult(string):
    estado_actual = 0
    estados_aceptados = [6]
    
    for caracter in string:
        if estado_actual == 0 and caracter == 'o':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'p':
            estado_actual = 2
        elif estado_actual == 2 and caracter == 'm':
            estado_actual = 3
        elif estado_actual == 3 and caracter == 'u':
            estado_actual = 4
        elif estado_actual == 4 and caracter == 'l':
            estado_actual = 5
        elif estado_actual == 5 and caracter == 't':
            estado_actual = 6
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        
    if estado_actual in estados_aceptados:
        return ESTADO_ACEPTADO
    else:
        return ESTADO_NO_ACEPTADO

#AFD "("
def afd_parentesisIzq(string):
    estado_actual = 0 
    for caracter in string:
        if estado_actual == 0 and caracter == '(':
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        return ESTADO_ACEPTADO

#AFD ")"
def afd_parentesisDer(string):
    estado_actual = 0 
    for caracter in string:
        if estado_actual == 0 and caracter == ')':
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        return ESTADO_ACEPTADO
#AFD ";"
def afd_puntoycoma(string):
    estado_actual = 0 
    for caracter in string:
        if estado_actual == 0 and caracter == ';':
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
        return ESTADO_ACEPTADO
