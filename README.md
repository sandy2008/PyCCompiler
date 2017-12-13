# PyCCompiler A C-Compiler written in Python

语法分析器所用到的文法。

notice：首字母大写的除了ID外为非终结符，剩下的为终结符，ID表示标识符。

''''''''''''''''''''''''''''''''''''
'句子
''''''''''''''''''''''''''''''''''''
Sentence --> Include | Statement | Assignment | Control | Expression | Constant | FunctionStatement | FunctionCall //克林闭包


''''''''''''''''''''''''''''''''''''
'导入语句include
''''''''''''''''''''''''''''''''''''
Include --> #include < ID > | #include "ID"


''''''''''''''''''''''''''''''''''''
'声明语句
''''''''''''''''''''''''''''''''''''
Statement --> Type ID; | Type ID[ Constant ]; | Type ID[ Constant ] = { ConstantList };
Type --> int | float 
ConstantList --> ∑ | Constant ConstantRest
ConstantRest --> ∑ | ,Constant | ConstantRest
ConstantRest --> (,Constant)*


''''''''''''''''''''''''''''''''''''
'赋值语句
'''''''''''''''''''''''''''''''''''' 
Assignment --> ID = Expression;


''''''''''''''''''''''''''''''''''''
'控制语句
'''''''''''''''''''''''''''''''''''' 
Control --> IfControl | WhileControl | ForControl
IfElseControl --> IfControl ElseControl
IfControl --> if( Expression ){ Sentence }
ElseControl --> ∑ | else{ Sentence } 
WhileControl --> while( Expression ){ Sentence }
ForControl --> for( Assignment; Expression; Expression ){ Sentence }


''''''''''''''''''''''''''''''''''''
'表达式
'''''''''''''''''''''''''''''''''''' 
Expression --> ( Expression ) | Expression Operator Expression | SingleOperator Expression | ArrayIndex | Constant
ArrayIndex --> ID[ Constant ]
SingleOperator --> ! | ++ | --
Operate --> + | - | * | / | ++ | -- | > | < | >= | <= | &


''''''''''''''''''''''''''''''''''''
'常量
''''''''''''''''''''''''''''''''''''
Constant --> Num | String
Num --> [0-9] | [1-9][0-9]+    //正则表达式表示
String --> [a-zA-Z0-9\n%:,.]+  //正则表达式表示


''''''''''''''''''''''''''''''''''''
'函数声明、调用
''''''''''''''''''''''''''''''''''''
FunctionStatement --> Type FunctionName( StateParameterList ){ Sentence }
StateParameterList --> ∑ | Parameter ParameterRest
Parameter --> Type ID
ParameterRest --> ∑ | ,Parameter | ParameterRest
Type --> int | float | char | double

FunctionCall --> ID( CallParameterList );
CallParameterList --> ∑ | ID ParameterRest
ParameterRest --> ∑ | ,ID | ParameterRest


''''''''''''''''''''''''''''''''''''
'return语句
''''''''''''''''''''''''''''''''''''
Return --> return Expresstion;