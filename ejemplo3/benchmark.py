import timeit
import matplotlib.pyplot as plt
from antlr_runner import parse_interfaces as antlr_parse
from ply_parser.parser import parser as ply_parser
from lark_parser import parse as lark_parse

# Configuración de prueba
config = """
auto eth0
iface eth0 inet static
    address 192.168.1.2
    netmask 255.255.255.0
"""

# Preparación
tools = {
    'ANTLR': ('antlr_parse(config)', globals()),
    'PLY': ('ply_parser.parse(config)', globals()),
    'Lark': ('lark_parse(config)', globals())
}

# Pruebas
results = {tool: [] for tool in tools}
for n in [10, 100, 1000]:  # Ejecuciones
    for tool, (cmd, ctx) in tools.items():
        t = timeit.timeit(cmd, number=n, globals=ctx)
        results[tool].append(t)

# Gráfica
plt.figure(figsize=(10, 5))
for tool in tools:
    plt.plot(['10', '100', '1000'], results[tool], label=tool, marker='o')

plt.title('Comparación de Parsers')
plt.xlabel('Número de ejecuciones')
plt.ylabel('Tiempo (segundos)')
plt.legend()
plt.grid()
plt.savefig('benchmark_results.png')
plt.show()