from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for i in question_data:
    question_text = i["question"]
    question_ans = i["correct_answer"]
    question = Question(question_text,question_ans)
    question_bank.append(question)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz")

print(f"You're  total score: {quiz.score}/{quiz.question_number}")

#You can pick up as many questions as you like from Trivia api
