
import tkinter as tk
import sympy as sp
import re



WINDOW_TITLE = "My Derivative Calculator"
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 450
BACKGROUND_COLOR = "#202B3C"

TITLE_COLOR = "#FFFFFF"
TEXT_COLOR = "#E2E8F0"
RESULT_COLOR = "#7CFCB2"

FONT_NAME = "Arial"
TITLE_SIZE = 20
TEXT_SIZE = 11
BUTTON_SIZE = 11

CALCULATE_COLOR = "#16A34A"
CLEAR_COLOR = "#475569"
BUTTON_TEXT_COLOR = "#FFFFFF"

INPUT_WIDTH = 35
INPUT_FONT_SIZE = 13



x, y, z = sp.symbols('x y z')




def calculate():

    equation = entry.get().strip()
    variable = choice.get()

    # Check empty input
    if not equation:
        result.config(text="Please enter an equation.")
        status.config(text="Input is empty.")
        return

    # Allowed variables and functions
    allowed_names = {
        "x", "y", "z",
        "sin", "cos", "tan",
        "sqrt", "log", "exp"
    }

    # Detect words in the input
    words = re.findall(r'[A-Za-z_]\w*', equation)

    # Reject unsupported words
    if any(word not in allowed_names for word in words):
        result.config(text="Invalid equation!")
        status.config(text="Unsupported word detected.")
        return

    try:

        # Convert input into a SymPy expression
        expression = sp.sympify(
            equation,
            locals={
                'x': x,
                'y': y,
                'z': z,
                'sin': sp.sin,
                'cos': sp.cos,
                'tan': sp.tan,
                'sqrt': sp.sqrt,
                'log': sp.log,
                'exp': sp.exp
            }
        )

        # Calculate derivative
        if variable == "x":
            answer = sp.diff(expression, x)

        elif variable == "y":
            answer = sp.diff(expression, y)

        elif variable == "z":
            answer = sp.diff(expression, z)

        else:
            result.config(text="Invalid variable!")
            status.config(text="Select x, y, or z.")
            return

        # Display result
        result.config(text="Derivative: " + str(answer))
        status.config(text="Calculation successful!")

    except Exception:
        result.config(text="Invalid equation!")
        status.config(text="Check your mathematical syntax.")




def clear():

    entry.delete(0, tk.END)

    result.config(text="Derivative will appear here")
    status.config(text="Ready")




window = tk.Tk()

window.title(WINDOW_TITLE)

window.geometry(
    f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
)

window.resizable(False, False)

window.configure(bg=BACKGROUND_COLOR)



title = tk.Label(
    window,
    text="Derivative Calculator",
    font=(FONT_NAME, TITLE_SIZE, "bold"),
    bg=BACKGROUND_COLOR,
    fg=TITLE_COLOR
)

title.pack(pady=20)



instruction = tk.Label(
    window,
    text="Enter a mathematical expression:",
    font=(FONT_NAME, TEXT_SIZE),
    bg=BACKGROUND_COLOR,
    fg=TEXT_COLOR
)

instruction.pack()

entry = tk.Entry(
    window,
    width=INPUT_WIDTH,
    font=(FONT_NAME, INPUT_FONT_SIZE)
)

entry.pack(pady=12)




variable_label = tk.Label(
    window,
    text="Differentiate with respect to:",
    font=(FONT_NAME, TEXT_SIZE),
    bg=BACKGROUND_COLOR,
    fg=TEXT_COLOR
)

variable_label.pack()

choice = tk.StringVar(value="x")

variable_menu = tk.OptionMenu(
    window,
    choice,
    "x", "y", "z"
)

variable_menu.pack(pady=8)




calculate_button = tk.Button(
    window,
    text="Calculate",
    command=calculate,
    width=14,
    bg=CALCULATE_COLOR,
    fg=BUTTON_TEXT_COLOR,
    font=(FONT_NAME, BUTTON_SIZE, "bold")
)

calculate_button.pack(pady=7)

clear_button = tk.Button(
    window,
    text="Clear",
    command=clear,
    width=14,
    bg=CLEAR_COLOR,
    fg=BUTTON_TEXT_COLOR,
    font=(FONT_NAME, BUTTON_SIZE)
)

clear_button.pack(pady=5)



result = tk.Label(
    window,
    text="Derivative will appear here",
    font=(FONT_NAME, TEXT_SIZE, "bold"),
    bg=BACKGROUND_COLOR,
    fg=RESULT_COLOR,
    wraplength=450
)

result.pack(pady=18)




status = tk.Label(
    window,
    text="Ready",
    font=(FONT_NAME, 9),
    bg=BACKGROUND_COLOR,
    fg=TEXT_COLOR
)

status.pack()



window.mainloop()
