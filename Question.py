class Question:
    def __init__(self, prompt, answer_key):
        self.prompt = prompt
        self.answer_key = answer_key


class essayQuestion(Question):
    def __init__(self, essay_prompt):
        self.essay_prompt = essay_prompt
