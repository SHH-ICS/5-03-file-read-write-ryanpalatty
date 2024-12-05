filehandle = open("questions.txt", 'w')

question = input("Enter the multiple-choice question: ")
answer1 = input("Enter the first answer choice: ")
answer2 = input("Enter the second answer choice: ")
answer3 = input("Enter the third answer choice: ")
answer4 = input("Enter the fourth answer choice: ")
correct_answer = input("Enter the letter of the correct answer (A, B, C, or D): ")

filehandle.write(question + "\n")
filehandle.write("A. " + answer1 + "\n")
filehandle.write("B. " + answer2 + "\n")
filehandle.write("C. " + answer3 + "\n")
filehandle.write("D. " + answer4 + "\n")
filehandle.write("Correct Answer: " + correct_answer + "\n")

filehandle.close()
print("Question saved to questions.txt successfully!")
