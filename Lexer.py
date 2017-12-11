class Lexer:
    '''Word Analysis'''

    def __init__(self):
        self.tokens = []

    def is_blank(self, index):
        return content[index] == ' ' or content[index] == '\t' or content[index] == '\n' or content[index] == '\r'

    # Skip Blank
    def skip_blank(self, index):
        while index < len(content) and self.is_blank(index):
            index = index + 1
        return index

    def print_log(self, style, value):
        print('(%s, %s)' % (style, value))

    def is_keyword(self, value):
        for item in keywords:
            if value in item:
                return True
        return False

    # Main Code of Lexer
    def main(self):
        i = 0
        while i < len(content):
            i = self.skip_blank(i)
        if content[i] == '#':
            self.tokens.append(Token(4, content[i]))
            i = self.skip_blank(i + 1)
            # head files
            while i < len(content):
                # match "include"
                if re.match('include', content[i:]):
                    self.tokens.append(Token(0, 'include'))
                    i = self.skip_blank(i + 7)
                # match " or v
                elif content[i] == '\"' or content[i] == '<':
                    self.tokens.append(Token(4, content[i]))
                    i = self.skip_blank(i + 1)
                    close_string = '\"' if content[i] == '\"' else '>'
                    # find included lib
                    lib = ''
                    while content[i] != close_string:
                        lib += content[i]
                        i += 1
                    self.tokens.append(Token(4, close_string))
                    i = self.skip_blank(i + 1)
                    break
                else:
                    print ('include error!')
                    exit()

        #if content begins with letter or down slash
        elif content[i].isalpha() or content[i] == '_':
            #find the string
