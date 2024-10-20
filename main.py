from utils.getllm import fetchllm
from utils.getprompts import get_prompts

from langchain_core.runnables import RunnableMap
from langchain_core.output_parsers import JsonOutputParser

import json
model=fetchllm("openai")

prompt=get_prompts("MCQ_Prompt")

chain=RunnableMap(
    {
        "topic_name":lambda x:x["topic_name"],
        "flag":lambda x:x["flag"]
    }
)|prompt|model|JsonOutputParser()

lists=["what is cloud computing?","Cloud vs. on-premise","cloud computing services","use cases of IaaS, PaaS, SaaS","FaaS","Cloud Deployment Models","Public Cloud vs Private Cloud","Hybrid cloud","Community cloud","Regulations on the cloud","General Data Privacy Regulation(GDPR) in cloud","Personal Data in cloud","The big three cloud providers","AWS","Microsoft Azure","Google Cloud","The risk of vendor lock-in in cloud","Sage Maker","Nerd Wallet","Lush Migration in Cloud"]

mcqs=[]
for topic in lists:
    mcq_dict={}
    result=chain.invoke({"topic_name":topic,"flag":"0"})
    mcq_dict["topic"]=topic
    mcq_dict["mcq"]=result
    mcqs.append(mcq_dict)
    print("Completed for topic",topic)

with open(r"CloudComputingMCQS.json","w",encoding="utf-8") as file:
    json.dump(mcqs,file,indent=4)

