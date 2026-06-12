def chatbot():
    print("Simple Chatbot")
    print("Type 'bye' to exit\n")
    
    while True:
        user_input = input("You : ").lower()
        
        if(user_input=="hello"):
            print("Bot : hii!")
        elif(user_input=="how are you"):
            print("Bot : I'm Fine, Thanks!")
        elif(user_input=="what is your name"):
            print("Bot : I am Simple Python Chatbot.")
        elif(user_input=="bye"):
            print("Bot : Goodbye !")
            break
        else:
            print("Bot : Sorry ! I dont Understand that.")
            
chatbot()