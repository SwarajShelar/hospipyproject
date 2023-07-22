import tkinter as tk
from tkinter import ttk
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import messagebox
from tkinter import font
import tkinter.ttk as ttk
from PIL import Image, ImageTk


class HospitalManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("800x600")

        # Database connection
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Database1"
        )

        # Background image
        self.bg_image = Image.open("doc1.jpg")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # label to hold the background image
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Make the label cover the entire window

        # Set the background color to match the image
        self.root.configure(bg="#F0F0F0")

        # Bind the root window's resize event to update the background image
        self.root.bind("<Configure>", self.update_background)

        self.style = ttk.Style()
        self.style.configure("Title.TLabel", font=("Helvetica", 24, "bold"), foreground="midnight blue")
        self.style.configure("Subtitle.TLabel", font=("Helvetica", 16, "bold"), foreground="dark green")
        self.style.configure("TButton", font=("Helvetica", 12, "bold"), foreground="white", relief=tk.RAISED)

        # A consistent color scheme
        self.bg_color = "#F0F0F0"
        self.btn_color = "steel blue"

        # Created a frame for the header with hospital logo or image
        self.header_frame = tk.Frame(self.root, bg=self.bg_color)
        self.header_frame.pack(fill="x", padx=10, pady=5)

        # Created UI elements
        self.label_title = tk.Label(self.root, text="Oscar Hospital", font=("Helvetica", 24, "bold"),
                                    fg="midnight blue")
        self.label_title.pack(pady=20)

        # Created a frame for the tabs
        self.tabs_frame = tk.Frame(self.root, bg=self.bg_color)
        self.tabs_frame.pack(fill="both", expand=True, padx=20, pady=5)

        # Tabs
        self.tabs = ttk.Notebook(self.tabs_frame)
        self.tab_admit = ttk.Frame(self.tabs)
        self.tab_medicines = ttk.Frame(self.tabs)
        self.tabs.add(self.tab_admit, text="Admit Patient")
        self.tabs.add(self.tab_medicines, text="Medicine Storage")
        self.tabs.pack(fill="both", expand=True)

        # Tab: Admit Patient
        self.label_patient = tk.Label(self.tab_admit, text="Patient Admission", font=("Helvetica", 16, "bold"),
                                      fg="dark green")
        self.label_patient.pack(pady=10)

        self.label_name = tk.Label(self.tab_admit, text="Name:", font=("Helvetica", 12))
        self.label_name.pack()
        self.entry_name = tk.Entry(self.tab_admit, font=("Helvetica", 12))
        self.entry_name.pack()

        self.label_surname = tk.Label(self.tab_admit, text="Surname:", font=("Helvetica", 12))  # New field
        self.label_surname.pack()
        self.entry_surname = tk.Entry(self.tab_admit, font=("Helvetica", 12))  # New field
        self.entry_surname.pack()

        self.label_age = tk.Label(self.tab_admit, text="Age:", font=("Helvetica", 12))
        self.label_age.pack()
        self.entry_age = tk.Entry(self.tab_admit, font=("Helvetica", 12))
        self.entry_age.pack()

        self.label_gender = tk.Label(self.tab_admit, text="Gender:", font=("Helvetica", 12))
        self.label_gender.pack()
        self.combo_gender = ttk.Combobox(self.tab_admit, values=["Male", "Female"], font=("Helvetica", 12))
        self.combo_gender.pack()

        self.label_room_type = tk.Label(self.tab_admit, text="Room Type:", font=("Helvetica", 12))
        self.label_room_type.pack()
        self.combo_room_type = ttk.Combobox(self.tab_admit, values=["Single", "Double", "Deluxe"],
                                            font=("Helvetica", 12))
        self.combo_room_type.pack()

        self.label_mobile = tk.Label(self.tab_admit, text="Mobile:", font=("Helvetica", 12))  # New field
        self.label_mobile.pack()
        self.entry_mobile = tk.Entry(self.tab_admit, font=("Helvetica", 12))  # New field
        self.entry_mobile.pack()

        self.label_address = tk.Label(self.tab_admit, text="Address:", font=("Helvetica", 12))  # New field
        self.label_address.pack()
        self.entry_address = tk.Entry(self.tab_admit, font=("Helvetica", 12))  # New field
        self.entry_address.pack()

        self.btn_admit = tk.Button(self.tab_admit, text="Admit Patient", command=self.admit_patient,
                                   font=("Helvetica", 12), bg="light green", fg="black", relief=tk.RAISED)
        self.btn_admit.pack(pady=20)

        # Tab: Room Selection
        self.display_frame = ttk.Frame(self.tabs)
        self.tabs.add(self.display_frame, text="Display Section")
        self.tabs.pack(fill="both", expand=True, padx=20, pady=10)

        # Tab: Medicine Storage
        self.label_med = tk.Label(self.tab_medicines, text="Medicine Storage", font=("Helvetica", 16, "bold"),
                                  fg="maroon")
        self.label_med.pack(pady=10)

        self.label_med_name = tk.Label(self.tab_medicines, text="Medicine Name:", font=("Helvetica", 12))
        self.label_med_name.pack()
        self.entry_med_name = tk.Entry(self.tab_medicines, font=("Helvetica", 12))
        self.entry_med_name.pack()

        self.label_med_description = tk.Label(self.tab_medicines, text="Medicine Description:",
                                              font=("Helvetica", 12))
        self.label_med_description.pack()
        self.text_med_description = tk.Text(self.tab_medicines, height=5, width=30, font=("Helvetica", 12))
        self.text_med_description.pack()

        self.label_med_expiry = tk.Label(self.tab_medicines, text="Expiry Date:", font=("Helvetica", 12))
        self.label_med_expiry.pack()
        self.entry_med_expiry = tk.Entry(self.tab_medicines, font=("Helvetica", 12))
        self.entry_med_expiry.pack()

        self.label_med_price = tk.Label(self.tab_medicines, text="Price:", font=("Helvetica", 12))
        self.label_med_price.pack()
        self.entry_med_price = tk.Entry(self.tab_medicines, font=("Helvetica", 12))
        self.entry_med_price.pack()

        self.btn_store_medicine = tk.Button(self.tab_medicines, text="Store Medicine", command=self.store_medicine,
                                            font=("Helvetica", 12), bg="tomato", fg="white", relief=tk.RAISED)
        self.btn_store_medicine.pack(pady=20)

        # Display Section UI elements
        self.label_display = tk.Label(self.display_frame, text="Display Section", font=("Helvetica", 16, "bold"),
                                      fg="purple")
        self.label_display.pack(pady=10)

        self.display_patients_btn = tk.Button(self.display_frame, text="Display Patients",
                                              command=self.display_patients,
                                              font=("Helvetica", 12), bg="medium orchid", fg="white", relief=tk.RAISED)
        self.display_patients_btn.pack(pady=10)

        self.display_medicines_btn = tk.Button(self.display_frame, text="Display Medicines",
                                               command=self.display_medicines,
                                               font=("Helvetica", 12), bg="dark orange", fg="white", relief=tk.RAISED)
        self.display_medicines_btn.pack(pady=10)

        self.display_data_btn = tk.Button(self.display_frame, text="Data Analysis", command=self.data_analysis,
                                          font=("Helvetica", 12), bg="dark slate gray", fg="white", relief=tk.RAISED)
        self.display_data_btn.pack(pady=10)

        # Display tree for patient and medicine information
        self.display_tree_frame = ttk.Frame(self.display_frame)
        self.display_tree_frame.pack(pady=10, fill="both", expand=True)

        self.display_tree = ttk.Treeview(self.display_tree_frame, show="headings", selectmode="browse")
        self.display_tree["columns"] = (
        "Name", "Surname", "Age", "Gender", "Room Type", "Mobile", "Address", "Medicine Name")
        self.display_tree.heading("#1", text="Name")
        self.display_tree.heading("#2", text="Surname")  # New column
        self.display_tree.heading("#3", text="Age")
        self.display_tree.heading("#4", text="Gender")
        self.display_tree.heading("#5", text="Room Type")
        self.display_tree.heading("#6", text="Mobile")  # New column
        self.display_tree.heading("#7", text="Address")  # New column
        self.display_tree.heading("#8", text="Medicine Name")
        self.display_tree.pack(side=tk.LEFT, fill="both", expand=True)

        # Bind the treeview selection event to show details
        self.display_tree.bind("<ButtonRelease-1>", self.show_details)

        self.display_scrollbar = ttk.Scrollbar(self.display_tree_frame, orient=tk.VERTICAL,
                                               command=self.display_tree.yview)
        self.display_scrollbar.pack(side=tk.RIGHT, fill="y")
        self.display_tree.configure(yscrollcommand=self.display_scrollbar.set)

        # Detail Display Section
        self.detail_display_frame = ttk.Frame(self.display_frame)
        self.detail_display_frame.pack(pady=10, fill="both", expand=True)

        self.label_detail_display = tk.Label(self.detail_display_frame, text="Details", font=("Helvetica", 16, "bold"),
                                             fg="dark blue")
        self.label_detail_display.pack(pady=10)

        self.text_detail_display = tk.Text(self.detail_display_frame, height=5, width=50, font=("Helvetica", 12))
        self.text_detail_display.pack(fill="both", expand=True)

        # Button to clear the detail display section
        self.clear_detail_btn = tk.Button(self.detail_display_frame, text="Clear Details",
                                          command=self.clear_detail_display,
                                          font=("Helvetica", 12), bg="gray", fg="white", relief=tk.RAISED)
        self.clear_detail_btn.pack(pady=10)

        # Applied a consistent font and color to the elements
        self.label_patient.config(font=("Helvetica", 16, "bold"), fg="dark green")
        self.label_med.config(font=("Helvetica", 16, "bold"), fg="maroon")
        self.display_patients_btn.config(font=("Helvetica", 12, "bold"), bg="medium orchid", fg="white",
                                         relief=tk.RAISED)
        self.display_medicines_btn.config(font=("Helvetica", 12, "bold"), bg="dark orange", fg="white",
                                          relief=tk.RAISED)
        self.display_data_btn.config(font=("Helvetica", 12, "bold"), bg="dark slate gray", fg="white", relief=tk.RAISED)
        self.btn_admit.config(font=("Helvetica", 12, "bold"), bg="light green", fg="black", relief=tk.RAISED)
        self.btn_store_medicine.config(font=("Helvetica", 12, "bold"), bg="tomato", fg="white", relief=tk.RAISED)
        self.clear_detail_btn.config(font=("Helvetica", 12, "bold"), bg="gray", fg="white", relief=tk.RAISED)
        self.label_detail_display.config(font=("Helvetica", 16, "bold"), fg="dark blue")

        # Beautify buttons
        self.style.configure("TButton", font=("Helvetica", 12, "bold"), foreground="white",
                             relief=tk.RAISED, background=self.btn_color)
        self.style.map("TButton", foreground=[("active", "white")], background=[("active", "dark blue")])

        # Implement hover effects on buttons
        self.btn_admit.bind("<Enter>", lambda event: self.btn_admit.config(background="dark blue"))
        self.btn_admit.bind("<Leave>", lambda event: self.btn_admit.config(background=self.btn_color))
        self.btn_store_medicine.bind("<Enter>", lambda event: self.btn_store_medicine.config(background="dark red"))
        self.btn_store_medicine.bind("<Leave>", lambda event: self.btn_store_medicine.config(background=self.btn_color))
        self.clear_detail_btn.bind("<Enter>", lambda event: self.clear_detail_btn.config(background="gray"))
        self.clear_detail_btn.bind("<Leave>", lambda event: self.clear_detail_btn.config(background=self.btn_color))

        # Added padding and spacing
        self.label_title.pack(pady=(20, 0))
        self.btn_admit.pack(pady=20)

        # Added a responsive design (optionally)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.tabs_frame.rowconfigure(0, weight=1)
        self.tabs_frame.columnconfigure(0, weight=1)
        self.tab_admit.rowconfigure(4, weight=1)
        self.tab_admit.columnconfigure(1, weight=1)

    def admit_patient(self):
        # Get patient details from the input fields
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        age = self.entry_age.get()
        gender = self.combo_gender.get()
        mobile_number = self.entry_mobile.get()
        address = self.entry_address.get()
        room_type = self.combo_room_type.get()  # Get the selected room type

        # Validate the input
        if not name or not surname or not age or not gender or not mobile_number or not address or not room_type:
            messagebox.showerror("Error", "Please fill in all the fields.")
            return

        # Insert patient details into the database
        try:
            cursor = self.db.cursor()
            sql = "INSERT INTO patients (name, surname, age, gender, mobile_number, address) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (name, surname, age, gender, mobile_number, address)
            cursor.execute(sql, values)
            self.db.commit()

            # Get the last inserted patient ID
            patient_id = cursor.lastrowid

            cursor.close()
            messagebox.showinfo("Success", "Patient admitted successfully!")

            # Book the room for the admitted patient
            self.book_room(patient_id, room_type)

            # Clear input fields after successful admission
            self.clear_input_fields()

            # Display updated patient data
            self.display_patients()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error while admitting patient: {err}")

    def select_room(self):
        # Create a new window for room selection
        room_window = tk.Toplevel(self.root)
        room_window.title("Room Selection")
        room_window.geometry("400x200")

        # Create UI elements in the room selection window
        label_title = tk.Label(room_window, text="Select Room Type", font=("Helvetica", 16))
        label_title.pack()

        combo_room_type = ttk.Combobox(room_window, values=["Single", "Double", "Deluxe"])
        combo_room_type.pack()

        btn_select = tk.Button(room_window, text="Select Room", command=lambda: self.book_room(room_window,
                                                                                               combo_room_type.get()))
        btn_select.pack()

    def book_room(self, patient_id, room_type):
        # Check if the patient has already booked a room
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT * FROM room_bookings WHERE patient_id = %s", (patient_id,))
            booking_exists = cursor.fetchone()
            cursor.close()

            if booking_exists:
                messagebox.showinfo("Info", "Patient has already booked a room.")
            else:
                # Insert room booking details into the database
                cursor = self.db.cursor()
                sql = "INSERT INTO room_bookings (patient_id, room_type) VALUES (%s, %s)"
                values = (patient_id, room_type)
                cursor.execute(sql, values)
                self.db.commit()
                cursor.close()

                messagebox.showinfo("Success", "Room booked successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error while booking room: {err}")

    def save_booking(self, patient_id, room_type, room_window):
        # Function to save the room booking details in the database

        # Insert room booking details into the database
        try:
            cursor = self.db.cursor()
            sql = "INSERT INTO room_bookings (patient_id, room_type) VALUES (%s, %s)"
            values = (patient_id, room_type)
            cursor.execute(sql, values)
            self.db.commit()
            cursor.close()
            messagebox.showinfo("Success", "Room booked successfully!")
            room_window.destroy()  # Close the room selection window after booking
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error while booking room: {err}")

    def store_medicine(self):
        # Get medicine details from the input fields
        name = self.entry_med_name.get()
        description = self.text_med_description.get("1.0", "end-1c")
        expiry = self.entry_med_expiry.get()
        price = self.entry_med_price.get()

        # Validate the input
        if not name or not description or not expiry or not price:
            messagebox.showerror("Error", "Please fill in all the fields.")
            return

        # Insert medicine details into the database
        try:
            cursor = self.db.cursor()
            sql = "INSERT INTO medicines (name, description, expiry, price) VALUES (%s, %s, %s, %s)"
            values = (name, description, expiry, price)
            cursor.execute(sql, values)
            self.db.commit()
            cursor.close()
            messagebox.showinfo("Success", "Medicine details stored successfully!")
            self.clear_medicine_input_fields()  # Clear input fields after successful storage
            # Display updated medicine data after storing medicine
            self.display_medicines()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error while storing medicine details: {err}")

    def display_patients(self):
        # Clear the display tree
        self.display_tree.delete(*self.display_tree.get_children())

        # Fetch patient information from the database
        try:
            cursor = self.db.cursor()
            cursor.execute(
                "SELECT patients.id, patients.name, patients.surname, patients.age, patients.gender, patients.mobile_number, patients.address, room_bookings.room_type "
                "FROM patients LEFT JOIN room_bookings ON patients.id = room_bookings.patient_id")
            patients_data = cursor.fetchall()
            cursor.close()

            # Insert patient data into the Treeview with respective columns
            for patient in patients_data:
                self.display_tree.insert("", "end", values=(
                    patient[1], patient[2], patient[3], patient[4], patient[5], patient[6], patient[7]))
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error while fetching patient information: {err}")

        self.display_tree["columns"] = ("Name", "Surname", "Age", "Gender", "Mobile Number", "Address", "Room Type")
        self.display_tree.heading("#1", text="Name")
        self.display_tree.heading("#2", text="Surname")
        self.display_tree.heading("#3", text="Age")
        self.display_tree.heading("#4", text="Gender")
        self.display_tree.heading("#5", text="Mobile Number")
        self.display_tree.heading("#6", text="Address")
        self.display_tree.heading("#7", text="Room Type")

    def display_medicines(self):
        # Clear the display tree
        self.display_tree.delete(*self.display_tree.get_children())

        # Fetch medicine information from the database
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT name, description, expiry, price FROM medicines")
            medicines_data = cursor.fetchall()
            cursor.close()

            # Insert medicine data into the Treeview with respective columns
            for medicine in medicines_data:
                self.display_tree.insert("", "end", values=(medicine[0], medicine[1], medicine[2], medicine[3]))
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error while fetching medicine information: {err}")

        # Reset the columns for medicines
        self.display_tree["columns"] = ("Medicine Name", "Medicine Description", "Expiry Date", "Price")
        self.display_tree.heading("#1", text="Medicine Name")
        self.display_tree.heading("#2", text="Medicine Description")
        self.display_tree.heading("#3", text="Expiry Date")
        self.display_tree.heading("#4", text="Price")

    def data_analysis(self):
        # Fetch patient age data from the database
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT age FROM patients")
            age_data = cursor.fetchall()
            cursor.close()

            if not age_data:
                messagebox.showinfo("Info", "No patient data available for analysis.")
                return

            # Convert the fetched data to a Pandas DataFrame
            df = pd.DataFrame(age_data, columns=["Age"])

            # Perform data analysis
            avg_age = df["Age"].mean()
            max_age = df["Age"].max()
            min_age = df["Age"].min()

            # Create a histogram to visualize age distribution
            plt.figure(figsize=(8, 6))
            plt.hist(df["Age"], bins=10, color="skyblue", edgecolor="black")
            plt.xlabel("Age")
            plt.ylabel("Frequency")
            plt.title("Age Distribution")
            plt.grid(True)
            plt.show()

            # Display analysis results
            messagebox.showinfo("Data Analysis",
                                f"Average Age: {avg_age:.2f}\nMaximum Age: {max_age}\nMinimum Age: {min_age}")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error while performing data analysis: {err}")

    def show_details(self, event):
        # Get the selected item from the tree
        selected_item = self.display_tree.focus()
        item_data = self.display_tree.item(selected_item)

        # Get the patient details from the selected item
        patient_name = item_data["values"][0]
        age = item_data["values"][1]
        gender = item_data["values"][2]
        room_type = item_data["values"][3]

        # Show detailed information in the Detail Display Section
        details_text = f"Name: {patient_name}\n" \
                       f"Age: {age}\n" \
                       f"Gender: {gender}\n" \
                       f"Room Type: {room_type}"

        self.show_detail_display(details_text)

    def show_detail_display(self, details_text):
        # Show detailed information of the selected patient in the Detail Display Section
        self.text_detail_display.delete("1.0", "end")
        self.text_detail_display.insert("1.0", details_text)

    def clear_detail_display(self):
        # Clear the Detail Display Section
        self.text_detail_display.delete("1.0", "end")

    def clear_input_fields(self):
        self.entry_name.delete(0, tk.END)
        self.entry_surname.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.combo_gender.set("")  # Clear the combobox selection
        self.entry_mobile.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)
        self.combo_room_type.set("")  # Clear the combobox selection

    def clear_medicine_input_fields(self):
        self.entry_med_name.delete(0, tk.END)
        self.text_med_description.delete("1.0", tk.END)
        self.entry_med_expiry.delete(0, tk.END)
        self.entry_med_price.delete(0, tk.END)
        
    def update_background(self, event):
        bg_width = event.width
        bg_height = event.height
        self.bg_photo = ImageTk.PhotoImage(self.bg_image.resize((bg_width, bg_height)))
        self.bg_label.configure(image=self.bg_photo)


if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalManagementSystem(root)
    app.display_patients()  # Display existing patients' data when the application starts
    app.display_medicines()
    root.mainloop()
