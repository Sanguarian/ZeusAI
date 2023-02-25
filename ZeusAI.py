import openai
import tkinter as tk

# Set up OpenAI API
openai.api_key = "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"

# Set up OpenAI model
model_engine = "text-davinci-003"


# Define chat function
def chat(prompt, max_tokens):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text
    return message.strip()


# Define function to handle user input
def handle_input():
    global context
    user_input = input_box.get("1.0", 'end-1c')
    if user_input.lower() in ["exit", "quit", "bye"]:
        root.destroy()
        return
    prompt = f"{context}You: {user_input.strip()}\nZeus:"
    message = chat(prompt, max_tokens=128)
    chat_history.insert(tk.END, f"You: {user_input}\n")
    chat_history.insert(tk.END, f"Zeus: {message}\n", "zeus")
    context += f"You: {user_input.strip()}\nZeus: {message}\n"
    input_box.delete("1.0", tk.END)
    chat_history.see(tk.END)


# Define function to blink cursor
def blink_cursor():
    input_box.tag_configure("cursor", background="green", foreground="green")
    input_box.after(500, toggle_cursor)


def toggle_cursor():
    input_box.tag_configure("cursor", background="black", foreground="green")
    input_box.after(500, blink_cursor)


# Create GUI window
root = tk.Tk()
root.title("ZeusAI Chat")
root.configure(bg="black")
root.option_add("*Font", "TkFixedFont")

# Create chat history text widget with padding
chat_history = tk.Text(root, wrap=tk.WORD, bg="black", fg="green", font=('TkFixedFont', 12), width=50, padx=1)
chat_history.tag_config("zeus", foreground="white", background="black")
chat_history.pack(expand=True, fill=tk.BOTH)

# Create input frame widget
input_frame = tk.Frame(root, bg="black")
input_frame.pack(side=tk.BOTTOM, fill=tk.X)

# Create input box widget
input_box = tk.Text(
    input_frame,
    bg="black",
    fg="green",
    wrap=tk.WORD,
    font=('TkFixedFont', 12),
    height=5,
    width=50,
    insertbackground="green"
)
input_box.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
input_box.focus_set()
input_box.bind("<Return>", handle_input)
input_box.tag_configure("cursor", background="black", foreground="white")
toggle_cursor()

# Create submit button
submit_button = tk.Button(input_frame, text="Submit", command=handle_input, bg="black", fg="white")
submit_button.pack(side=tk.RIGHT)

# Initialize chat context
context = ""

# Start main loop
root.mainloop()