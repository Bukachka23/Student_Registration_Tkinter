import tkinter
from tkinter import ttk
from tkinter import messagebox


# The function for the accept button and the enter data button
def enter_data():
    accepted = accept_var.get()
    if accepted == "Accepted":

        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        if firstname and lastname:

            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            registration_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()

            output_text.insert("end", f"First Name: {firstname}, Last Name: {lastname}\n")
            output_text.insert("end", f"Title: {title}, Age: {age}, Nationality: {nationality}\n")
            output_text.insert("end", f"Number of Courses: {numcourses}, Number of Semesters: {numsemesters}\n")
            output_text.insert("end", f"Registration Status: {registration_status}\n")
            output_text.insert("end", "----------------------------------\n")
        else:
            tkinter.messagebox.showwarning("Warning", "You must enter a first and last name")
    else:
        tkinter.messagebox.showwarning("Warning", "You must accept the terms and conditions")

# The function for the accept button
def show_info():
    info_window = tkinter.Toplevel(window)
    info_window.title("User Info Creation")
    info_label = ttk.Label(info_window, text="To create a new user, please fill in all the required fields and click the 'Enter the data' button.", wraplength=300)
    info_label.pack(padx=20, pady=20)


window = tkinter.Tk()
window.title("My First GUI Program")

# Main menu
frame = tkinter.Frame(window)
frame.pack()

# A label for the terms and conditions user info frame
user_info_frame = tkinter.LabelFrame(frame, text="User Info")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

# A label for the terms and conditions first name
first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)

# A label for the terms and conditions last name
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

# Create an entry widget for the first name
first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

# Add the info button to the user info frame
title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["Mr.", "Mrs.", "Ms.", "Dr.", "Prof."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

# Add the info button to the user info frame
age_label = tkinter.LabelFrame(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

# Add the info button to the user info frame
nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["USA", "UK", "Germany", "France", "Australia"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

# Add the info button to the user info frame
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Add the info button to the courses frame
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

# Create a label for the check button
registered_label = tkinter.Label(courses_frame, text="Registered Status")

# Create a string variable for the check button
reg_status_var = tkinter.StringVar(value="Not Registered" )
registered_check = tkinter.Checkbutton(courses_frame, text="Registered", variable=reg_status_var, onvalue="Registered", offvalue="Not Registered")

# Add the info button to the courses frame
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

# The label and spinbox for the number of courses
numcourses_label = tkinter.Label(courses_frame, text="Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to=100)
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

# The label and spinbox for the number of semesters
numsemesters_label = tkinter.Label(courses_frame, text="Completed Semesters")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to=100)
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

# A loop to add padding to all the widgets in the frame
for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Create a frame for the terms and conditions
terms_frame = tkinter.LabelFrame(frame, text="Terms and Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

# Create a frame for the output
output_frame = tkinter.LabelFrame(frame, text="Output")
output_frame.grid(row=3, column=0, sticky="news", padx=20, pady=10)

# Create a Text widget for displaying the information
output_text = tkinter.Text(output_frame, wrap="word", height=10, width=50)
output_text.pack(expand=True, fill="both", padx=10, pady=5)

# Create a check button for the terms and conditions
accept_var = tkinter.StringVar(value="Not accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I agree to the terms and conditions", variable=accept_var, onvalue="Accepted", offvalue="Not accepted")

# Create a button to enter the data
terms_check.grid(row=0, column=0)

# Create a button to enter the data
button = tkinter.Button(frame, text="Enter the data", command=enter_data)       # Create a button to enter the data
button.grid(row=4, column=0, sticky="news", padx=20, pady=10)

# Create a button to show the info
info_button = ttk.Button(frame, text="User Info Help", command=show_info)
info_button.grid(row=5, column=0, sticky="news", padx=20, pady=10)


window.mainloop()





