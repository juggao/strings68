// A simple syntax-directed translator for a simple language

grammar strings68;

// Root non-terminal symbol
// A program is a bunch of declarations followed by a bunch of statements
// The Java code outputs the necessary NASM code around these declarations

program       : 
              declaration*
              statement*
              ;

// Parse rule for variable declarations

declaration   : 
              STRING NAME SEMICOLON 
              ;

// Parse rule for statements

statement      : 
               ifstmt 
             | loopstmt
             | printstmt 
             | assignstmt 
             | toupperstmt
             | tolowerstmt
             | shiftlstmt
             | shiftrstmt
             | breakstmt
               ;

// Parse rule for if statements

ifstmt      : 
            IF LPAREN identifier EQUAL identifier RPAREN
            statement*
            ENDIF
          | IF LPAREN identifier EQUAL STRINGCHARS RPAREN
            statement* 
            ENDIF  
            ;

loopstmt      : 
            LOOP 
            statement* 
            ENDLOOP
            ;

breakstmt     :
            BREAK SEMICOLON
            ;

// Parse rule for print statements

printstmt      : 
               PRINT term SEMICOLON
               ;
toupperstmt    : 
               TOUPPER term SEMICOLON
               ;
tolowerstmt      : 
               TOLOWER term SEMICOLON
               ;              
shiftlstmt      : 
               SHIFTL term SEMICOLON
               ;     
shiftrstmt      : 
               SHIFTR term SEMICOLON
               ;     

// Parse rule for assignment statements

assignstmt      : 
                NAME ASSIGN expression SEMICOLON
              | NAME ASSIGN LPAREN expression RPAREN SEMICOLON
                ;

// Parse rule for expressions

expression      : 
                term
              | 
                term PLUS term 
                ;

// Parse rule for terms

term          : 
              identifier
            | string
            | stringchars
              ;

// Parse rule for identifiers

identifier   : NAME ;
stringchars  : STRINGCHARS ; 
string       : STRING;

// Reserved Keywords
////////////////////////////////

IF: 'if';
ENDIF: 'endif';
PRINT: 'print';
STRING: 'string';
TOLOWER: 'tolower';
TOUPPER: 'toupper';
LOOP:  'loop';
ENDLOOP: 'endloop';
BREAK:  'break';
CONTINUE: 'continue';
SHIFTL: 'shiftl'; 
SHIFTR: 'shiftr';

// Operators
PLUS: '+';
EQUAL: '==';
ASSIGN: '=';
NOTEQUAL: '!=';

// Semicolon and parentheses
SEMICOLON: ';';
LPAREN: '(';
RPAREN: ')';
Q:  '"';

// Variable names
NAME: [a-zA-Z0-9_]+;   

//STRINGCHARS: '\'' ( '$' '\''? | ~('$' | '\'') )* '\'' ;
STRINGCHARS
  : UnterminatedStringLiteral '"'
  ;

UnterminatedStringLiteral
  : '"' (~["\\\r\n] | '\\' (. | EOF))*
  ;


// Ignore all white spaces 
// WS: [ \t\r\n]+ -> skip ;
WHITESPACE          : (' ' | '\t')+  -> skip;
NEWLINE             : ('\r'? '\n' | '\r')+ -> skip;
COMMENT             : '#' ~[\r\n]* '\r'? '\n' -> skip ;
