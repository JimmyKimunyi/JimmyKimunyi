#while loops are used to execute code multiple times
command = ""
started = False
 
while True:
    command= input(" > ").lower()
    if command=="start" :
        if started:
            print(" Car already started !")
        else:
            started = True
            print("Car started ...")
    elif command =="stop" :
        if not started :
            print ("Car already stopped ! ")
        else:
            started = False
            print("Car stopped ...")
    elif command == "help":
        print ("""
start - to start the car
stop - stop the car
quit - to quit""")
    elif command =="quit":
        break
    else :
        print (" Sorry, i don't understand that")
   
