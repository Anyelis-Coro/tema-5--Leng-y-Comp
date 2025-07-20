from antlr4 import *
from InterfacesLexer import InterfacesLexer
from InterfacesParser import InterfacesParser

def clean_input(text):
    # Elimina espacios iniciales/finales y normaliza saltos de línea
    return '\n'.join(line.strip() for line in text.split('\n') if line.strip())

def parse_interfaces(input_text):
    cleaned_input = clean_input(input_text)
    input_stream = InputStream(cleaned_input)
    lexer = InterfacesLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = InterfacesParser(stream)
    tree = parser.file_()
    print(tree.toStringTree(recog=parser))

if __name__ == "__main__":
    test_config = """
    auto eth0
    iface eth0 inet static
        address 192.168.1.2
    """
    parse_interfaces(test_config)