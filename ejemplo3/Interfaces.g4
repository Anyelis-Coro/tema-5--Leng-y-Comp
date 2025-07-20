grammar Interfaces;

file_ : NEWLINE* (auto | iface)+ EOF;

auto: 'auto' ID NEWLINE;
iface: 'iface' ID FAMILY METHOD NEWLINE config+;
config: DIRECTIVE IP NEWLINE;

DIRECTIVE: 'address'|'netmask'|'gateway';
FAMILY: 'inet'|'inet6';
METHOD: 'static'|'dhcp';
ID: [a-zA-Z0-9_-]+;
IP: [0-9]+ '.' [0-9]+ '.' [0-9]+ '.' [0-9]+;
NEWLINE: '\r'? '\n';
WS: [ \t]+ -> skip;