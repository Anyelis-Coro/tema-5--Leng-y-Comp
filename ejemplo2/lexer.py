import ply.lex as lex

tokens = (
    'AUTO',
    'IFACE',
    'DIRECTIVE',
    'IP',
    'INTERFACE',
    'METHOD',
    'FAMILY',
    'NEWLINE'
)

# Reglas con precedencia para palabras clave
def t_AUTO(t):
    r'auto\b'
    return t

def t_IFACE(t):
    r'iface\b'
    return t

def t_DIRECTIVE(t):
    r'address|netmask|gateway'
    return t

def t_METHOD(t):
    r'static|dhcp'
    return t

def t_FAMILY(t):
    r'inet\b|inet6\b'
    return t

def t_IP(t):
    r'\d+\.\d+\.\d+\.\d+'
    return t

def t_INTERFACE(t):
    r'[a-zA-Z0-9_-]+'
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Error léxico en línea {t.lineno}: '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == "__main__":
    data = "auto eth0\niface eth0 inet static"
    lexer.input(data)
    for tok in lexer:
        print(tok)