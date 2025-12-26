from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for i in question_data:
    question_text = i["text"]
    question_ans = i["answer"]
    question = Question(question_text,question_ans)
    question_bank.append(question)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz")
print(f"You're  total score: {quiz.score}/{quiz.question_number}")