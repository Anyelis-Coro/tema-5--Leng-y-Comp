from lark import Lark, Transformer

grammar = """
    start: (auto | iface)+
    auto: "auto" CNAME
    iface: "iface" CNAME family method config_line+
    config_line: directive ip_address
    family: "inet" | "inet6"
    method: "static" | "dhcp"
    directive: "address" | "netmask" | "gateway"
    ip_address: /\d+\.\d+\.\d+\.\d+/
    CNAME: /[a-zA-Z0-9_-]+/
    %ignore " "
    %ignore "\t"
    %ignore "\n"
"""

class TreeToDict(Transformer):
    def auto(self, items):
        return ('auto', str(items[0]))
    
    def iface(self, items):
        return ('iface', items[0], items[1], items[2], items[3:])

parser = Lark(grammar, parser='lalr', transformer=TreeToDict())

def parse(data):
    return parser.parse(data)

# Ejemplo de uso
if __name__ == "__main__":
    data = """
    auto eth0
    iface eth0 inet static
        address 192.168.1.2
        netmask 255.255.255.0
    """
    print(parse(data))