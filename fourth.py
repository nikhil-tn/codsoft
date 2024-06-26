import time
import threading

class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer
    
    def display_question(self):
        print(self.text)
        for index, option in enumerate(self.options, start=1):
            print(f"{index}. {option}")
    
    def check_answer(self, user_answer):
        return user_answer == self.correct_answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
    
    def run_quiz(self):
        print("Welcome to the Quiz!")
        print("You will have 10 seconds to answer each question.\n")
        time.sleep(1)
        
        for question in self.questions:
            self.ask_question(question)
        
        print("\nQuiz completed!")
        print(f"Your final score is: {self.score}/{len(self.questions)}")
    
    def ask_question(self, question):
        question.display_question()
        
        timer = threading.Timer(10.0, self.timeout)
        timer.start()
        
        try:
            user_answer = int(input("Enter your answer (1/2/3/4): ")) - 1
            timer.cancel()  # Cancel timer if answer submitted before timeout
            if 0 <= user_answer < len(question.options):
                if question.check_answer(question.options[user_answer]):
                    print("Correct!")
                    self.score += 1
                else:
                    print("Incorrect!")
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    def timeout(self):
        print("\nTime's up!")
        print("No answer submitted for this question.\n")

if __name__ == "__main__":

    questions = [
        Question("What is the capital of France?", ["Paris", "Berlin", "London", "Madrid"], "Paris"),
        Question("Who wrote 'Harry Potter' series?", ["J.K. Rowling", "George R.R. Martin", "Stephen King", "J.R.R. Tolkien"], "J.K. Rowling"),
        Question("What is the largest planet in our solar system?", ["Jupiter", "Saturn", "Neptune", "Mars"], "Jupiter")
    ]
    
    quiz = Quiz(questions)
    
    quiz.run_quiz()
