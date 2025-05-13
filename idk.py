"""
A Most Ingenious Number-Guessing Contrivance
Authored this 4th Day of July, 1776
By one Ebenezer Codsworth, Esq.
"""

import tkinter as tk
from tkinter import messagebox
import random
import ctypes
import os
import subprocess

class SystemGuardian:
    def __init__(self):
        self.correct_number = random.randint(1, 10)
        self.access_granted = False
        self.attempts_remaining = 3
        
    def verify_guess(self, guess):
        """Perform the numerical verification with utmost precision"""
        try:
            numerical_guess = int(guess)
            if 1 <= numerical_guess <= 10:
                if numerical_guess == self.correct_number:
                    return True
                else:
                    self.attempts_remaining -= 1
                    return False
            else:
                raise ValueError("Number out of bounds")
        except ValueError:
            raise ValueError("That's not a proper number, good sir!")

    def lock_system(self):
        """Engage the system's protective measures"""
        try:
            # For Windows systems
            ctypes.windll.user32.BlockInput(True)
            messagebox.showerror("Access Denied", "The system remains locked!")
        except:
            # For other systems
            messagebox.showerror("Access Denied", "The system remains locked!")

    def unlock_system(self):
        """Release the system's protective measures"""
        try:
            # For Windows systems
            ctypes.windll.user32.BlockInput(False)
        except:
            pass
        self.access_granted = True
        messagebox.showinfo("Access Granted", "You may now proceed!")

def on_submit():
    """Handler for the submit button action"""
    guess = entry.get()
    try:
        if guardian.verify_guess(guess):
            guardian.unlock_system()
            root.destroy()
            # Launch the system's application menu
            subprocess.Popen("explorer.exe" if os.name == 'nt' else "open /")
        else:
            if guardian.attempts_remaining > 0:
                messagebox.showwarning("Incorrect", 
                    f"Wrong! {guardian.attempts_remaining} attempts remain!")
            else:
                guardian.lock_system()
                root.destroy()
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Initialize our protective guardian
guardian = SystemGuardian()

# Create the main window with colonial aesthetics
root = tk.Tk()
root.title("System Access Portal")
root.geometry("350x200")

# Decorative elements
frame = tk.Frame(root, bd=2, relief="groove")
frame.pack(padx=10, pady=10, fill="both", expand=True)

label = tk.Label(frame, text="Present Your Numerical Credential\n(1 through 10)", 
                 font=("Times New Roman", 12))
label.pack(pady=15)

entry = tk.Entry(frame, font=("Times New Roman", 12), justify="center")
entry.pack(pady=5)

submit_button = tk.Button(frame, text="Seek Admission", command=on_submit,
                         font=("Times New Roman", 10))
submit_button.pack(pady=10)

warning = tk.Label(frame, 
    text="Three failed attempts shall bar your passage!", 
    fg="red", font=("Times New Roman", 9))
warning.pack(side="bottom", pady=5)

root.mainloop()
