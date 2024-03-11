import tkinter as tk
import sqlite3

# Create a database connection
conn = sqlite3.connect("appointments.db")
cursor = conn.cursor()

# Create the appointments table
cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY,
    patient_name TEXT,
    appointment_date TEXT,
    doctor_name TEXT
)
""")
conn.commit()

# Function to add an appointment
def add_appointment():
    patient_name = patient_entry.get()
    appointment_date = date_entry.get()
    doctor_name = doctor_entry.get()

    cursor.execute("""
    INSERT INTO appointments (patient_name, appointment_date, doctor_name)
    VALUES (?, ?, ?)
    """, (patient_name, appointment_date, doctor_name))
    conn.commit()

# Function to search for an appointment
def search_appointment():
    patient_name = patient_entry.get()
    cursor.execute("""
    SELECT * FROM appointments WHERE patient_name = ?
    """, (patient_name,))
    result = cursor.fetchone()
    if result:
        result_label.config(text=f"Appointment Date: {result[2]}\nDoctor: {result[3]}")
    else:
        result_label.config(text="Appointment not found.")

# Create the main window
root = tk.Tk()
root.title("Medical Appointment Scheduler")

# Widgets
patient_label = tk.Label(root, text="Patient Name:")
patient_entry = tk.Entry(root)
date_label = tk.Label(root, text="Appointment Date:")
date_entry = tk.Entry(root)
doctor_label = tk.Label(root, text="Doctor Name:")
doctor_entry = tk.Entry(root)
add_button = tk.Button(root, text="Add Appointment", command=add_appointment)
search_button = tk.Button(root, text="Search Appointment", command=search_appointment)
result_label = tk.Label(root, text="")

# Grid layout
patient_label.grid(row=0, column=0)
patient_entry.grid(row=0, column=1)
date_label.grid(row=1, column=0)
date_entry.grid(row=1, column=1)
doctor_label.grid(row=2, column=0)
doctor_entry.grid(row=2, column=1)
add_button.grid(row=3, column=0, columnspan=2)
search_button.grid(row=4, column=0, columnspan=2)
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()

# Close the database connection
conn.close()
