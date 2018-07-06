import ply.lex as lex

tokens=['IDENTIDAD','MAS','MENOS','DIVIDE','POR','MODULO','POTENCIA','Y','OINCL','OEXCL','NEGADO','IGUAL','IDENTICO','DIFERENTE','MAYOR', 'MENOR',
        'PARENTH_IZQ', 'PARENTH_DER', 'LLAVE_IZQ','LLAVE_DER', 'DO', 'FOR', 'FOREACH', 'BREAK',
        'CONTINUE', 'REQUIRE', 'GOTO','VAR','OR','AND',
        'NUMBER', 'COMA', 'TIPO', 'LAMBDA','FIN', 'INT', 'STRING', 'DOUBLE', 'FLOAT']

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
t_COMA = r','
t_MAYOR=r'>'
t_MENOR=r'<'
t_PARENTH_IZQ = r'\('
t_PARENTH_DER = r'\)'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_DO = r'do'
t_FOR = r'for'
t_FOREACH = r'foreach'
t_BREAK = r'break'
t_CONTINUE = r'continue'
t_GOTO = r'goto'
t_OR = r'or'
t_AND = r'and'
t_LAMBDA = r'\->'
t_FIN =  r';'

reserved = {
    'if': 'IF',
    'then':'THEN',
    'while':'WHILE',
    'else if': 'ELSEIF',
    'int': 'INT',
    'String': 'STRING',
    'double': 'DOUBLE',
    'float': 'FLOAT'
}


def t_VAR(p):
    r'\w+'
    p.type = reserved.get(p.value, 'VAR')
    return p


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_INT(t):
    r'int'
    t.value = t.value
    return t


def t_STRING(t):
    r'String'
    t.value = t.value
    return t


def t_FLOAT(t):
    r'float'
    t.value = t.value
    return t


def t_DOUBLE(t):
    r'double'
    t.value = t.value
    return t


def t_error(t):
    print(t)


lex.lex()

lex.input("int resultado = (int valor1, int valor2) -> valor1+valor2;")

while True:
    tok = lex.token()
    if not tok:
        t_error(tok)
        break
    print(tok)


