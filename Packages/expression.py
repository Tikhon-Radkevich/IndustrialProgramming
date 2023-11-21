class Expression:
    def __init__(self, title: str, expression: str, args: dict):
        self.title = title
        self.expression = expression
        self.args = args
        self.converted_expression = None
        self.result = None

    # reset custom ==
    def __eq__(self, other):
        return (self.title == other.title and self.expression == other.expression and
                self.args == other.args and self.result == other.result)

    def calculate(self):
        try:
            converted_expression = self.expression
            for key, value in self.args.items():
                converted_expression = converted_expression.replace(str(key), str(value))

            self.converted_expression = converted_expression
            self.result = eval(self.converted_expression)
        except Exception as e:
            raise ValueError(f"Error calculating the \n{self.expression}: \n{e}")

    def get_description(self):
        description = f"{'#'*15} {self.title} {'#'*15}\n\n"
        description += f"Original Expression: {self.expression}\n"
        description += "Arguments:\n"
        for key, value in self.args.items():
            description += f"  {key}: {value}\n"
        description += f"Converted Expression: {self.converted_expression}\n"
        description += f"Result: {self.result}\n"
        return description

    def get_dict(self) -> dict:
        data = {
            self.title: {
                "expression": self.converted_expression,
                "args": self.args,
                "result": self.result
            }
        }
        return data
