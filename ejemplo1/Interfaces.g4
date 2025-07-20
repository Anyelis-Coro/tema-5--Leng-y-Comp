grammar Interfaces;

file: (auto | iface)+ EOF;

auto: 'auto' ID NEWLINE;
iface: 'iface' ID FAMILY METHOD NEWLINE config+;
config: DIRECTIVE IP_ADDRESS NEWLINE;

DIRECTIVE: 'address' | 'netmask' | 'gateway';
FAMILY: 'inet' | 'inet6';
METHOD: 'static' | 'dhcp';
ID: [a-zA-Z0-9_-]+;
IP_ADDRESS: [0-9]+ '.' [0-9]+ '.' [0-9]+ '.' [0-9]+;
NEWLINE: '\r'? '\n';
WS: [ \t]+ -> skip;