class Token:
    '''Analyze the Tokens'''
    def __init__(self, type_index, value):
        self.type = DETAIL_TOKEN_STYLE[
            value] if type_index == 0 or type_index == 3 or type_index == 4 else TOKEN_STYLE[type_index]
        self.value = value
