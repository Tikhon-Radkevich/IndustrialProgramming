class Expression:
    def __init__(self, title: str, expression: str, args: dict):
        self.title = title
        self.expression = expression
        self.args = args
        self.converted_expression = None
        self.result = None

    def calculate(self):
        converted_expression = self.expression
        for key, value in self.args.items():
            converted_expression = converted_expression.replace(str(key), str(value))

        self.converted_expression = converted_expression
        self.result = eval(self.converted_expression)

    def get_description(self):
        description = f"{'#'*15} {self.title} {'#'*15}\n\n"
        description += f"Original Expression: {self.expression}\n"
        description += "Arguments:\n"
        for key, value in self.args.items():
            description += f"  {key}: {value}\n"
        description += f"Converted Expression: {self.converted_expression}\n"
        description += f"Result: {self.result}\n"
        return description
