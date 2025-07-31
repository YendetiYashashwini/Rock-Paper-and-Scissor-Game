import random
choices = {
    "1" : "Rock🪨", 
    "2" : "Paper📃",
    "3" : "Scissor✂️"
}
user_score = 0
comp_score = 0
while True:
    print("🎮 Welcome to the Rock🪨 , Paper📃 and Scissor✂️  Game!")
    print("Choose your option : ")
    print("1. Rock🪨\n2. Paper📃\n3. Scissor✂️")
    while True:
        user_choice = input("Enter your choice (1/2/3) : ")
        if user_choice in ["1", "2", "3"]:
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
            continue
    comp_choice = random.choice(["1", "2", "3"])
    if user_choice == comp_choice:
        Result = "IT'S A TIE, Try again! 🤝"
    elif (user_choice == "1" and comp_choice == "3") or (user_choice == "2" and comp_choice == "1") or (user_choice == "3" and comp_choice == "2"):
        Result = "🏆 YOU WON! Congratulations! 🎉"
        user_score += 1
    else:
        Result = "YOU LOST! Better luck next time.😊"
        comp_score += 1
    print(f"You chose : {choices[user_choice]}")
    print(f"Computer chose : {choices[comp_choice]}")
    print(Result)
    print(f"📊 Scoreboard:\nYou: {user_score}\tComputer: {comp_score}")
    play_again = input("Do you want to continue playing? (yes/no) : ").strip().lower()
    if play_again != "yes":
        print("Thank you for playing! Goodbye! 👋")
        break
     
            
