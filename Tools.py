from langchain_community.tools import tool


@tool("Calculate")
def calculate(equation):
    """ Useful for solving math equations """

    return eval(equation)

@tool("Authors")
def authors():
    """Returns the names of the authors you have to credit for your work"""
    return "Noah Kohrs and Thibaut Haberer"