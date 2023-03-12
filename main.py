import tkinter as tk
from tkinter import messagebox

class DataEntrySoftware:

    def __init__(self, master):
        self.master = master
        master.title("Data Entry Software")

        # Name
        self.label_name = tk.Label(master, text="Name:")
        self.label_name.grid(row=0, column=0)

        self.entry_name = tk.Entry(master)
        self.entry_name.grid(row=0, column=1)

        # Last Name
        self.label_last_name = tk.Label(master, text="Last Name:")
        self.label_last_name.grid(row=1, column=0)

        self.entry_last_name = tk.Entry(master)
        self.entry_last_name.grid(row=1, column=1)

        # Email
        self.label_email = tk.Label(master, text="Email:")
        self.label_email.grid(row=2, column=0)

        self.entry_email = tk.Entry(master)
        self.entry_email.grid(row=2, column=1)

        # Password
        self.label_password = tk.Label(master, text="Password:")
        self.label_password.grid(row=3, column=0)

        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.grid(row=3, column=1)

        # Phone Number
        self.label_phone = tk.Label(master, text="Phone Number:")
        self.label_phone.grid(row=4, column=0)

        self.entry_phone = tk.Entry(master)
        self.entry_phone.grid(row=4, column=1)

        # Address
        self.label_address = tk.Label(master, text="Address:")
        self.label_address.grid(row=5, column=0)

        self.entry_address = tk.Entry(master)
        self.entry_address.grid(row=5, column=1)

        # Submit Button
        self.button_submit = tk.Button(master, text="Submit", command=self.submit)
        self.button_submit.grid(row=6, column=0, columnspan=2)

    def submit(self):
        name = self.entry_name.get()
        last_name = self.entry_last_name.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        phone = self.entry_phone.get()
        address = self.entry_address.get()

        # Save the data to a text file
        try:
            with open(f"{name}_{last_name}.txt", "w") as f:
                f.write(f"Name: {name}\nLast Name: {last_name}\nEmail: {email}\nPassword: {password}\nPhone Number: {phone}\nAddress: {address}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data to file: {e}")
            return

        # Show success message
        messagebox.showinfo("Success", "Data saved to file.")

        # Clear the entry fields
        self.entry_name.delete(0, tk.END)
        self.entry_last_name.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    app = DataEntrySoftware(root)
    root.mainloop()
