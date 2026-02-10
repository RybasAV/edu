class StringVar:
    def __init__(self, string):
        self.string = string

    def set(self, index, simbol):
        new_string = self.string[:index] + simbol + self.string[index:]
        return new_string

    def get(self, start_index, end_index):
        new_string = self.string[start_index:end_index]
        return new_string


s = "Hello world!"
a = StringVar(s)
print(a.set(5, "!"))
print(a.get(1, 9))
