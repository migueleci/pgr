grammar SCCP;
sys: 	(decl)? 'begin' (proc)+ 'end' ;
decl:	(var)+ ;
var:	'var' (ID)+ tname ;
tname:	'Int' | 'Bool' ;
proc: 	'tell' '(' const ')'
	|	'ask' ('<' loc '>')? const '->' proc
	|	proc '||' proc
	| 	'[' proc ']_' INT
	;
const: 	BOOL
	|	ID
	| 	expr
	| 	const 'and' const
	;
loc: 	INT ('.' INT)+ ;
expr:	ID op ( ID | INT ) ;
op:		'>' | '<' | '=' | '>=' | '<=' ;
BOOL: 	'true' | 'false' ;
INT: 	[0-9]+ ;
ID:		[A-Z] [A-Z0-9]* ;
WS  :   [ \t\r\n]+ -> skip ;
