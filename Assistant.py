#!/usr/bin/python

from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser	
import datetime
import random
#for email sending
#import smtlib 
Alarms = ['']

def talkToMe(audio):
	print(audio)
	tts = gTTS(text=audio, lang='en')
	tts.save('audio.mp3')	
	os.system('mpg123 audio.mp3')

#listens for commands
def myCommand():
	r = sr.Recognizer()
	command = ''
	with sr.Microphone() as source:
		print('I am ready for your next command')
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source, duration = 1)
		audio = r.listen(source)
	try:
		command = r.recognize_google(audio)
		print('you said \"' + command + '\"\n')
	
	#loop back and countinue listening
	except sr.UnknownValueError:
		assistant(myCommand())

	return command

#Functions for commands

#returns the date in weekday month day.
def whatDayIsIT():
	weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
	months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	currentDate = datetime.date.today()
	weekday = weekdays[currentDate.weekday()]
	month = months[currentDate.month - 1]
	day = currentDate.day
	dayStr = str(day)	
	if day == 1:
		dayStr = '1st'
	elif day == 2:
		dayStr = '2nd'
	elif day == 3:
		dayStr = '3rd'
	else:
		dayStr = dayStr + 'th'
		
	talkToMe(weekday + ' ' + month + ' ' + dayStr)

def roll(num1, num2):
	ran = random.randint(num1,num2 - 1)
	return str(ran)

#if statements for commands
def assistant(command):
	if 'open Reddit python' in command:
		chrome_path = '/usr/bin/google-chrome'
		url = 'https://www.reddit.com/r/Python/'
		webbrowser.get(chrome_path).open(url)

	if 'what\'s up' in command:
		talkToMe('Just Chilling')

	if 'how are you' in command:
		talkToMe('Fantastic')

	if 'who created you' in command:
		talkToMe('Josh Basic')

	if 'what time is it' in command or 'what\'s the time' in command:
		currentDT = datetime.datetime.now()
		hour = currentDT.hour
		minute = currentDT.minute
		AMPM = 'AM'
		if hour > 12:
			hour = hour - 12
			AMPM = 'PM'
			
		
		time = str(hour) + ':' + str(minute) + AMPM 
		#print(time)
		talkToMe(time)
	
	if 'say' in command:
		#print("say: " + command[4:])		
		talkToMe(command[4:])
	
	if 'day is it' in command or 'date is it' in command or 'what\'s the date' in command:
		whatDayIsIT()

	if 'thank you' in command:
		talkToMe('Your welcome!')

	if 'roll' in command:
		cmdList = command.split()
		#check that there is a word after 'and' and the two words next to and are numbers.
		for i in range(len(cmdList)):
			if cmdList[i] == 'and' and i != len(cmdList) and cmdList[i-1].isdigit() and cmdList[i+1].isdigit():
				
				talkToMe(roll(int(cmdList[i-1]), int(cmdList[i+1])))
				break

while True:
	assistant(myCommand())



