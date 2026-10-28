# from agent import Tinyagent

# agent = Tinyagent()
# print(agent.run("what is the weather like today"))

#----------------------------------------------------------------------

# import json 
# import urllib.request

# data = json.dumps(
#     {
#     "model" : "gemma4:e4b",
#     "messages" : [{"role" : "user" , "content" : "Hi, what is the weather in chicago today ? "}]
#     }
# ).encode("utf-8")

# #post request 
# req = urllib.request.Request(
#     url = "http://localhost:11434/v1/chat/completions",
#     data = data,
#     headers = {"Content-Type" : "application/json"}

# )

# #parse response
# with urllib.request.urlopen(req) as response :
#     result = json.loads(response.read())

# print(result['choices'][0])


#----------------------------------------------------------------------

# from llm import LLM
# from dataclasses import asdict
# import json
# llm = LLM(model = "gemma4:e4b" , think = False)
# response = llm.generate([{"role" : "user" , "content" : " hi , how is life ? "}])
# print(json.dumps(asdict(response), indent=2))



#----------------------------------------------------------------------

# from llm import LLM
# from agent import Tinyagent


# llm = LLM(model="gemma4:e4b", think=False)
# agent = Tinyagent(llm=llm)
# response_text = agent.run("What is the capital of France?")
# print("Agent output:\n", response_text)

# print("\nRecorded trajectory runs:")
# for run in agent.trajectory.runs:
#     print(f"Query: {run['query']}")
#     for i, step in enumerate(run["steps"]):
#         print(f"  Step {i + 1}: answer = {step.answer}")
