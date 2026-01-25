# Iris – A Simple Rule-Based Python Chatbot

Iris is a terminal-based chatbot built using core Python concepts.  
It follows a rule-based approach to simulate basic conversation and focuses on clarity, structure, and clean logic rather than advanced AI techniques.

This project was built as a learning exercise to strengthen fundamentals like control flow, functions, and file handling.

---

## Features
- Interactive terminal-based conversation
- Rule-based intent handling (positive, negative, fallback responses)
- Session-based chat history saved to a text file
- Persistent storage using file I/O
- Modular design using helper functions
- Graceful exit handling

---

## Technologies Used
- Python
- Control Flow (`if/elif/else`, loops)
- Functions
- File Handling (read/write/append)

---

## How It Works
1. The chatbot greets the user and asks for their name.
2. User inputs are processed inside a loop until the user exits.
3. Responses are selected using predefined rule-based logic.
4. Each conversation session is stored in a text file for reference.

---

## How to Run
1. Clone the repository
2. Run the script using:
   ```bash
   python iris.py
