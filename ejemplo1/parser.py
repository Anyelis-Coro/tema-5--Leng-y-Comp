import ply.yacc as yacc
from lexer import tokens

def p_interfaces(p):
    '''
    interfaces : interface
               | interfaces interface
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_interface(p):
    '''
    interface : AUTO INTERFACE_NAME
              | IFACE INTERFACE_NAME FAMILY METHOD config_lines
    '''
    if p[1] == 'auto':
        p[0] = ('auto', p[2])
    else:
        p[0] = ('iface', p[2], p[3], p[4], p[5])

def p_config_lines(p):
    '''
    config_lines : config_line
                | config_lines config_line
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_config_line(p):
    'config_line : DIRECTIVE IP_ADDRESS'
    p[0] = (p[1], p[2])

def p_error(p):
    if p:
        print(f"Error de sintaxis en línea {p.lineno}: Token inesperado '{p.value}' (Tipo: {p.type})")
    else:
        print("Error de sintaxis: entrada incompleta")

parser = yacc.yacc()