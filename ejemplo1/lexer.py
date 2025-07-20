import ply.lex as lex

tokens = ('DIRECTIVE', 'IP', 'INTERFACE')
t_DIRECTIVE = r'address|netmask|gateway'
t_IP = r'\d+\.\d+\.\d+\.\d+'
t_INTERFACE = r'[a-zA-Z0-9_-]+'
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Error en línea {t.lineno}: Carácter inválido '{t.value[0]}'")

lexer = lex.lex()

if __name__ == "__main__":
    data = "eth0 192.168.1.1 address"
    lexer.input(data)
    for tok in lexer:
        print(tok)