import subprocess
from datetime import datetime

CMD = '''
on run argv
  display notification (item 2 of argv) with title (item 1 of argv)
end run
'''

def notify(title, text):
    subprocess.call(['osascript', '-e', CMD, title, text])

completed = False

while True:
    date = datetime.now().date()
    time = datetime.now().time()
    date = int(date.strftime("%w"))
    time = str(time.strftime("%H:%M"))
    if time == "8:00":
        with open("data.txt", "w") as raw_data:
            if completed == True:
                raw_data.write("True")
                completed = False
            else:
                raw_data.write("False")

        with open("data.txt", "r") as data_read:
            data = data_read.read()

    if time == "8:00":
        if data == "False":
            if date == 1:
                notify("PiggyJr's Daily Reminder", "Make sure to remember your guitar lesson!")
                completed = True

            if date == 2:
                notify("PiggyJr's Daily Reminder", "You have nothing to remember today!")
                completed = True

            if date == 3:
                notify("Piggy Jr's Daily Reminder", "Make sure to remember your media den books and your chess tournament!")
                completed = True

            if date == 4:
                notify("PiggyJr's Daily Reminder", "You have nothing to remember today!")
                completed = True

            if date == 5:
                notify("PiggyJr's Daily Reminder", "You have nothing to remember today!")
                completed = True
            
            if date == 6:
                notify("PiggyJr's Daily Reminder", "You have nothing to remember today!")
                completed = True

            if date == 0:
                notify("PiggyJr's Daily Reminder", "Make sure to remember to go to church today!")
                completed = True
