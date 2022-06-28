class QuizBrain:
    def __init__(self, q_list):
        self.number = 0
        self.list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.number < len(self.list)

    def next_question(self):
        current_question = self.list[self.number]
        correct_answer = current_question.answer
        self.number += 1
        user_answer = input(f"Q.{self.number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, u_answer, c_answer):
        if u_answer.lower() == c_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's incorrect.")
        print(f"The correct answer was: {c_answer}")
        print(f"Your current score is: {self.score}/{self.number}\n")
