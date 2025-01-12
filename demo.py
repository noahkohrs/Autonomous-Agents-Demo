import os
from localllm import phi4
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
from Tools import calculate, authors
from langchain_openai import ChatOpenAI

## Required by CrewAI, even if we don't use open ai apis
os.environ["OPENAI_API_KEY"] = "__NONE__"

llm = phi4()


print("## Welcome to the Math Whiz")
math_input = input("What is your math equation: ")

math_agent = Agent(
    role="Math Magician",
    goal="You are able to evaluate any math expression",
    backstory="YOU ARE A MATH WHIZ. Your friends know you to think of everything in a mathematical way. Little did they know you have a secret weapon, the ability to evaluate any math expression using the Calculate tool. You use this tool for anything that involves numbers.",
    verbose=True,
    tools=[calculate],
    llm=llm
)

writer = Agent(
    role="Writer",
    goal="Craft compelling explanations based from results of math equations. The explainations must detail every single steps of the reasonning. Assume you are writing to someone that doesn't know anything about the subject.",
    backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.  
    You transform complex concepts into compelling narratives.
    """,
    verbose=True,
    tools=[authors],
    llm=llm
)

task1 = Task(
    description=f"{math_input}",
    expected_output="Give full details in bullet points.",
    agent=math_agent
)

task2 = Task(
    description="""using the insights provided, explain in great detail how the equation and result 
    were formed in a structured Markdown document. Don't forget to include the authors of the tools you used! You can see them in the Authors tool.""",
    expected_output="""Explain in great detail and save in markdown.  Do no add the triple tick marks at the 
                    beginning or end of the file.  Also don't say what type it is in the first line. The output should be the whole detailed explanation, not a summary.""",
    output_file="markdown/math.md",
    agent=writer
)

crew = Crew(
    agents=[math_agent, writer],
    tasks=[task1, task2],
    process=Process.sequential,
    verbose=2
)

result = crew.kickoff()

print(result)








