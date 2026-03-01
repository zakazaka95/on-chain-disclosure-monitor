# v0.1.0
# { "Depends": "py-genlayer:latest" }

from genlayer import *


class DisclosureVerifier(gl.Contract):
    statement: str
    required_keyword: str
    result: bool

    def __init__(self, statement: str, required_keyword: str):
        self.statement = statement
        self.required_keyword = required_keyword
        self.result = False

    @gl.public.view
    def get_inputs(self) -> dict[str, str]:
        return {
            "statement": self.statement,
            "required_keyword": self.required_keyword,
        }

    @gl.public.view
    def get_result(self) -> bool:
        return self.result

    @gl.public.write
    def resolve(self) -> None:
        self.result = self.required_keyword.lower() in self.statement.lower()
