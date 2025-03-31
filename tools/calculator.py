from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class CalculatorInput(BaseModel):
    operation: str = Field(..., description="Mathematical experssion to evaluate")

class calculator(BaseTool):
    name: str= "Calculator"
    description: str = """A calculator that can perform basic arithmetic operations like addition, subtraction, multiplication, and division, etc. The input should be a mathematical expression, e.g. '200*7' or '5000/2*10'"""
    args_schema: Type[BaseModel] = CalculatorInput

    def _run(self, operation:str) -> str:
        try:
            result = eval(operation)
            return str(result)
        except Exception as e:
            return f"Error evaluating expression: {e}"


# if __name__ == "__main__":
#     a= calculator()
#     print(a._run("200*7"))  # Example usage

