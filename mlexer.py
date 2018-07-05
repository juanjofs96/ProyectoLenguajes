import ply.lex as lex

tokens=['IDENTIDAD','MAS','MENOS','DIVIDE','POR','MODULO','POTENCIA','Y','OINCL','OEXCL','NEGADO','IGUAL','IDENTICO','DIFERENTE','MAYOR',
        'IF', 'ELSE', 'ELSEIF', 'WHILE', 'PARENTH_IZQ', 'PARENTH_DER', 'LLAVE_IZQ','LLAVE_DER', 'DO', 'FOR', 'FOREACH', 'BREAK',
        'CONTINUE', 'SWITCH', 'CASE', 'DECLARE', 'RETURN', 'REQUIRE', 'INCLUDE', 'GOTO','VAR','OR','AND']
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


def t_VAR(p):
    r'\$[^0-9]+[A-Za-z_0-9]+'
    p.type = reserved.get(p.value, 'VAR')
    return p


def t_error(t):
    print(t)

lex.lex()

lex.input("if+*else ifelse $_animal")
while True:
    tok = lex.token()
    if not tok:
        t_error(tok)
        break
    print(tok.value)


