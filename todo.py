from datetime import datetime
import sys
import os.path

def FuncHelp():
	#Help Function
	
	todohelp="""Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""
	'''
	todohelp.encode(encoding='UTF-8',errors='strict')
	print(todohelp)
	'''
	sys.stdout.buffer.write(todohelp.encode('utf8'))

def FuncAdd(st):
	
	# Function to add a New Todo
	if os.path.isfile('todo.txt'):					
	    with open("todo.txt",'r') as reqTodo:
	    	data=reqTodo.read()
	    with open("todo.txt",'w') as todoFile:
	    	todoFile.write(st+'\n'+data)
	else:										
	    with open("todo.txt",'w') as todoFile:
	    	todoFile.write(st+'\n')
	print('Added todo: "{}"'.format(st))


def FuncShow():

	# Function to List and print the available todos
	if os.path.isfile('todo.txt'):
	    with open("todo.txt",'r') as reqTodo:
	    	data=reqTodo.readlines()
	    count=len(data)
	    st=""
	    for line in data:
	    	st+='[{}] {}'.format(count,line)
	    	count-=1
	    sys.stdout.buffer.write(st.encode('utf8'))	
	else:
	    print ("There are no pending todos!") 


def FuncDel(num):

	# Funcountion to Delete the task from the List
	if os.path.isfile('todo.txt'):
	    with open("todo.txt",'r') as reqTodo:
	    	data=reqTodo.readlines()
	    count=len(data)
	    if num>count or num<=0:
	    	print(f"Error: todo #{num} does not exist. Nothing deleted.")
	    else:
	    	with open("todo.txt",'w') as todoFile:
	    		for line in data:
	    			if count!=num:
	    				todoFile.write(line)
	    			count-=1
	    	print("Deleted todo #{}".format(num))
	else:
	    print("Error: todo #{} does not exist. Nothing deleted.".format(num))


def FuncComplete(num):

	# Function to mark the given task as Done
	if os.path.isfile('todo.txt'):
	    with open("todo.txt",'r') as reqTodo:
	    	data=reqTodo.readlines()
	    count=len(data)
	    if num>count or num<=0:
	    	print("Error: todo #{} does not exist.".format(num))
	    else:
	    	with open("todo.txt",'w') as todoFile:
	    		if os.path.isfile('done.txt'):
	    			with open("done.txt",'r') as todoDone:
				    	doneData=todoDone.read()
			    	with open("done.txt",'w') as doneFileMod:
			    		for line in data:
			    			if count==num:
			    				doneFileMod.write("x "+datetime.today().strftime('%Y-%m-%d')+" "+line)
			    			else:
			    				todoFile.write(line)
			    			count-=1
			    		doneFileMod.write(doneData)
		    	else:
		    		with open("done.txt",'w') as doneFileMod:
			    		for line in data:
			    			if count==num:
			    				doneFileMod.write("x "+datetime.today().strftime('%Y-%m-%d')+" "+line)
			    			else:
			    				todoFile.write(line)
			    			count-=1

	    	print("Marked todo #{} as done.".format(num))
	else:
	    print("Error: todo #{} does not exist.".format(num))


def FuncReport():

	# Function to Generate Report
	countTodo=0
	countDone=0
	if os.path.isfile('todo.txt'):
	    with open("todo.txt",'r') as todoFile:
	    	todoData=todoFile.readlines()
	    countTodo=len(todoData)
	if os.path.isfile('done.txt'):
	    with open("done.txt",'r') as doneFile:
	    	doneData=doneFile.readlines()
	    countDone=len(doneData)
	st=datetime.today().strftime('%Y-%m-%d') + " Pending : {} Completed : {}".format(countTodo,countDone)
	sys.stdout.buffer.write(st.encode('utf8'))

 
if len(sys.argv)==1:
	FuncHelp()
elif sys.argv[1]=='help':
	FuncHelp()
elif sys.argv[1]=='ls':
	FuncShow()
elif sys.argv[1]=='add':
	if len(sys.argv)>2:
		FuncAdd(sys.argv[2])
	else:
		print("Error: Missing todo string. Nothing added!")
elif sys.argv[1]=='del':
	if len(sys.argv)>2:
		FuncDel(int(sys.argv[2]))
	else:
		print("Error: Missing NUMBER for deleting todo.")
elif sys.argv[1]=='done':
	if len(sys.argv)>2:
		FuncComplete(int(sys.argv[2]))
	else:
		print("Error: Missing NUMBER for marking todo as done.")
elif sys.argv[1]=='report':
	FuncReport()
else:
	print('Option Not Available. Please use "./todo help" for Usage Information')