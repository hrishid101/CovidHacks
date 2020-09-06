import tkinter as tk
import datetime
import webbrowser
import matplotlib.pyplot as plt

today1 = datetime.date.today()
yesterday1 = today1 - datetime.timedelta(days=1)

minutes = 0


root = tk.Tk()
root.title('Fitness Is My Passion')
root.geometry('800x500')
root.resizable(0, 0)

frame = tk.Frame(root, bg='#80ccff')
frame.place(relwidth=1, relheight=1)

frame1 = tk.Frame(root, bg='light gray')
frame1.place(relx=.5, rely=.1, relwidth=.8, relheight=.4, anchor='n')

label = tk.Label(frame1, text='Welcome to our Fitness App!', bg='#80ccff', font=("Arial", 46), justify='center',
                 wraplength=500, fg='#002e4d')
label.place(relwidth=1, relheight=1)

frame2 = tk.Frame(root, bg='#80ccff')
frame2.place(relx=.5, rely=.5, relwidth=.8, relheight=.4, anchor='n')

user1 = tk.Entry(frame2, bg='#e6f5ff', font=("Arial", 20), justify='center')
user1.place(relwidth=1, relheight=.25)

label2 = tk.Label(frame2, text='Enter your name in the box above.', bg='#80ccff', font=("Arial", 20), justify='center',
                  wraplength=500, fg='#002e4d')
label2.place(rely=.25, relwidth=1, relheight=.25)

button = tk.Button(frame2, text='Log In', bg='#e6f5ff', font=("Arial", 16), command=lambda: logIn(user1.get()),
                   justify='center')
button.place(rely=.5, relwidth=.5, relheight=.25)

button2 = tk.Button(frame2, text='Sign Up', bg='#e6f5ff', font=("Arial", 16), command=lambda: signUp(user1.get()),
                    justify='center')
button2.place(relx=.5, rely=.5, relwidth=.5, relheight=.25)


def destroyMain():
    label.destroy()
    label2.destroy()
    button.destroy()
    button2.destroy()


def signUp(user1):
    global user
    destroyMain()
    user = user1
    exerciseLog = open(f'{user}Log.txt', 'a')
    healthData = open(f'{user}HealthData.txt', 'a')
    timeLog = open(f'{user}Time.txt', 'a')
    dateLog = open(f'{user}Date.txt', 'a')
    weightLog = open(f'{user}Weight.txt', 'a')
    workoutDate = open(f'{user}WorkoutDate.txt', 'a')
    minuteLog = open(f'{user}Minutes.txt', 'a')
    bmiLog = open(f'{user}BMI.txt', 'a')
    signUpPage()


def signUpPage():
    global dataLabel, heightLabel, weightLabel, ageLabel, weightInput, ageInput, hawButton, heightInput

    frame = tk.Frame(root, bg='#80ccff')
    frame.place(relwidth=1, relheight=1)

    frame1 = tk.Frame(root, bg='#80ccff')
    frame1.place(relx=.5, rely=.1, relwidth=1, relheight=.5, anchor='n')

    dataLabel = tk.Label(frame1, text='Enter Data:', bg='#80ccff', font=("Arial", 46), justify='center',
                     wraplength=500, fg='#002e4d')
    dataLabel.place(relwidth=1, relheight=.5)

    heightLabel = tk.Label(frame1, bg='#80ccff', font=("Arial", 20), text='Height (in):', justify='center')
    heightLabel.place(relx=.05, rely=.5, relwidth=.25, relheight=.25)

    weightLabel = tk.Label(frame1, bg='#80ccff', font=("Arial", 20), justify='center', text='Weight(lbs):')
    weightLabel.place(relx=.375, rely=.5, relwidth=.25, relheight=.25)

    ageLabel = tk.Label(frame1, bg='#80ccff', text='Age:', font=("Arial", 20), justify='center')
    ageLabel.place(relx=.7, rely=.5, relwidth=.25, relheight=.25)

    frame2 = tk.Frame(root, bg='#80ccff')
    frame2.place(relx=.5, rely=.5, relwidth=1, relheight=.5, anchor='n')

    heightInput = tk.Entry(frame2, bg='#e6f5ff', font=("Arial", 20), justify='center')
    heightInput.place(relx=.05, relwidth=.25, relheight=.25)

    weightInput = tk.Entry(frame2, bg='#e6f5ff', font=("Arial", 20), justify='center')
    weightInput.place(relx=.375, relwidth=.25, relheight=.25)

    ageInput = tk.Entry(frame2, bg='#e6f5ff', font=("Arial", 20), justify='center')
    ageInput.place(relx=.7, relwidth=.25, relheight=.25)

    hawButton = tk.Button(frame2, bg='#e6f5ff', font=("Arial", 20), justify='center', text='Enter', command=lambda: hawEnter())
    hawButton.place(relx=.25, rely=.35, relwidth=.5, relheight=.25)

    enterButton = tk.Button(frame2, bg='#e6f5ff', font=("Arial", 20), justify='center', text='Continue',
                          command=lambda: homeScreen())
    enterButton.place(relx=.25, rely=.65, relwidth=.5, relheight=.25)


def destroyHaw():
    dataLabel.destroy()
    heightLabel.destroy()
    weightLabel.destroy()
    ageLabel.destroy()
    heightInput.destroy()
    weightInput.destroy()
    ageInput.destroy()
    hawButton.destroy()


def hawEnter():
    global height, weight, age, bmi
    height = heightInput.get()
    weight = weightInput.get()
    age = ageInput.get()
    bmi = round((703 * (int(weight)) / (int(int(height) ** 2))), 2)
    healthData = open(f'{user}HealthData.txt', 'r+')
    weightLog = open(f'{user}Weight.txt', 'a')
    dateLog = open(f'{user}Date.txt', 'a')
    bmiLog = open(f'{user}BMI.txt', 'a')
    healthData.write(str(height) + '\n')
    healthData.write(str(weight) + '\n')
    healthData.write(str(age) + '\n')
    healthData.write(str(bmi) + '\n')
    weightLog.write(str(weight) + '\n')
    dateLog.write(str(today1) + '\n')
    bmiLog.write(str(bmi) + '\n')


def logIn(user1):
    global user, minutes, tLine, cLine, weight, wLine, bmi, bLine
    destroyMain()
    user = user1
    exerciseLog = open(f'{user}Log.txt', 'a')
    dietLog = open(f'{user}Diet.txt', 'a')
    healthData = open(f'{user}HealthData.txt', 'a')

    minuteLog = open(f'{user}Minutes.txt', 'r')
    tLines = minuteLog.readline()
    for tLine in minuteLog:
        pass
    if today1 != yesterday1:
        minutes = 0
    else:
        minutes = tLine

    weightLog = open(f'{user}Weight.txt', 'r')
    wLines = weightLog.readline()
    for wLine in weightLog:
        pass
        weight = wLine

    bmiLog = open(f'{user}BMI.txt', 'r')
    bLines = bmiLog.readline()
    for bLine in bmiLog:
        pass
        bmi = bLine

    homeScreen()


def homeScreen():
    global logLabel, logButton, workoutButton, bmiLabel, graphsButton, editHealthButton, weight, bmi
    getActiveMinutes()
    healthData = open(f'{user}HealthData.txt', 'r+')
    dataLines = healthData.readlines()



    frame = tk.Frame(root, bg='#80ccff')
    frame.place(relwidth=1, relheight=1)

    frame1 = tk.Frame(root, bg='#80ccff')
    frame1.place(relx=.5, relwidth=.9, relheight=.5, anchor='n')

    frame2 = tk.Frame(root, bg='#80ccff')
    frame2.place(relx=.5, rely=.5, relwidth=.9, relheight=.5, anchor='n')

    logLabel = tk.Label(frame1, text=f"Today's Active Minutes: {minutes}", bg='#80ccff', font=("Arial", 24),
                        justify='center',
                        fg='#002e4d')
    logLabel.place(relx=.05, rely=.1, relwidth=.9, relheight=.25)

    logButton = tk.Button(frame1, text='Log New Workout', bg='#e6f5ff', font=("Arial", 16), justify='center', command=lambda: logWorkoutPage())
    logButton.place(relx=.05, rely=.45, relwidth=.4, relheight=.25)

    workoutButton = tk.Button(frame1, text='Workouts', bg='#e6f5ff', font=("Arial", 16), justify='center', command=lambda: workoutPage())
    workoutButton.place(relx=.55, rely=.45, relwidth=.4, relheight=.25)

    graphLabel = tk.Label(frame2, text='Graphs: ', bg='#80ccff', font=("Arial", 26),
                             wraplength=500,
                             justify='center', fg='#002e4d')
    graphLabel.place(relwidth=.6, relheight=.25, rely=0.1, relx=0.025)

    bmiLabel = tk.Label(frame2, text=f'BMI: {dataLines[3]}', bg='#80ccff', font=("Arial", 20),
                        justify='left', fg='#002e4d')
    bmiLabel.place(relx=.725, relwidth=.25, relheight=.25, rely=0.175)

    graphsButton = tk.Button(frame2, text='Minutes Active', command=lambda: activeMinutesGraph(), bg='#e6f5ff', font=("Arial", 16), justify='center',
                             wraplength=300)
    graphsButton.place(relwidth=.3, relheight=.25, rely=.45)

    graphsButton1 = tk.Button(frame2, text='Weight', command=lambda: weightChangeGraph(), bg='#e6f5ff', font=("Arial", 16), justify='center',
                              wraplength=300)
    graphsButton1.place(relx=.35, relwidth=.3, relheight=.25, rely=0.45)

    editHealthButton = tk.Button(frame2, text='Edit BMI', bg='#e6f5ff', font=("Arial", 16), justify='center', command=lambda: editHealthData())
    editHealthButton.place(relx=.7, rely=.45, relwidth=.3, relheight=.25)


def destroyHome():
    logLabel.destroy()
    logButton.destroy()
    workoutButton.destroy()
    bmiLabel.destroy()
    graphsButton.destroy()
    editHealthButton.destroy()


def workoutPage():
    frame = tk.Frame(root, bg='#80ccff')
    frame.place(relwidth=1, relheight=1)

    dataLabel = tk.Label(frame, text='Workouts:', bg='#80ccff', font=("Arial", 40), justify='center',
                         wraplength=500, fg='#002e4d')
    dataLabel.place(relwidth=1, relheight=.5)

    graphsButton = tk.Button(frame, text='10 Min Abs', command=lambda: webbrowser.open('https://www.youtube.com/watch?v=AnYl6Nk9GOA'), bg='#e6f5ff',
                             font=("Arial", 16), justify='center',
                             wraplength=300)
    graphsButton.place(relwidth=.3, relheight=.25, rely=.5)

    graphsButton1 = tk.Button(frame, text='10 Min Arms', command=lambda: webbrowser.open('https://www.youtube.com/watch?v=DHOPWvO3ZcI'), bg='#e6f5ff',
                              font=("Arial", 16), justify='center',
                              wraplength=300)
    graphsButton1.place(relx=.35, relwidth=.3, relheight=.25, rely=0.5)

    editHealthButton = tk.Button(frame, text='12 Min Legs', bg='#e6f5ff', font=("Arial", 16), justify='center',
                                 command=lambda: webbrowser.open('https://www.youtube.com/watch?v=Fu_oExrPX68'))
    editHealthButton.place(relx=.7, rely=.5, relwidth=.3, relheight=.25)

    homeButton = tk.Button(frame, command=lambda: homeButtonAction(), text='Home', font=("Arial", 16), bg='#e6f5ff',
                           justify='center')
    homeButton.place(relwidth=.2, relheight=.05)


def logWorkoutPage():
    destroyHome()
    global workoutTimeInput, exerciseTypeInput

    frame = tk.Frame(root, bg='#80ccff')
    frame.place(relwidth=1, relheight=1)

    frame1 = tk.Frame(root, bg='#80ccff')
    frame1.place(relx=.5, rely=.1, relwidth=1, relheight=.5, anchor='n')

    dataLabel3 = tk.Label(frame1, text='How long did you work out?', bg='#80ccff', font=("Arial", 46), justify='center',
                          wraplength=500, fg='#002e4d')
    dataLabel3.place(relwidth=1, relheight=.5)

    workoutTime = tk.Label(frame1, bg='#80ccff', font=("Arial", 20), justify='center', text='Workout Time (minutes):',
                            wraplength=250)
    workoutTime.place(relx=.1, rely=.5, relwidth=.35, relheight=.25)

    workoutType = tk.Label(frame1, bg='#80ccff', text='Workout Type:', font=("Arial", 20),
                             justify='center', wraplength=250)
    workoutType.place(rely=.5, relx=.55, relwidth=.35, relheight=.25)

    frame2 = tk.Frame(root, bg='#80ccff')
    frame2.place(relx=.5, rely=.5, relwidth=1, relheight=.5, anchor='n')

    workoutTimeInput = tk.Entry(frame2, bg='#e6f5ff', font=("Arial", 20), justify='center')
    workoutTimeInput.place(relx=.1, relwidth=.35, relheight=.25)

    exerciseTypeInput = tk.Entry(frame2, bg='#e6f5ff', font=("Arial", 20), justify='center')
    exerciseTypeInput.place(relx=.55, relwidth=.35, relheight=.25)

    enterButton2 = tk.Button(frame2, bg='#e6f5ff', font=("Arial", 20), justify='center', text='Enter',
                            command=lambda: logRun())
    enterButton2.place(relx=.25, rely=.35, relwidth=.5, relheight=.25)

    homeButton = tk.Button(frame, command=lambda: homeButtonAction(), text='Home', font=("Arial", 16), bg='#e6f5ff', justify='center')
    homeButton.place(relwidth=.2, relheight=.05)


def logRun():
    global minutes
    exerciseLog = open(f'{user}Log.txt', 'a')
    timeLog = open(f'{user}Time.txt', 'a')
    workoutDate = open(f'{user}WorkoutDate.txt', 'a')
    time = workoutTimeInput.get()
    minuteLog = open(f'{user}Minutes.txt', 'a')
    minutes1 = workoutTimeInput.get()
    minutes = int(minutes) + int(minutes1)
    print(minutes, minutes1)
    minuteLog.write(str(minutes) + '\n')
    type = exerciseTypeInput.get()
    exerciseLog.write(f'Time: {time} Minutes | Workout Type: {type} | Date: {today1}' + '\n')
    timeLog.write(time + '\n')
    workoutDate.write(str(today1) + '\n')


def activeMinutesGraph():
    with open(f'{user}Time.txt') as f:
        lines1 = [line.rstrip() for line in f]
    lines1 = [int(i) for i in lines1]

    with open(f'{user}WorkoutDate.txt') as t:
        lines2 = [line.rstrip() for line in t]

    xlist = lines2
    ylist = lines1

    plt.plot([i for i in xlist], [j for j in ylist])
    plt.ylabel('Minutes Spent Exercising')
    plt.xlabel('Date')
    plt.show()


def weightChangeGraph():
    with open(f'{user}Weight.txt') as f:
        lines1 = [line.rstrip() for line in f]
    lines1 = [int(i) for i in lines1]

    with open(f'{user}Date.txt') as t:
        lines2 = [line.rstrip() for line in t]
    lines2 = [str(i) for i in lines2]

    xlist1 = lines2
    ylist2 = lines1

    plt.plot([i for i in xlist1], [j for j in ylist2])
    plt.ylabel('Weight Loss/Gain')
    plt.xlabel('Date')
    plt.show()


def editHealthData():
    global dataLabel, heightLabel1, weightLabel1, ageLabel1, heightInput1, weightInput1, ageInput1, hawButton1

    frame = tk.Frame(root, bg='#80ccff')
    frame.place(relwidth=1, relheight=1)

    frame1 = tk.Frame(root, bg='#80ccff')
    frame1.place(relx=.5, rely=.1, relwidth=1, relheight=.5, anchor='n')

    dataLabel = tk.Label(frame1, text='Enter Data:', bg='#80ccff', font=("Arial", 46), justify='center',
                         wraplength=500, fg='#002e4d')
    dataLabel.place(relwidth=1, relheight=.5)

    heightLabel1 = tk.Label(frame1, bg='#80ccff', font=("Arial", 20), text='Height (in):', justify='center')
    heightLabel1.place(relx=.05, rely=.5, relwidth=.25, relheight=.25)

    weightLabel1 = tk.Label(frame1, bg='#80ccff', font=("Arial", 20), justify='center', text='Weight(lbs):')
    weightLabel1.place(relx=.375, rely=.5, relwidth=.25, relheight=.25)

    ageLabel1 = tk.Label(frame1, bg='#80ccff', text='Age:', font=("Arial", 20), justify='center')
    ageLabel1.place(relx=.7, rely=.5, relwidth=.25, relheight=.25)

    frame2 = tk.Frame(root, bg='#80ccff')
    frame2.place(relx=.5, rely=.5, relwidth=1, relheight=.5, anchor='n')

    heightInput1 = tk.Entry(frame2, bg='#e6f5ff', font=("Arial", 20), justify='center')
    heightInput1.place(relx=.05, relwidth=.25, relheight=.25)

    weightInput1 = tk.Entry(frame2, bg='#e6f5ff', font=("Arial", 20), justify='center')
    weightInput1.place(relx=.375, relwidth=.25, relheight=.25)

    ageInput1 = tk.Entry(frame2, bg='#e6f5ff', font=("Arial", 20), justify='center')
    ageInput1.place(relx=.7, relwidth=.25, relheight=.25)

    hawButton1 = tk.Button(frame2, bg='#e6f5ff', font=("Arial", 20), justify='center', text='Apply',
                          command=lambda: hawEdit())
    hawButton1.place(relx=.25, rely=.35, relwidth=.5, relheight=.25)

    homeButton = tk.Button(frame, command=lambda: homeButtonAction(), text='Home', font=("Arial", 16), bg='#e6f5ff',
                           justify='center')
    homeButton.place(relwidth=.2, relheight=.05)


def hawEdit():
    global height1, weight1, age1, bmi
    height1 = heightInput1.get()
    weight1 = weightInput1.get()
    age1 = ageInput1.get()
    bmi = round((703 * (int(weight1)) / (int(int(height1) ** 2))), 2)
    healthData = open(f'{user}HealthData.txt', 'r+')
    weightLog = open(f'{user}Weight.txt', 'a')
    bmiLog = open(f'{user}BMI.txt', 'a')
    dateLog = open(f'{user}Date.txt', 'a')
    healthData.write(str(height1) + '\n')
    healthData.write(str(weight1) + '\n')
    weightLog.write(str(weight1) + '\n')
    healthData.write(str(age1) + '\n')
    healthData.write(str(bmi) + '\n')
    bmiLog.write(str(bmi) + '\n')
    dateLog.write(str(today1) + '\n')


def homeButtonAction():
    homeScreen()


def getActiveMinutes():
    global minutes
    minuteLog = open(f'{user}Minutes.txt', 'r')
    lines = minuteLog.readline()
    for line in minuteLog:
        pass
        minutes = line

root.mainloop()
