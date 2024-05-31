import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from quiz_data import quiz_data

# Initialize the current question index and score
current_question = 0
score = 0

# Function to display the current question and answer choices
def show_question():
    question = quiz_data[current_question]
    question_label.config(text=question["question"], font=("Arial", 18, "bold"), background="white")

    choices = question["choices"]
    for i in range(4):
        choice_buttons[i].config(text=choices[i], state="normal", bg="#1877f2", fg="white")

    feedback_label.config(text="")
    next_button.config(state="disabled")
    
    img = Image.open(question["image"])
    img = img.resize((250, 150), Image.LANCZOS)  # Adjust the size as needed
    photo = ImageTk.PhotoImage(img)
    image_label.config(image=photo)
    image_label.image = photo

# Function to check if the selected answer is correct
def check_answer(choice):
    global score
    question = quiz_data[current_question]
    selected_choice = choice_buttons[choice].cget("text")

    if selected_choice == question["answer"]:
        score += 1
        feedback_label.config(text="Good Job!", foreground="green")
    else:
        feedback_label.config(text="You got it wrong!", foreground="red")

    for button in choice_buttons:
        button.config(state="disabled")
    next_button.config(state="normal")

    score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))

# Function to move to the next question or end the quiz if it was the last question
def next_question():
    global current_question
    current_question += 1

    if current_question < len(quiz_data):
        show_question()
    else:
        messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Good Job! \nFinal score: {}/{}".format(score, len(quiz_data)))
        window.destroy()

# Function to navigate to the next page (from instructions to the quiz)
def move_next_page():
    global count
    if count < len(pages) - 1:
        pages[count].pack_forget()
        count += 1
        pages[count].pack(fill=tk.BOTH, expand=True)

# Create the main window
window = tk.Tk()
window.title("Quiz Game")
window.geometry("800x750")
window.config(bg="White")

# Main frame to hold pages
main_frame = tk.Frame(window, bg="white")
main_frame.pack(fill=tk.BOTH, expand=True)


quiz_label = tk.Label(main_frame,
                      text="Guess the Flag",
                      font=("Arial", 30, "bold"),
                      bg="white")
quiz_label.pack()

# Page 1: Instructions and objectives
page_1 = tk.Frame(main_frame, bg="white")
objective_label = tk.Label(page_1, 
                           text="Objective:", 
                           font=("Arial", 18, "bold"),
                           bg="white")
objective_label.pack(pady=10)

#This tells the user what the point of the program is
objective_instructions = tk.Label(page_1, 
                                  text="Try to guess the country associated with the displayed flag.\nThe game will present a series of flags around the world.\nYour goal is to correctly identify the corresponding country.", 
                                  font=("Arial", 14),
                                  bg="white")
objective_instructions.pack(pady=10)

#Label for how to play
how_play_label = tk.Label(page_1, 
                          text="How to Play:", 
                          font=("Arial", 18, "bold"),
                          bg="white")
how_play_label.pack(pady=10)

#instructions on how to play the program
play_instructions = tk.Label(page_1, 
                             text="1. You will be shown a flag.\n2. Select the name of the country you think the flag represents.\n3. Click the button to submit your guess.", 
                             font=("Arial", 14),
                             bg="white")
play_instructions.pack(pady=10)

#Score Label
score_text = tk.Label(page_1, 
                      text="Scoring:", 
                      font=("Arial", 18, "bold"),
                      bg="white")
score_text.pack(pady=10)

#How the scoring will work on the program
score_instructions = tk.Label(page_1,
                              text="Correct Guess: You earn points for each correct guess.\nIncorrect Guess: Points may be deducted for incorrect guesses.",
                              font=("Arial", 14),
                              bg="white")
score_instructions.pack()

# Tips for how to play the game
tips_text = tk.Label(page_1,
                     text="Tips:",
                     font=("Arial", 18, "bold"),
                     bg="white")
tips_text.pack(pady=10)

# Details on how the game will be
tips_label = tk.Label(page_1,
                      text="Pay attention to the details of each flag, such as colors, symbols, or distinctive\nfeatures. Use your knowledge of world geography to make educated guesses.",
                      font=("Arial", 14),
                      bg="white")
tips_label.pack()

# Prompt to click next to continue
click_next = tk.Label(page_1,
                      text="Click Next to Continue.",
                      font=("Arial", 18, "bold"),
                      bg="white")
click_next.pack(pady=20)


# Pack the first page
page_1.pack(pady=10)

# Button to continue to the quiz page
nextBTN = tk.Button(page_1, 
                    text="Continue", 
                    font=("Arial", 12, "bold"), 
                    bg="#1877f2", 
                    fg="white", 
                    width=12, 
                    command=move_next_page)
nextBTN.pack(pady=10)
page_1.pack(fill=tk.BOTH, expand=True)

# Page 2: Quiz questions and answers
page_2 = tk.Frame(main_frame, bg="white")


#Question labek
question_label = ttk.Label(page_2, 
                           anchor="center", 
                           padding=10)
question_label.pack(pady=10)


image_label = ttk.Label(page_2, anchor="center", padding=10, background="white")
image_label.pack(pady=10)

choice_frame = tk.Frame(page_2, background="white")
choice_frame.pack(pady=20) 


#Buttons
choice_buttons = []
for i in range(4):
    button = tk.Button(choice_frame, 
                       width=15,
                       height=1,
                       command=lambda i=i: check_answer(i), 
                       font=("Arial", 15))
    choice_buttons.append(button)
    button.grid(row=i//2, column=i%2, padx=10, pady=10)

feedback_label = tk.Label(page_2, 
                          anchor="center", 
                          bg="white", 
                          font=("Arial", 15))
feedback_label.pack(pady=10)

#Total score at the end
score_label = ttk.Label(page_2, 
                        text="Score: 0/{}".format(len(quiz_data)), 
                        anchor="center", 
                        padding=10, 
                        background="white", 
                        font=("Arial", 17))
score_label.pack()

#For next question
next_label = tk.Label(page_2, 
                      text="Click Here for next Question.", 
                      font=("Arial", 14, "bold"), 
                      background="white")
next_label.pack(pady=5)

#will disabel the next button if user hasn't answer
next_button = tk.Button(page_2, 
                        text="Next", 
                        state="disabled", 
                        font=("Arial", 13), 
                        bg="#1877f2", 
                        fg="white",
                        pady=10, 
                        padx=15,
                        command=next_question )
next_button.pack(pady=10)

# List to hold the pages
pages = [page_1, page_2]
count = 0

# Show the first question
show_question()

# Start the main event loop
window.mainloop()
