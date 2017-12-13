# PyCCompiler A C-Compiler written in Python

语法分析器所用到的文法。

#notice：首字母大写的除了ID外为非终结符，剩下的为终结符，ID表示标识符。

#句子

Sentence --> Include | Statement | Assignment | Control | Expression | Constant | FunctionStatement | FunctionCall //克林闭包 <br>


#导入语句include

Include --> #include < ID > | #include "ID" <br>


#声明语句

Statement --> Type ID; | Type ID[ Constant ]; | Type ID[ Constant ] = { ConstantList }; <br>
Type --> int | float  <br>
ConstantList --> ∑ | Constant ConstantRest <br>
ConstantRest --> ∑ | ,Constant | ConstantRest <br>
ConstantRest --> (,Constant)* <br>


#赋值语句
 
Assignment --> ID = Expression; <br>


#控制语句
 
Control --> IfControl | WhileControl | ForControl <br>
IfElseControl --> IfControl ElseControl <br>
IfControl --> if( Expression ){ Sentence } <br>
ElseControl --> ∑ | else{ Sentence }  <br>
WhileControl --> while( Expression ){ Sentence } <br>
ForControl --> for( Assignment; Expression; Expression ){ Sentence }


###表达式
 
Expression --> ( Expression ) | Expression Operator Expression | SingleOperator Expression | ArrayIndex | Constant <br>
ArrayIndex --> ID[ Constant ] <br>
SingleOperator --> ! | ++ | -- <br>
Operate --> + | - | * | / | ++ | -- | > | < | >= | <= | & <br>


#常量

Constant --> Num | String <br>
Num --> [0-9] | [1-9][0-9]+    //正则表达式表示 <br>
String --> [a-zA-Z0-9\n%:,.]+  //正则表达式表示 <br>


#函数声明、调用

FunctionStatement --> Type FunctionName( StateParameterList ){ Sentence } <br>
StateParameterList --> ∑ | Parameter ParameterRest <br>
Parameter --> Type ID <br>
ParameterRest --> ∑ | ,Parameter | ParameterRest <br>
Type --> int | float | char | double <br> <br>

FunctionCall --> ID( CallParameterList ); <br>
CallParameterList --> ∑ | ID ParameterRest <br>
ParameterRest --> ∑ | ,ID | ParameterRest <br>



#return语句

Return --> return Expresstion; <br>