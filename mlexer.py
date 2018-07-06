import ply.lex as lex

tokens=['IDENTIDAD','MAS','MENOS','DIVIDE','POR','MODULO','POTENCIA','Y','OINCL','OEXCL','NEGADO','IGUAL','IDENTICO','DIFERENTE','MAYOR', 'MENOR',
        'IF', 'ELSE', 'ELSEIF', 'WHILE', 'PARENTH_IZQ', 'PARENTH_DER', 'LLAVE_IZQ','LLAVE_DER', 'DO', 'FOR', 'FOREACH', 'BREAK',
        'CONTINUE', 'SWITCH', 'CASE', 'DECLARE', 'RETURN', 'REQUIRE', 'INCLUDE', 'GOTO','VAR','OR','AND',
        'NUMBER', 'COMA', 'STRING', 'TIPO', 'LAMBDA','FIN']

t_ignore = ' \t'
t_MAS=r'\+'
t_MENOS=r'-'
t_POR=r'\*'
t_DIVIDE=r'/'
t_MODULO=r'%'
t_POTENCIA=r'\*\*'
t_Y=r'&'
t_OINCL=r'\|'
t_OEXCL=r'\^'
t_NEGADO=r'/~'
t_IGUAL=r'='
t_IDENTICO=r'=='
t_DIFERENTE=r'!='

t_TIPO=r'String|int|boolean|double|float|char|short|long'
t_COMA = r','

t_MAYOR=r'>'
t_MENOR=r'<'

t_IF = r'if'
t_ELSEIF = r'else\sif'
t_ELSE = r'else'
t_WHILE = r'\while'
t_PARENTH_IZQ = r'\('
t_PARENTH_DER = r'\)'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_DO = r'do'
t_FOR = r'for'
t_FOREACH = r'foreach'
t_BREAK = r'break'
t_CONTINUE = r'continue'
t_SWITCH = r'switch'
t_CASE = r'case'
t_DECLARE = r'declare'
t_RETURN = r'return'
t_INCLUDE = r'include'
t_GOTO = r'goto'
t_OR = r'or'
t_AND = r'and'
t_STRING = r'String'
t_LAMBDA = r'\->'
t_FIN =  r';'

reserved = {
    'if': 'IF',
    'then':'THEN',
    'while':'WHILE',
    'else if': 'ELSEIF',
    'include' : 'INCLUDE',
    'return': 'RETURN',
    'case': 'CASE',
    'switch': 'SWITCH'
}

#def t_TIPO(tipo):
 #   r'("String"|"int"|"boolean"|"double"|"float"|"long"|"short"|"char")'
#    return tipo

def t_VAR(p):
    r'\$[^0-9]+[A-Za-z_0-9]+'
    p.type = reserved.get(p.value, 'VAR')
    return p


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_error(t):
    print(t)


lex.lex()

lex.input(";")

while True:
    tok = lex.token()
    if not tok:
        t_error(tok)
        break
    print(tok)


