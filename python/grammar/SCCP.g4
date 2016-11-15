grammar SCCP;
sys: 	(decl)? 'begin' (line)+ 'end' ;
decl:	(var)+ ;
var:	'var' (ID)+ tname ;
tname:	'Int' | 'Bool' ;
line:	proc '.' ;
proc: 	'tell' '(' const ')'					# tell
	|	'ask' ('<' loc '>')? const '->' proc	# ask
	|	proc '||' proc							# parallel
	| 	'[' proc ']_' INT 						# procloc
	;
const: 	BOOL 									# bool
	|	ID										# id
	| 	expr 									# cexpr
	| 	const 'and' const 						# and
	;

loc: 	INT ('.' INT)+ ;
expr:	ID op ( ID | INT ) ;
op:		'>' | '<' | '=' | '>=' | '<=' ;
BOOL: 	'true' | 'false' ;
INT: 	[0-9]+ ;
ID:		[A-Z] [A-Z0-9]* ;
WS  :   [ \t\r\n]+ -> skip ;
