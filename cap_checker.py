import time
from Xlib import display, X
import tkinter as tk

# Function to check if Caps Lock is on
def is_caps_lock_on():
    d = display.Display()
    root = d.screen().root
    keys = root.query_pointer()._data["mask"]
    return (keys & X.LockMask) != 0

# Function to create the on-screen indicator
def show_capslock_indicator():
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.attributes("-alpha", 0.5)  # Set the opacity (0.0 to 1.0)
    
    screen_width = root.winfo_screenwidth()
    indicator_width = 150  # Width of the indicator
    margin_right = 30  # Margin from the right edge of the screen
    position_x = screen_width - indicator_width - margin_right
    
    root.geometry(f"{indicator_width}x70+{position_x}+30")  # Position with right margin
    root.configure(bg="#4f4f4f")  # Background color to gray
    
    # Label with padding and custom font
    label = tk.Label(root, text="CAPS LOCK ON", fg="white", bg="#4f4f4f", font=("Sans", 13))
    label.pack(expand=True, padx=10, pady=10)
    label.pack(fill=tk.BOTH, expand=1)
    
    while True:
        if not is_caps_lock_on():
            root.destroy()
            break
        root.update()
        time.sleep(0.1)

    root.mainloop()

# Main loop to check Caps Lock status
def monitor_capslock():
    caps_on = False
    while True:
        if is_caps_lock_on() and not caps_on:
            show_capslock_indicator()
            caps_on = True
        elif not is_caps_lock_on():
            caps_on = False

if __name__ == "__main__":
    monitor_capslock()
