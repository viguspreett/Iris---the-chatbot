import tkinter as tk

good_responses = ["good", "fine", "great", "all well", "I am dong good", "I am doing fine", ]
bad_responses = ["bad", "unwell", "sad", "not good", "not well", "not nice", "okayish"]

def get_reply(msg):
    msg = msg.lower()

    if msg == "bye":
        return "Goodbye. Take care!"
    elif msg in good_responses:
        return "That's good to hear!"
    elif msg in bad_responses:
        return "It's okay. This too shall pass."
    else:
        return "Oh, I see."

root = tk.Tk()
root.title("Iris – The Chatbot")
root.geometry("500x600")

user_name = None # conversation state

chat_box = tk.Text(root, height=25, width=60, wrap="word") #display
chat_box.pack(pady=10)
chat_box.config(state="disabled")

user_entry = tk.Entry(root, width=45) #entry
user_entry.pack(pady=5)
user_entry.focus()

def send_message(event=None): 
    global user_name

    user_msg = user_entry.get().strip()
    if not user_msg:
        return

    chat_box.config(state="normal")
    chat_box.insert(tk.END, f"User: {user_msg}\n")

    if user_name is None:
        user_name = user_msg
        chat_box.insert(
            tk.END,
            f"Iris: Nice to meet you! How are you doing, {user_name}?\n\n"
        )
    else:
        reply = get_reply(user_msg)
        chat_box.insert(tk.END, f"Iris: {reply}\n\n")

        if user_msg.lower() == "bye":
            chat_box.config(state="disabled")
            root.after(1200, root.destroy)
            return

    chat_box.config(state="disabled")
    chat_box.see(tk.END)
    user_entry.delete(0, tk.END)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

root.bind("<Return>", send_message)

chat_box.config(state="normal")
chat_box.insert(
    tk.END,
    "Iris: Hello there! I'm Iris, A simple chatbot :D\n"
    "Iris: May I know your name?\n\n"
)
chat_box.config(state="disabled")

root.mainloop()