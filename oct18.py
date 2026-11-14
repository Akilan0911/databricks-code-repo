#1.import all necessary lib
import sys
print(f"executing the script {sys.argv[0]}")

#3. define all functions
def greeting(arg):
	print(f"good morning team {arg}")
def message(arg):
	print(f"We have a quiz today - {arg}")

#4. main logic to execute/orchestrate
def main():
	if msg=='greeting':
		greeting(team_name)
	elif msg=='info':
		message(team_name)

print("length of arguments passed is ",len(sys.argv))
if len(sys.argv) > 2:
	#2. define all variables
	msg = sys.argv[1]
	team_name = sys.argv[2]
	main()