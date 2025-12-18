from lark import Transformer

class ConfigTransformer(Transformer):
    def __init__(self):
        self.constants = {}

    def start(self, items):
        return items

    # ===== ТЕРМИНАЛЫ =====

    def BIN_NUMBER(self, token):
        return int(token[2:], 2)

    def STRING(self, token):
        return token[1:-1]

    def NAME(self, token):
        return str(token)

    # ===== ПРАВИЛА =====

    def number(self, items):
        return items[0]

    def string(self, items):
        return items[0]

    def const_ref(self, items):
        name = items[0]
        return self.constants[name]

    def pair(self, items):
        return (items[0], items[1])

    def dict(self, items):
        return dict(items)

    def const_decl(self, items):
        name = items[0]
        value = items[2]
        self.constants[name] = value
        return (name, value)

    def COMMENT(self, _):
        return None
