import ply.lex as lex

tokens = (
    'AUTO',
    'IFACE',
    'DIRECTIVE',
    'IP_ADDRESS',
    'INTERFACE_NAME',
    'METHOD',
    'FAMILY'
)

# Reglas con precedencia para palabras clave
def t_AUTO(t):
    r'auto\b'
    return t

def t_IFACE(t):
    r'iface\b'
    return t

def t_DIRECTIVE(t):
    r'address|netmask|gateway|dns-nameservers'
    return t

def t_METHOD(t):
    r'static|dhcp|manual'
    return t

def t_FAMILY(t):
    r'inet\b|inet6\b'
    return t

def t_IP_ADDRESS(t):
    r'\d+\.\d+\.\d+\.\d+'
    return t

def t_INTERFACE_NAME(t):
    r'[a-zA-Z0-9_-]+'
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Error léxico en línea {t.lineno}: Carácter inválido '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()