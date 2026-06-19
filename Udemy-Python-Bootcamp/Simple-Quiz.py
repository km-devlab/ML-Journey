
"""
Quiz Game
---------
A simple multiple-choice quiz that tracks your score
and gives you a summary at the end.
"""


class QuizGame:
    def __init__(self):
        self.questions = [
            {
                "question": "What does 'print()' do in Python?",
                "options": ["A) Deletes a variable", "B) Displays output", "C) Creates a loop"],
                "answer": "B"
            },
            {
                "question": "Which symbol is used for comments in Python?",
                "options": ["A) //", "B) <!-- -->", "C) #"],
                "answer": "C"
            },
            {
                "question": "What data type is the value True?",
                "options": ["A) Integer", "B) Boolean", "C) String"],
                "answer": "B"
            },
            {
                "question": "Which keyword is used to define a function?",
                "options": ["A) func", "B) def", "C) function"],
                "answer": "B"
            },
            {
                "question": "What will len('hello') return?",
                "options": ["A) 4", "B) 5", "C) 6"],
                "answer": "B"
            },
        ]
        self.score = 0

    def ask_question(self, q):
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        answer = input("Your answer (A/B/C): ").strip().upper()

        if answer == q["answer"]:
            print("Correct!")
            self.score += 1
        else:
            print(f"Wrong. The correct answer was {q['answer']}.")

    def run(self):
        print("=== Welcome to the Python Quiz ===")
        print(f"There are {len(self.questions)} questions. Good luck!\n")

        for q in self.questions:
            self.ask_question(q)

        self.show_results()

    def show_results(self):
        total = len(self.questions)
        percentage = (self.score / total) * 100

        print("\n=== Quiz Complete ===")
        print(f"Score: {self.score}/{total} ({percentage:.0f}%)")

        if percentage == 100:
            print("Perfect score! You're a Python natural.")
        elif percentage >= 60:
            print("Nice job! Solid understanding.")
        else:
            print("Keep practicing — you'll get there!")


if __name__ == "__main__":
    game = QuizGame()
    game.run()
