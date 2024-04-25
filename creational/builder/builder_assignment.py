class CodeBuilder:
    def __init__(self, root_name):
        # todo
        self.pattern = "class " + str(root_name) + ":\n"
        self.ori_pattern = self.pattern
        self.nullstr = " " * 2 + "pass"
        self.is_null = True
        self.pattern += self.nullstr

    def add_field(self, types, name):
        if self.is_null:
            self.pattern = self.ori_pattern
            self.pattern += " " * 2 + "def __init__(self):\n"
            self.is_null = False
        self.pattern += " " * 4 + "self." + str(types) + " = " + str(name) + "\n"
        return self
        # todo

    def __str__(self):
        # todo
        return self.pattern


cb = CodeBuilder("Person").add_field("name", '""').add_field("age", 0)
print(cb)
