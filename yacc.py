import mlexer
import ply.yacc as yacc


tokens = mlexer.tokens

precedence = (
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDE'),
    ('right', 'UMINUS'),            # Unary minus operator
)

def p_expresion(p):
    '''expresion : expresion_suma
    | expresion_resta
    | termino'''


def p_termino(p):
    '''termino : termino_mul
    | termino_div
    | factor'''


def p_factor(p):
    '''factor : NUMBER
    | VAR
    | PARENTH_IZQ expresion PARENTH_DER'''


def p_asignar(p):
    '''asignar : VAR IGUAL expresion'''
    vars[p[1]] = p[3]


def p_expresion_suma(p):
    '''expresion_suma : expresion MAS termino'''
    p[0] = p[1] + p[3]


def p_expresion_resta(p):
    '''expresion_resta : expresion MENOS termino'''
    p[0] = p[1] - p[3]


def p_termino_mult(p):
    '''termino_mul : termino POR factor'''
    p[0] = p[1] * p[3]


def p_termino_div(p):
    '''termino_div : termino DIVIDE  factor'''
    p[0] = p[1] / p[2]


def p_expresion_termino(p):
    '''expresion_termino : termino'''
    p[0] = p[1]


def p_termino_factor(p):
    '''termino_factor : factor'''
    p[0] = p[1]


def p_factor_num(p):
    '''factor_num : NUMBER'''
    p[0] = p[1]


def p_expresion_uminus(p):
    'expresion_uminus : MENOS expresion %prec UMINUS'
    p[0] = -p[2]


def p_factor_variable(p):
    '''factor_variable : VAR'''
    if vars.has_key(p[1]):
        p[0] = vars[p[1]]
    else:
        print("Undefined Variable", p[1], "in line no.", p.lineno(1))


def p_factor_expr(p):
    '''factor_expr : PARENTH_IZQ expresion PARENTH_DER'''
    p[0] = p[2]


def p_logica(p):
    '''logica : logica OR expresion
    | logica AND expresion
    | NEGADO expresion'''


def p_logica_or(p):
    '''logica_or : logica OR expresion'''
    p[0] = p[1] or p[3]


def p_logica_and(p):
    '''logica_and : logica AND expresion'''
    p[0] = p[1] and p[3]


def p_logica_negacion(p):
    '''logica_negacion : NEGADO VAR'''
    p[0] = not p[1]


def p_comparacion(p):
    '''comparacion : expresion IDENTICO expresion
    | expresion DIFERENTE expresion
    | expresion MAYOR expresion
    | expresion MENOR expresion'''

    if p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]


##PROYECTO LENGUAJES, DEFINICION DE EXPRESIONES LAMBDA JAVA 8##

def p_empty(p):
    '''empty : '''
    p[0] = None


#PRIMER VAR DEBERIA SER UN TIPO
def p_expresion_interna(p):
    '''expresion_interna : VAR VAR COMA expresion_interna
    | VAR VAR
    | VAR'''


parser = yacc.yacc(debug = False, write_tables = False)

while True:
    s = input('Hola')
    parser.parse()



