import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from ejemplo3.antlr_runner import parse as antlr_parse
    from ejemplo2.parser import parser as ply_parse
    from lark_parser import parse as lark_parse
except ImportError as e:
    print("ERROR: Faltan archivos. Verifica que:")
    print("1. Los parsers estén generados (ANTLR)")
    print("2. Los módulos estén en las carpetas correctas")
    raise e

# Resto del código original...

def run_benchmark():
    with open("ejemplo3/test_input.txt") as f:
        config = f.read()
    
    tools = {
        'ANTLR': lambda: antlr_parse(config),
        'PLY': lambda: ply_parse.parse(config),
        'Lark': lambda: lark_parse(config)
    }
    
    results = {}
    for name, parser in tools.items():
        time = timeit.timeit(parser, number=100)
        results[name] = time
    
    plt.bar(results.keys(), results.values())
    plt.savefig('benchmark.png')

if __name__ == "__main__":
    run_benchmark()