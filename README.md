# scientific-calculator
This project is a Scientific Calculator built using the Python Tkinter library. It provides basic arithmetic operations as well as advanced scientific functions such as trigonometric functions, logarithms, square roots, and more.

**Features**

**Basic Arithmetic:** 
Addition, subtraction, multiplication, and division.

**Scientific Functions:**
Trigonometric functions: Sine, Cosine, and Tangent (in degrees).

**Logarithms (base 10).**
Exponentiation and square roots.

**Constants:** Pi (π) and Euler's number (e).
Expression Evaluation: Supports parentheses for grouping expressions and the power operator ^ for exponentiation.

**Technologies Used**
Python: The programming language used for the calculator's logic.

Tkinter: A standard Python library used for creating the graphical user interface (GUI).

**How to Run**
Install Python: Make sure Python is installed on your machine. You can download it from python.org.

**Clone or Download the Repository:**
git clone https://github.com/your-repository/scientific-calculator.git

**Run the Python Script:** Navigate to the folder where the script is located and run the following command:
python calculator.py

**Code Structure**
ScientificCalculator Class
This is the main class that manages the functionality of the calculator. It consists of:

__init__ Method: Initializes the calculator, sets up the GUI layout, and binds button clicks to their respective functions.
create_widgets Method: Lays out the entry box and buttons in a grid format.
create_button Method: Creates buttons dynamically with specific text and positioning.
on_button_click Method: Handles the button clicks and updates the expression or evaluates the result.
calculate_result Method: Evaluates the mathematical expression using Python's eval function and updates the display.
Buttons
The calculator has buttons for digits, arithmetic operations, and scientific functions. Clicking on each button adds to the expression, and pressing the = button evaluates the expression.

**Error Handling**
If an invalid expression is entered, the calculator will display "Error" and reset the expression.

**GUI Design**
Dark Theme: The calculator has a dark background with buttons that are styled to provide a clean, modern look.
Responsive Layout: The buttons and entry field adjust to fit the window size, ensuring an optimal user experience across different screen sizes.
Future Improvements
Add more advanced scientific functions like hyperbolic functions, factorial, and nth roots.
Add keyboard input support for faster use.
Improve error handling for specific edge cases.

**License**
This project is open-source under the MIT License.
