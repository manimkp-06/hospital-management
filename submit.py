import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import datetime

def greet(entry_patient_name, entry_patient_email, entry_patient_phone, entry_appointment_date, entry_appointment_time, entry_appointment_reason, doctor_gender, entry_doctor_name):
    patient_name = entry_patient_name.get()
    patient_email = entry_patient_email.get()
    phone_number = entry_patient_phone.get()
    if len(phone_number) == 10:
        print(f"Patient Phone: {phone_number}")
    else:
        messagebox.showerror("Invalid input", "Please enter a 10-digit phone number.")
    appointment_date = entry_appointment_date.get()
    appointment_time = entry_appointment_time.get()
    appointment_reason = entry_appointment_reason.get()
    gender = doctor_gender.get()
    
    if gender == "Male":
        if appointment_reason == "Neuro":
            doctor_name = "Dr. Sivaraman"
        elif appointment_reason == "Cardiology":
            doctor_name = "Dr. Mathavan"
        elif appointment_reason == "Counseling":
            doctor_name = "Dr.Johnson"
        elif appointment_reason == "Dialysis":
            doctor_name = "Dr.Arunkumar"
        else:
            doctor_name = "Dr.Gowtham"
    elif gender == "Female":
        if appointment_reason == "Neuro":
            doctor_name = "Dr.Priya"
        elif appointment_reason == "Cardiology":
            doctor_name = "Dr.Swetha"
        elif appointment_reason == "Counseling":
            doctor_name = "Dr.Saranya"
        elif appointment_reason == "Dialysis":
            doctor_name = "Dr.Vinothini"
        else:
            doctor_name = "Dr.Julie"

    entry_doctor_name.delete(0, tk.END)
    entry_doctor_name.insert(0, doctor_name)

    messagebox.showinfo("Appointment Confirmed", f'Thank you, {patient_name}. Your appointment is confirmed with {doctor_name} on {appointment_date} at {appointment_time}.')

def validate_phone_number(new_value):
   
    return new_value.isdigit() and len(new_value) <= 10

def open_appointment_window():
    appointment_window = tk.Toplevel(root)
    appointment_window.title("Patient Online Appointment")
    
    tk.Label(appointment_window, text="Patient Name:",font=("Times New Roman", 20)).grid(row=0, column=0, padx=10, pady=5)
    entry_patient_name = tk.Entry(appointment_window)
    entry_patient_name.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(appointment_window, text="Patient Email:",font=("Times New Roman", 20)).grid(row=1, column=0, padx=10, pady=5)
    entry_patient_email = tk.Entry(appointment_window)
    entry_patient_email.grid(row=1, column=1, padx=10, pady=5)
    entry_patient_email.insert(0, "@email.com")

    tk.Label(appointment_window, text="Patient Phone:",font=("Times New Roman", 20)).grid(row=2, column=0, padx=10, pady=5)
    validate_cmd = appointment_window.register(validate_phone_number)
    entry_patient_phone = tk.Entry(appointment_window, validate="key", validatecommand=(validate_cmd, '%P'))
    entry_patient_phone.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(appointment_window, text="Reason for Appointment:",font=("Times New Roman", 20)).grid(row=3, column=0, padx=10, pady=5)
    entry_appointment_reason = ttk.Combobox(appointment_window, values=["Neuro", "Cardiology", "Counseling", "Dialysis"], height=4, width=30)
    entry_appointment_reason.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(appointment_window, text="Doctor Gender:",font=("Times New Roman", 20)).grid(row=4, column=0, padx=10, pady=5)
    doctor_gender = tk.StringVar()
    tk.Radiobutton(appointment_window, text="Male", variable=doctor_gender, value="Male").grid(row=4, column=1, padx=10, pady=5)
    tk.Radiobutton(appointment_window, text="Female", variable=doctor_gender, value="Female").grid(row=4, column=2, padx=10, pady=5)

    tk.Label(appointment_window, text="Doctor Name:",font=("Times New Roman", 20)).grid(row=5, column=0, padx=10, pady=5)
    entry_doctor_name = tk.Entry(appointment_window)
    entry_doctor_name.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(appointment_window, text="Appointment Date:",font=("Times New Roman", 20)).grid(row=6, column=0, padx=10, pady=5)
    entry_appointment_date = ttk.Combobox(appointment_window, values=[datetime.date.today().strftime("%Y-%m-%d")])
    entry_appointment_date.grid(row=6, column=1, padx=10, pady=5)

    tk.Label(appointment_window, text="Appointment Time:",font=("Times New Roman", 20)).grid(row=7, column=0, padx=10, pady=5)
    entry_appointment_time = ttk.Combobox(appointment_window, values=["10:00 AM", "11:00 AM", "02:00 PM", "03:00 PM"])
    entry_appointment_time.grid(row=7, column=1, padx=10, pady=5)

    submit_button = tk.Button(appointment_window, text="Submit Appointment",font=("Times New Roman", 20), command=lambda: greet(entry_patient_name, entry_patient_email, entry_patient_phone, entry_appointment_date, entry_appointment_time, entry_appointment_reason, doctor_gender, entry_doctor_name))
    submit_button.grid(row=8, columnspan=2, pady=10)

    appointment_window.mainloop()


root = tk.Tk()
root.title("AR Hospital")
tk.Label(root, text="AR Hospital", font=("Times New Roman", 30), fg="blue").grid(row=2, column=0, columnspan=3, padx=20, pady=20)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

tk.Button(root, text="Patient Online Appointment", font=("Times New Roman", 15), command=open_appointment_window).grid(row=4, column=0, columnspan=3, padx=20, pady=20)

root.mainloop()
