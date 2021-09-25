/*
 * Student's name: Nguyen Minh Loc
 * Student ID: 1852554
 */
grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
    language=Python3;
}
/*-------------------Program Structure-------------------*/
program: (class_decl)+ EOF;

typ: bool_typ | int_typ | float_typ | void_typ | string_typ;

//class_decl
class_decl: CLASS class_name (EXTENDS ID)? LP (class_member | constructor | main_method)* RP;
class_name: ID;
class_member: attribute_decl | method_decl | arr_decl | obj_decl;

//attribute_decl
attribute_decl: attribute_kw? typ ID (ASSIGN expr)? attribute_list SEMI;
attribute_kw: (STATIC | FINAL | STATIC FINAL | FINAL STATIC);
attribute_list: COMMA ID (ASSIGN expr)? attribute_list |  ;

//method_decl
method_decl: STATIC? typ ID LB para_list RB stmt_block;
para_list: typ ID (COMMA ID)* (SEMI typ ID (COMMA ID)*)* | ;

//special method
constructor: cstor_name LB para_list RB stmt_block_wo_return;
cstor_name: ID;
main_method: STATIC? void_typ 'main' LB RB stmt_block;

//arr_decl
arr_decl: arr_typ arr_list (ASSIGN arr_lit)? SEMI;
arr_list: ID (COMMA ID)*;

//object_decl
obj_decl: class_name obj_list SEMI;
obj_list: obj_name (COMMA obj_name)*;
obj_name: ID (ASSIGN ID)?;

/*-------------------Type-------------------*/

//primitive
int_typ: INT;
float_typ: FLOAT;
bool_typ: BOOLEAN;
string_typ: STRING;
void_typ: VOID;

//array
arr_typ: (INT | FLOAT | BOOLEAN | STRING) LSB INT_LIT RSB;

//class
class_typ: CLASS;

/*-------------------Expression-------------------*/
stmt: asm_stmt
		| if_stmt
		| for_stmt
		| break_stmt
		| continue_stmt
		| return_stmt
		| method_invo
		| invoke_stmt
		;

expr: NEW expr 
		| expr DOT expr (LB (expr (COMMA expr)* | ) RB)?
		| expr LSB expr RSB
		| (ADDOP | SUBOP) expr
		| NOT expr
		| expr CONCATENATION expr
		| expr (MULOP | I_DIV | F_DIV | MOD) expr
		| expr (ADDOP | SUBOP) expr
		| expr (AND | OR) expr
		| expr (EQUAL | NOT_EQUAL) expr
		| expr (LESS | GREATER | LESS_OR_EQUAL | GREATER_OR_EQUAL) expr
		| method_invo | asm_stmt | invoke_stmt | atom
		;
atom: LB expr RB
		|	literal
		| THIS
		|	ID
		;

/*-------------------Statement-------------------*/

//block statement
stmt_block: LP (attribute_decl | arr_decl | obj_decl | stmt)* RP;
stmt_block_wo_return: LP (attribute_decl|arr_decl|obj_decl|asm_stmt|if_stmt|for_stmt|break_stmt|continue_stmt|method_invo)* RP;

//assignment statement
asm_stmt: lhs INDEXOP expr SEMI;
lhs: ID | (ID|THIS) DOT (ID|ID LSB expr RSB) | ID LSB expr RSB;

//if statement
if_stmt: IF expr THEN (stmt|stmt_block) (ELSE (stmt|stmt_block))?;

//for statement
for_stmt: FOR scalar_var INDEXOP expr (TO|DOWNTO) expr DO (stmt|stmt_block);
scalar_var: ID;

//break statement
break_stmt: BREAK SEMI;

//continue statement
continue_stmt: CONTINUE SEMI;

//return statement
return_stmt: RETURN expr SEMI;

//method invocation statement
method_invo: (ID|THIS) DOT expr (LB (expr (COMMA expr)* | ) RB)? SEMI;

//invoke statement
invoke_stmt: ID LB argu_list? RB;
argu_list: expr (COMMA expr)*;

/*-------------------Lexical Structure-------------------*/

//comment
COMMENT_LINE   : '#' ~ [\r\n]* ('\r'? '\n' | EOF) -> skip ;
COMMENT_BLOCK  : '/*' .*? '*/' -> skip;

//keyword
BOOLEAN: 'boolean';
INT: 'int';
FLOAT: 'float';
VOID: 'void';
STRING: 'string';
NEW: 'new';
IF: 'if';
ELSE: 'else';
THEN: 'then';
CONTINUE: 'continue';
BREAK: 'break';
FOR: 'for';
DO: 'do';
TO: 'to';
DOWNTO: 'downto';
RETURN: 'return';
TRUE: 'true';
FALSE: 'false';
CLASS: 'class';
EXTENDS: 'extends';
STATIC: 'static';
FINAL: 'final';
NIL: 'nil';
THIS: 'this';

//operator
ADDOP: '+';
SUBOP: '-';
MULOP: '*';
I_DIV: '/';
F_DIV: '\\';
MOD: '%';
NOT_EQUAL: '!=';
EQUAL: '==';
LESS: '<'	;
GREATER: '>';
LESS_OR_EQUAL: '<=';
GREATER_OR_EQUAL: '>=';	
OR: '||';
AND: '&&';
NOT: '!';
CONCATENATION: '^';
ASSIGN: '=';
INDEXOP: ':=';

//separator
LB: '(';
RB: ')';
LP: '{';
RP: '}';
LSB: '[';
RSB: ']';
SEMI: ';';
COLON: ':';
COMMA: ',';
DOT: '.';

//literal
literal: FLOAT_LIT | INT_LIT | bool_lit | STRING_LIT | arr_lit;
INT_LIT: DIGIT+;
bool_lit: TRUE | FALSE;
arr_lit: LP arr_value (COMMA arr_value)* RP;
arr_value: (INT_LIT | FLOAT_LIT | bool_lit | STRING_LIT);
FLOAT_LIT: INT_LIT DECIMAL? EXPONENT?;

STRING_LIT: '"' CHAR* '"'
{
	temp = str(self.text)
	self.text = temp[1:-1]
};

//character set
fragment EXPONENT: [eE] (ADDOP | SUBOP)? DIGIT+;
fragment DECIMAL: DOT DIGIT*;
fragment LETTER: [a-zA-Z];
fragment UNDERSCORE: '_';
fragment DIGIT: [0-9];
fragment CHAR: ESC | ~ [\r\n\\"];
fragment ESC: '\\' ([btnfr"\\]);
fragment ILL_ESC: '\\' ~([btnfr"\\]) | ~'\\';
ID: (UNDERSCORE | LETTER) (UNDERSCORE | LETTER | DIGIT)*;
WS: [ \t\n\f\r] -> skip;

/*-------------------Lexical Errors-------------------*/

UNCLOSE_STRING: '"' CHAR* ([\r\nEOF] | ~'"')
{
	err_char = ['\r','\n',EOFError]
	if self.text[-1] in err_char:
		raise UncloseString(self.text[1:-1])
	else:
		raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE: '"' CHAR* ILL_ESC
{
	raise IllegalEscape(self.text[1:])
};
ERROR_CHAR: . 
{
	raise ErrorToken(self.text)
};