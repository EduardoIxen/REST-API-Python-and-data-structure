from BackEnd.Analyzer.Lexer import tokens

def p_init(t):
    'init : LQUESTION RELEMENTS RQUESTION list_elements LQUESTION DOLLAR RELEMENTS RQUESTION'
    t[0] = t[4]

def p_list_elements(t):
    'list_elements : list_elements element'
    t[1].append(t[2])
    t[0] = t[1]

def p_list_elements2(t):
    'list_elements : element'
    t[0] = [t[1]]  #create list of elements

def p_element(t):
    'element : LQUESTION RELEMENT typeElement RQUESTION list_items LQUESTION DOLLAR RELEMENT RQUESTION'
    t[0] = {'type': t[3], 'dicItems': t[5]}

def p_typeElement(t):
    'typeElement : RTYPE EQUAL STRING'
    t[0] = t[3]

def p_list_items(t):
    'list_items : list_items item'
    t[1].append(t[2])  # add item to list items
    t[0] = t[1]

def p_list_items2(t):
    'list_items : item'
    t[0] = [t[1]] #create list of items

def p_item(t):
    'item : LQUESTION RITEM typeItem EQUAL valyeItem DOLLAR RQUESTION'
    t[0] = {'key': t[3], 'value': t[5]}

def p_valueItem(t):
    '''valyeItem : STRING
                | NUMBER'''
    t[0] = t[1]

def p_typeItem(t):
    '''typeItem : RCARNET
                | RNOMBRE
                | RDPI
                | RCARRERA
                | RCORREO
                | RPASSWORD
                | RCREDITOS
                | REDAD
                | RDESCRIPCION
                | RMATERIA
                | RFECHA
                | RHORA
                | RESTADO
    '''
    t[0] = t[1]

def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc

def parse(inp):
    parserl = yacc.yacc()
    return parserl.parse(inp)

def analyzeFile(content):
    listValues = parse(content)
    return listValues