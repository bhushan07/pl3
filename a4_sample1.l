%{
#include<stdio.h>
#include "y.tab.h"
extern int yylval;
#define YYSTYPE int
%}
%option reentrant bison-bridge

%%
[0-9]+ {
          *yylval=atoi(yytext);
          return NUMBER;
       }
[\t] ;
[\n] return 0;
. return yytext[0];
%%
int yywrap(yyscan_t yyscanner)
{
return 1;
}

