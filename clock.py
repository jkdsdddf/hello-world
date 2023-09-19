import time

focus_minutes = 25
break_minutes = 5

def focus_timer(num_sessions):
    for i in range(num_sessions):
      print("Focusing...")
        time.sleep(focus_minutes * 60)
      print("Break time!")
        time.sleep(break_minutes * 60)

def main():
  num_sessions = 4
  focus_timer(num_sessions)

print("Congratulations! You have completed {} focus sessions and taken breaks in between.".format(num_sessions))

while True:
    user_input = input("Would you like to continue with another focus session? (yes/no): ")
    if user_input.lower() == "yes":
        num_sessions += 1
        print("Starting another focus session...")
        focus_timer(1)
        elif user_input.lower() == "no":
            print("Thank you for using the focus timer. Keep up the great work!dk")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

print("End of program.")
if __name__ == "__main__":
     main()
