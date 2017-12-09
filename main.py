'''
A Simple C-Compiler based in Python

'''

import re
import sys
import getopt

from Token import *
from Lexer import *

# Classifications of Token
from sqlalchemy import true

TOKEN_STYLE = ['KEY_WORD', 'IDENTIFIER', 'DIGIT_CONSTANT',
               'OPERATOR', 'SEPARATOR', 'STRING_CONSTANT']
# Detail Classificitaion
DETAIL_TOKEN_STYLE = {
    'include': 'INCLUDE', 'int': 'INT', 'float': 'FLOAT', 'char': 'CHAR', 'double': 'DOUBLE', 'for': 'FOR', 'if': 'IF', 'else': 'ELSE',
    'while': 'WHILE', 'do': 'DO', 'return': 'RETURN', '=': 'ASSIGN', '&': 'ADDRESS',
    '<': 'LT', '>': 'GT', '++': 'SELF_PLUS', '--': 'SELF_MINUS', '+': 'PLUS', '-': 'MINUS', '*': 'MUL', '/': 'DIV', '>=': 'GET', '<=': 'LET', '(': 'LL_BRACKET',
    ')': 'RL_BRACKET', '{': 'LB_BRACKET', '}': 'RB_BRACKET', '[': 'LM_BRACKET', ']': 'RM_BRACKET', ',': 'COMMA', '\"': 'DOUBLE_QUOTE',
    ';': 'SEMICOLON', '#': 'SHARP'}

#KeyWords
keywords = [['int', 'float', 'double', 'char', 'void'],
           ['if', 'for', 'while', 'do', 'else'], ['include', 'return']]

#Operators
operators = ['=', '&', '<', '>', '++', '--',
             '+', '-', '*', '/', '>=', '<=', '!=']

#delimiters
delimiters = ['(', ')', '{', '}', '[', ']', ',', '\"', ';']


file_name = None
content = None

def lexer():
    lexer = Lexer()
    lexer.main()
    for token in lexer.tokens:
        print ('(%s, %s)' % (token.type, token.value))


