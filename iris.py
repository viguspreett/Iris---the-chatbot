from datetime import datetime

def start_NewConvo():
    with open("chat_history.txt", "a") as file :
        file.write("\n" + "-"*20 + "\n" + "NEW CONVERSATION" + "\t")
        file.write(f"Started at : {datetime.now()}\n")

def log(msg):
    print(msg)
    with open("chat_history.txt", "a") as file:
        file.write(msg + "\n")

start_NewConvo()

log("Iris : Hello there! I'm Iris, A simple chatbot :D")
name = input(f"Iris : May i know your name?\n User :")
log(f"User : {name}")
log(f"Iris : Nice to meet you! How are you doing, {name}?")

good_responses = ["good", "fine", "great", "all well", "I am dong good", "I am doing fine", ]
bad_responses = ["bad", "unwell", "sad", "not good", "not well", "not nice", "okayish"]

while True :  
    mood = input("User : ").lower()
    log(f"User : {mood}")

    if mood == "bye":
        log("Iris : Its okay, Goodbye. Take care!")
        break 
    elif mood in good_responses :
        log("Iris : Good to know! ")
    elif mood in bad_responses :
        log("Iris : It's okay. Ek din sab theek hoga. This too shall pass!") 
    else : log("Iris : Oh, I see")