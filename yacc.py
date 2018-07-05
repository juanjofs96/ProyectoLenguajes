import mlexer
import ply.yacc as yacc


tokens = mlexer.tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),            # Unary minus operator
)


def p_expresion(p):
    '''expresion : expresion MAS termino
    | expresion MENOS termino
    | termino'''


def p_termino(p):
    '''termino : termino POR factor
    | termino DIVIDE factor
    | factor'''


def p_factor(p):
    '''factor : NUMERO
    | VAR
    | PARENTH_IZQ expresion PARENTH_DER'''


def p_asignar(p):
    '''asignar : VAR IGUAL expresion'''
    vars[p[1]] = p[3]


def p_expresion_suma(p):
    '''expresion : expresion MAS termino'''
    p[0] = p[1] + p[3]


def p_expresion_resta(p):
    '''expresion : expresion MENOS termino'''
    p[0] = p[1] - p[3]


def p_termino_mult(p):
    '''termino : termino POR factor'''
    p[0] = p[1] * p[3]


def p_termino_div(p):
    '''termino : termino DIVIDE  factor'''
    p[0] = p[1] / p[2]


def p_expresion_termino(p):
    '''expresion : termino'''
    p[0] = p[1]


def p_termino_factor(p):
    '''termino : factor'''
    p[0] = p[1]


def p_factor_num(p):
    '''factor : NUMERO'''
    p[0] = p[1]


def p_expresion_uminus(p):
    'expresion : MENOS expresion %prec UMINUS'
    p[0] = -p[2]


def p_factor_variable(p):
    '''factor : VAR'''
    if vars.has_key(p[1]):
        p[0] = vars[p[1]]
    else:
        print("Undefined Variable", p[1], "in line no.", p.lineno(1))



def p_factor_expr(p):
    '''factor : PARENTH_IZQ expresion PARENTH_DER'''
    p[0] = p[2]


def p_logica(p):
    '''logica : logica OR expresion
    | logica AND expresion
    | logica XOR expresion
    | NEGADO expresion'''


def p_logica_or(p):
    '''logica : logica OR expresion'''
    p[0] = p[1] or p[3]


def p_logica_and(p):
    '''logica : logica AND expresion'''
    p[0] = p[1] and p[3]


def p_logica_xor(p):
    '''logica : logica DIFERENTE expresion''' #XOR es equivalente a evaluar si dos expresiones son diferentes o no.
    p[0] = not(p[1] == p[3])


def p_logica_negacion(p):
    '''logica : NEGADO VAR'''
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


def p_declaracion_if(p):
    '''declaracion : IF PARENTH_IZQ comparacion declaracion PARENTH_DER '''
    if p[3]:
        p[0] = p[5]


def p_declaracion_if_else(p):
    '''declaracion : IF PARENTH_IZQ comparacion declaracion PARENTH_DER
                    | IF PARENTH_IZQ comparacion declaracion PARENTH_DER COMA declaracion ELSE '''
    if p[3]:
        p[0] = p[5]
    else:
        if p[7] is not None:
            p[0] = p[7]


def p_declaracion_while(p):
    'declaracion : WHILE PARENTH_IZQ comparacion declaracion PARENTH_DER'
    while(p[3]):
        p[5];


##PROYECTO LENGUAJES, DEFINICION DE EXPRESIONES LAMBDA JAVA 8##

def p_empty(p):
    '''empty : '''
    p[0] = None


def p_expresion_interna(p):
    '''expresion_interna : TIPO VAR COMA expresion
    | TIPO VAR
    | VAR'''


parser = yacc.yacc()

while True:
    s = input('')
    parser.parse()



