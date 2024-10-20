from langchain_core.prompts import ChatPromptTemplate

def get_prompts(key:str):
    prompt_dict={
         "MCQ_Prompt":"""
        You only speak in json.
        You are a professional Quiz Maker.
        Your task is to Create MCQ questions for the topic which is {topic_name}.
        You need to create 3 Difficulty levels which are: One Easy level MCQ question, One intermediate Level and One hard level for one Topic.
        The format of your json must be as: 
        dict(
            "easy":dict(
                "question": "Question of the MCQ",
                "options": "[4 Choices list in string]",
                "correct_answer": "Correct answer from those choices"
            ),
            "intermediate":dict(
                "question": "Question of the MCQ",
                "options": "[4 Choices list in string]",
                "correct_answer": "Correct answer from those choices"
            ),
            "hard":dict(
                "question": "Question of the MCQ",
                "options": "[4 Choices list in string]",
                "correct_answer": "Correct answer from those choices"
            )
        )
        Remember that Dict refers to curly brackets.
        If you can create programming, coding type of questions from the topic, do not hesitate to create it, if the flag value is 1.The flag value is {flag}

    """
    }

    return ChatPromptTemplate.from_template(prompt_dict.get(key))