import time
print("Welcome to leave application generator.")
print()
def leave(school, place, name, aclass, reason, indate, fdate):
	timecurrent = time.strftime("%x", time.localtime())
	return (f"\n{school},\n{place},\nDate - {timecurrent} \n\nRespected teacher,\nI am {name} of {aclass} of your school {school}. I want a small leave because of {reason} from {indate} to {fdate}. It would be a great help if you consider my leave and provide me leave as I requested.\nThanking you,\nYour obidient student,\n{name}.\n\n\n ")
	
a = input("School name: ")
b = input("City name: ")
d = input("your name: ")
#e = input("Current date: ")
f = input("Reason for leave: ")
g = input("Your class along with section: ")
h = input("Initial date for leave: ")
i = input("Final date for leave: ")
z = open(r'C:\Leave.txt', "a")
z.write(f"Created by application generator 1.0, at {time.asctime(time.localtime())}\n"+leave(a, b, d, g, f, h, i))
z.close
print("Text file successfully created at C:\\ by name \"Leave.txt\"")
