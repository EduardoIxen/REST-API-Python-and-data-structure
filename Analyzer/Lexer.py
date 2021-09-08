reserved = {
    'Elements': 'RELEMENTS',
    'element' : 'RELEMENT',
    'type' : 'RTYPE',
    'item' : 'RITEM',
    'Carnet' : 'RCARNET',
    'Correo' : 'RCORREO',
    'DPI' : 'RDPI',
    'Nombre' : 'RNOMBRE',
    'Carrera' : 'RCARRERA',
    'Password' : 'RPASSWORD',
    'Creditos' : 'RCREDITOS',
    'Edad' : 'REDAD',
    'Descripcion' : 'RDESCRIPCION',
    'Materia' : 'RMATERIA',
    'Fecha' : 'RFECHA',
    'Hora' : 'RHORA',
    'Estado' : 'RESTADO'
}

tokens = [
    'LQUESTION',
    'DOLLAR',
    'RQUESTION',
    'EQUAL',
    'ID',
    'NUMBER',
    'STRING'
] + list(reserved.values())

#Tokens
t_LQUESTION = r'\¿'
t_DOLLAR = r'\$'
t_RQUESTION = r'\?'
t_EQUAL = r'\='


def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID') #check if it is a reserver word
    return t

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_STRING(t):
    r'\"([^\\\"]|\\.)*\"'
    t.value = t.value[1:-1]  # remove quotes
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex

import re
lexer = lex.lex(reflags=re.IGNORECASE)