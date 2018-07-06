import mlexer
import ply.yacc as yacc


tokens = mlexer.tokens

precedence = (
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDE'),
    ('right', 'UMINUS'),            # Unary minus operator
)

def p_expresion(p):
    '''expresion : termino
    | expresion MAS termino
    | expresion MENOS termino'''



def p_termino(p):
    '''termino : factor
    | termino POR factor
    | termino DIVIDE factor'''


def p_factor(p):
    '''factor : NUMBER
    | VAR
    | PARENTH_IZQ expresion PARENTH_DER'''


def p_asignar(p):
    '''asignar : VAR IGUAL expresion'''
    vars[p[1]] = p[3]


def p_expr_suma(p):
    '''expr_suma : expresion MAS termino'''

    p[0] = p[1] + p[3]


def p_expr_resta(p):
    '''expr_resta : expresion MENOS termino'''
    p[0] = p[1] - p[3]


def p_term_mult(p):
    '''term_mul : termino POR factor'''
    p[0] = p[1] * p[3]


def p_term_div(p):
    '''term_div : termino DIVIDE  factor'''

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


def p_error(p):
    print(p)


#PRIMER VAR DEBERIA SER UN TIPO
def p_expresion_interna(p):
    '''expresion_interna : TIPO VAR COMA expresion_interna
    | TIPO VAR
    | VAR'''

def p_expresion_lamda(p):
    '''expresion_lambda : expresion_interna IGUAL expresion_lambda
    | PARENTH_IZQ expresion interna PARENTH_DER LAMBDA expresion FIN'''


parser = yacc.yacc(debug = False, write_tables = False)

while True:
    try:
        s = input("int a = (int b, int c) -> b + c;")
    except EOFError:
        break
    parser.parse(s)
    print("Cool")