import mlexer
import ply.yacc as yacc


tokens = mlexer.tokens

##PROYECTO LENGUAJES, DEFINICION DE EXPRESIONES LAMBDA JAVA 8##


def p_expr_general(p):
    '''expr_general : type VAR IGUAL expresion_lambda
    | VAR IGUAL expresion_lambda
    | expresion_lambda'''


def p_expresion_lamda(p):
    '''expresion_lambda : expresion_interna LAMBDA expresion FIN
    | PARENTH_IZQ expresion_interna PARENTH_DER LAMBDA expresion FIN'''


def p_expresion_interna(p):
    '''expresion_interna : type VAR COMA expresion_interna
    | type VAR
    | VAR'''


def p_expresion(p):
    '''expresion : expresion MAS termino
    | expresion MENOS termino
    | termino '''


def p_termino(p):
    '''termino : termino POR factor
    | termino DIVIDE factor
    | factor'''


def p_factor(p):
    '''factor : NUMBER
    | VAR
    | PARENTH_IZQ expresion PARENTH_DER'''


def p_type(p):
    '''type : STRING
    | INT
    | FLOAT
    | DOUBLE'''


def p_factor_variable(p):
    '''factor_variable : VAR'''
    if vars.has_key(p[1]):
        p[0] = vars[p[1]]
    else:
        print("Undefined Variable", p[1], "in line no.", p.lineno(1))


def p_empty(p):
    '''empty : '''
    p[0] = None


def p_error(p):
    print(p)


parser = yacc.yacc(debug = False, write_tables = False)

while True:
    try:
        s = input("Ingresa algo;")
    except EOFError:
        break
    parser.parse(s)
    print("Cool")