filehandle = open("questions.txt", 'r')
score = 0
print("Welcome to the Quiz!")

while True:
 
    question = filehandle.readline().strip()
    if not question:  
        break
    answer_a = filehandle.readline().strip()
    answer_b = filehandle.readline().strip()
    answer_c = filehandle.readline().strip()
    answer_d = filehandle.readline().strip()
    correct_answer = filehandle.readline().strip().split(": ")[1]
    print(question)
    print(answer_a)
    print(answer_b)
    print(answer_c)
    print(answer_d)
    user_answer = input("Your answer (A, B, C, or D): ").strip().upper()
    if user_answer == correct_answer:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was {correct_answer}.\n")

filehandle.close()
print(f"Quiz complete! You scored {score}.")
