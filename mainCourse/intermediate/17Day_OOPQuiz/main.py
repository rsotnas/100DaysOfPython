from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(question['text'], question['answer']) for question in question_data]
print(question_bank)


quiz = QuizBrain(question_bank)
quiz.next_question()


while quiz.still_has_questions():
  quiz.next_question()

print(f"You have completed the quiz. Your final score is: {quiz.score}/{quiz.question_number}")