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
