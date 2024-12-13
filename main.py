import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.config(padx=30,pady=30)

def calculate_bmi():
    pass

#ui
weight_input_label = tkinter.Label(text="Enter your weight (kg)")
weight_input_label.pack()

weight_input = tkinter.Entry(width=20)
weight_input.pack()

height_input_label = tkinter.Label(text="Enter your height (cm)")
height_input_label.pack()

height_input = tkinter.Entry(width=20)
height_input.pack()

calculate_button = tkinter.Button(text="Calculate",command=calculate_bmi())
calculate_button.pack()

result_label = tkinter.Label()
result_label.pack()

window.mainloop()