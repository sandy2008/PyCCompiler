'''
A Simple C-Compiler based in Python

For Help:
python main.py -h

For Lexical Result:
python main.py -s source.c -p

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
    '''Analyze the Tokens'''
    def __init__(self, type_index, value):
        self.type = DETAIL_TOKEN_STYLE[
            value] if type_index == 0 or type_index == 3 or type_index == 4 else TOKEN_STYLE[type_index]
        self.value = value



from token import *

class Lexer(object):
    '''Lexical Analyzer'''
    tokens = []

    def __init__(self):
        self.tokens = []

    # Blank String
    def is_blank(self, index):
        return content[index] == ' ' or content[index] == '\t' or content[index] == '\n' or content[index] == '\r'

    # Skip Blank String
    def skip_blank(self, index):
        while index < len(content) and self.is_blank(index):
            index += 1
        return index

    # Print
    def print_log(self, style, value):
        print ('(%s, %s)' % (style, value))

    # Judge Keyword
    def is_keyword(self, value):
        for item in keywords:
            if value in item:
                return True
        return False

    # Lexer Main
    def main(self):
        i = 0
        while i < len(content):
            i = self.skip_blank(i)
            # include file
            if content[i] == '#':
                self.tokens.append(Token(4, content[i]))
                i = self.skip_blank(i + 1)
                # analyze
                while i < len(content):
                    # find "include"
                    if re.match('include', content[i:]):
                        self.tokens.append(Token(0, 'include'))
                        i = self.skip_blank(i + 7)
                    # find " or <
                    elif content[i] == '\"' or content[i] == '<':
                        self.tokens.append(Token(4, content[i]))
                        i = self.skip_blank(i + 1)
                        close_flag = '\"' if content[i] == '\"' else '>'
                        # find include file
                        lib = ''
                        while content[i] != close_flag:
                            lib += content[i]
                            i += 1
                        self.tokens.append(Token(1, lib))
                        self.tokens.append(Token(4, close_flag))
                        i = self.skip_blank(i + 1)
                        break
                    else:
                        print ('include error!')
                        exit()

            elif content[i].isalpha() or content[i] == '_':
                # find string
                temp = ''
                while i < len(content) and (content[i].isalpha() or content[i] == '_' or content[i].isdigit()):
                    temp += content[i]
                    i += 1
                # analyze string
                if self.is_keyword(temp):
                    self.tokens.append(Token(0, temp))
                else:
                    self.tokens.append(Token(1, temp))
                i = self.skip_blank(i)
            # if digits
            elif content[i].isdigit():
                temp = ''
                while i < len(content):
                    if content[i].isdigit() or (content[i] == '.' and content[i + 1].isdigit()):
                        temp += content[i]
                        i += 1
                    elif not content[i].isdigit():
                        if content[i] == '.':
                            print ('float number error!')
                            exit()
                        else:
                            break
                self.tokens.append(Token(2, temp))
                i = self.skip_blank(i)
            # delimiters
            elif content[i] in delimiters:
                self.tokens.append(Token(4, content[i]))
                if content[i] == '\"':
                    i += 1
                    temp = ''
                    while i < len(content):
                        if content[i] != '\"':
                            temp += content[i]
                            i += 1
                        else:
                            break
                    else:
                        print ('error:lack of \"')
                        exit()
                    self.tokens.append(Token(5, temp))
                    self.tokens.append(Token(4, '\"'))
                i = self.skip_blank(i + 1)
            elif content[i] in operators:
                if (content[i] == '+' or content[i] == '-') and content[i + 1] == content[i]:
                    self.tokens.append(Token(3, content[i] * 2))
                    i = self.skip_blank(i + 2)
                # if >= or <=
                elif (content[i] == '>' or content[i] == '<') and content[i + 1] == '=':
                    self.tokens.append(Token(3, content[i] + '='))
                    i = self.skip_blank(i + 2)
                # else
                else:
                    self.tokens.append(Token(3, content[i]))
                    i = self.skip_blank(i + 1)

        for token in self.tokens:
          print ('(%s, %s)' % (token.type, token.value))


def lexer():
    lexer = Lexer()
    lexer.main()
    for token in lexer.tokens:
        print ('(%s, %s)' % (token.type, token.value))


if __name__ == '__main__':
    try:
        opts, argvs = getopt.getopt(sys.argv[1:], 's:lpah', ['help'])
    except:
        print (__doc__)
        exit()

    for opt, argv in opts:
        if opt in ['-h', '--h', '--help']:
            print (__doc__)
            exit()
        elif opt == '-s':
            file_name = argv.split('.')[0]
            source_file = open(argv, 'r')
            content = source_file.read()
        elif opt == '-l':
            lexer()

class SyntaxTreeNode(object):
    def __init__(self, value=None, _type=None, extra_info=None):
        self.valjue = value
        self.type = _type

        self.extra_info = extra_info
        self.father = None
        self.left = None
        self.right = None
        self.first_son = None
