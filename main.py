'''
A Simple C-Compiler based in Python

'''

import re
import sys
import getopt

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

class Token:
    def __init__(self, type_index, value):
        self.type = DETAIL_TOKEN_STYLE[
            value] if type_index == 0 or type_index == 3 or type_index == 4 else TOKEN_STYLE[type_index]
        self.value = value

class Lexer:
    '''Word Analysis'''
    def __init__(self):
        self.tokens = []

    def is_blank(self, index):
        return content[index] == ' ' or content[index] == '\t' or content[index] == '\n' or content[index] == '\r'

    #Skip Blank
    def skip_blank(self, index):
        while index < len(content) and self.is_blank(index):
            index = index + 1
        return index

    def print_log(self, style, value):
        print ('(%s, %s)' % (style, value))

    def is_keyword(self, value):
        for item in keywords:
            if value in item:
                return True
        return False

    #Main Code of Lexer
    def main(self):
        i = 0
        while i < len(content):
            i = self.skip_blank(i)
        if content[i] == '#':
            self.tokens.append(Token(4, content[i]))
            i = self.skip_blank(i + 1)
            #head files
            while i<len(content):
                #match "include"
                if re.match('include',content[i:]):
                    self.tokens.append(Token(0,'include'))
                    i = self.skip_blank(i + 7)
                #match " or v
                elif content[i] == '\"' or  content[i] == '<':
                    self.tokens.append(Token(4,content[i]))
                    i = self.skip_blank(i + 1)
                    close_flag 