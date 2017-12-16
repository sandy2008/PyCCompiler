from token import *

class Lexer(object):
    '''词法分析器'''
    content = None
    tokens = []

    def __init__(self, content):
        self.tokens = []
        self.content = content

    # 判断是否是空白字符
    def is_blank(self, index):
        return self.content[index] == ' ' or self.content[index] == '\t' or self.content[index] == '\n' or self.content[index] == '\r'

    # 跳过空白字符
    def skip_blank(self, index):
        while index < len(self.content) and self.is_blank(index):
            index += 1
        return index

    # 打印
    def print_log(self, style, value):
        print ('(%s, %s)' % (style, value))

    # 判断是否是关键字
    def is_keyword(self, value):
        for item in keywords:
            if value in item:
                return True
        return False

    # 词法分析主程序
    def main(self):
        i = 0
        while i < len(self.content):
            i = self.skip_blank(i)
            # 如果是引入头文件，还有一种可能是16进制数，这里先不判断
            if self.content[i] == '#':
                #self.print_log( '分隔符', self.content[ i ] )
                self.tokens.append(Token(4, self.content[i]))
                i = self.skip_blank(i + 1)
                # 分析这一引入头文件
                while i < len(self.content):
                    # 匹配"include"
                    if re.match('include', self.content[i:]):
                        # self.print_log( '关键字', 'include' )
                        self.tokens.append(Token(0, 'include'))
                        i = self.skip_blank(i + 7)
                    # 匹配"或者<
                    elif self.content[i] == '\"' or self.content[i] == '<':
                        # self.print_log( '分隔符', self.content[ i ] )
                        self.tokens.append(Token(4, self.content[i]))
                        i = self.skip_blank(i + 1)
                        close_flag = '\"' if self.content[i] == '\"' else '>'
                        # 找到include的头文件
                        lib = ''
                        while self.content[i] != close_flag:
                            lib += self.content[i]
                            i += 1
                        # self.print_log( '标识符', lib )
                        self.tokens.append(Token(1, lib))
                        # 跳出循环后，很显然找到close_flog
                        # self.print_log( '分隔符', close_flag )
                        self.tokens.append(Token(4, close_flag))
                        i = self.skip_blank(i + 1)
                        break
                    else:
                        print ('include error!')
                        exit()
            # 如果是字母或者是以下划线开头
            elif self.content[i].isalpha() or self.content[i] == '_':
                # 找到该字符串
                temp = ''
                while i < len(self.content) and (self.content[i].isalpha() or self.content[i] == '_' or self.content[i].isdigit()):
                    temp += self.content[i]
                    i += 1
                # 判断该字符串
                if self.is_keyword(temp):
                    # self.print_log( '关键字', temp )
                    self.tokens.append(Token(0, temp))
                else:
                    # self.print_log( '标识符', temp )
                    self.tokens.append(Token(1, temp))
                i = self.skip_blank(i)
            # 如果是数字开头
            elif self.content[i].isdigit():
                temp = ''
                while i < len(self.content):
                    if self.content[i].isdigit() or (self.content[i] == '.' and self.content[i + 1].isdigit()):
                        temp += self.content[i]
                        i += 1
                    elif not self.content[i].isdigit():
                        if self.content[i] == '.':
                            print ('float number error!')
                            exit()
                        else:
                            break
                # self.print_log( '常量' , temp )
                self.tokens.append(Token(2, temp))
                i = self.skip_blank(i)
            # 如果是分隔符
            elif self.content[i] in delimiters:
                # self.print_log( '分隔符', self.content[ i ] )
                self.tokens.append(Token(4, self.content[i]))
                # 如果是字符串常量
                if self.content[i] == '\"':
                    i += 1
                    temp = ''
                    while i < len(self.content):
                        if self.content[i] != '\"':
                            temp += self.content[i]
                            i += 1
                        else:
                            break
                    else:
                        print ('error:lack of \"')
                        exit()
                    # self.print_log( '常量' , temp )
                    self.tokens.append(Token(5, temp))
                    # self.print_log( '分隔符' , '\"' )
                    self.tokens.append(Token(4, '\"'))
                i = self.skip_blank(i + 1)
            # 如果是运算符
            elif self.content[i] in operators:
                # 如果是++或者--
                if (self.content[i] == '+' or self.content[i] == '-') and self.content[i + 1] == self.content[i]:
                    # self.print_log( '运算符', self.content[ i ] * 2 )
                    self.tokens.append(Token(3, self.content[i] * 2))
                    i = self.skip_blank(i + 2)
                # 如果是>=或者<=
                elif (self.content[i] == '>' or self.content[i] == '<') and self.content[i + 1] == '=':
                    # self.print_log( '运算符', self.content[ i ] + '=' )
                    self.tokens.append(Token(3, self.content[i] + '='))
                    i = self.skip_blank(i + 2)
                # 其他
                else:
                    # self.print_log( '运算符', self.content[ i ] )
                    self.tokens.append(Token(3, self.content[i]))
                    i = self.skip_blank(i + 1)

        for token in self.tokens:
          print ('(%s, %s)' % (token.type, token.value))
