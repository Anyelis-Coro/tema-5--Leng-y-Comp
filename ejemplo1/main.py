from lexer import lexer
from parser import parser

def preprocess(data):
    lines = []
    for line in data.split('\n'):
        stripped = line.strip()
        if stripped and not stripped.startswith('#'):
            lines.append(stripped)
    return '\n'.join(lines)

data = """
auto eth0
iface eth0 inet static
    address 192.168.1.2
    netmask 255.255.255.0
    gateway 192.168.1.1
"""

clean_data = preprocess(data)

print("=== Tokens reconocidos ===")
lexer.input(clean_data)
token_list = list(lexer)
for tok in token_list:
    print(f"Línea {tok.lineno}: {tok.type.ljust(15)} -> {tok.value}")

# Reiniciar el lexer para el parser
lexer.lineno = 1
lexer.input(clean_data)

print("\n=== Resultado del análisis ===")
try:
    result = parser.parse(lexer=lexer)
    print(result)
except Exception as e:
    print(f"Error durante el parsing: {e}")