import tkinter as tk
from tkinter import ttk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg="#2E2E2E")  # Dark background

        self.expression = ""
        self.text_input = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry box
        entry = ttk.Entry(self.root, textvariable=self.text_input, font=('arial', 24, 'bold'), justify='right', state='readonly')
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

        # Button frame
        button_frame = tk.Frame(self.root, bg="#2E2E2E")
        button_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        # Buttons configuration (text, row, col)
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0), ('(', 5, 1), (')', 5, 2), ('^', 5, 3),
            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('log', 6, 3),
            ('sqrt', 7, 0), ('exp', 7, 1), ('pi', 7, 2), ('e', 7, 3)
        ]

        # Create buttons with colors and padding
        for (text, row, col) in buttons:
            self.create_button(button_frame, text, row, col)

        # Configure rows and columns to expand and fill space
        for i in range(1, 8):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def create_button(self, frame, text, row, col):
        button = tk.Button(frame, text=text, font=('arial', 16, 'bold'), 
                           bg="#333", fg="white", activebackground="#555", 
                           activeforeground="white", 
                           command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, ipadx=15, ipady=15, padx=5, pady=5, sticky='nsew')

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            self.calculate_result()
        elif char == 'pi':
            self.expression += str(math.pi)
        elif char == 'e':
            self.expression += str(math.e)
        elif char == 'sqrt':
            self.expression += 'math.sqrt('
        elif char == 'sin':
            self.expression += 'math.sin(math.radians('
        elif char == 'cos':
            self.expression += 'math.cos(math.radians('
        elif char == 'tan':
            self.expression += 'math.tan(math.radians('
        elif char == 'log':
            self.expression += 'math.log10('
        elif char == '^':
            self.expression += '**'
        else:
            self.expression += str(char)

        self.text_input.set(self.expression)

    def calculate_result(self):
        try:
            result = eval(self.expression)
            self.text_input.set(result)
            self.expression = str(result)
        except Exception as e:
            self.text_input.set("Error")
            self.expression = ""

# Main function to run the calculator
def main():
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
