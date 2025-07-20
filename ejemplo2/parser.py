import ply.yacc as yacc
from lexer import tokens

def p_config(p):
    '''
    config : config_item
           | config config_item
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_config_item(p):
    '''
    config_item : auto
               | iface
    '''
    p[0] = p[1]

def p_auto(p):
    'auto : AUTO INTERFACE NEWLINE'
    p[0] = ('auto', p[2])

def p_iface(p):
    'iface : IFACE INTERFACE FAMILY METHOD NEWLINE directives'
    p[0] = ('iface', p[2], p[3], p[4], p[6])  # p[6] contiene las directivas

def p_directives(p):
    '''
    directives : directive NEWLINE
              | directives directive NEWLINE
    '''
    if len(p) == 3:  # Caso: single directive
        p[0] = [p[1]]
    else:  # Caso: multiple directives
        p[0] = p[1] + [p[2]]

def p_directive(p):
    'directive : DIRECTIVE IP'
    p[0] = (p[1], p[2])
    
def p_error(p):
    if p:
        print(f"Error de sintaxis en línea {p.lineno}: '{p.value}'")
    else:
        print("Error: Entrada incompleta")

parser = yacc.yacc()

if __name__ == "__main__":
    data = """
    auto eth0
    iface eth0 inet static
        address 192.168.1.2
        netmask 255.255.255.0
    """
    # Limpieza de datos
    data = '\n'.join(line.strip() for line in data.split('\n') if line.strip()) + '\n'
    result = parser.parse(data)
    print(result)