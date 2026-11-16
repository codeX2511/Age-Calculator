
import tkinter as tk
from tkinter import messagebox
from datetime import date
import calendar

# 🎨 Main Window
root = tk.Tk()
root.title("🎂 My Age Calculator")
root.geometry("520x700")
root.configure(bg="#10172A")
root.resizable(False, False)

# Colors
BG = "#10172A"
CARD = "#1D2942"
GOLD = "#FFD166"
WHITE = "#FFFFFF"
CYAN = "#48CAE4"
PINK = "#FF70A6"

# 🌟 Heading
tk.Label(
    root,
    text="🎂 AGE CALCULATOR",
    font=("Arial", 25, "bold"),
    bg=BG,
    fg=GOLD
).pack(pady=(25, 5))

tk.Label(
    root,
    text="✨ Discover Your Beautiful Journey ✨",
    font=("Arial", 12),
    bg=BG,
    fg="#B8C7E0"
).pack(pady=5)

# 📅 Input Card
input_card = tk.Frame(root, bg=CARD, padx=20, pady=20)
input_card.pack(padx=25, pady=20, fill="x")

tk.Label(
    input_card,
    text="📅 Enter Your Date of Birth",
    font=("Arial", 15, "bold"),
    bg=CARD,
    fg=WHITE
).pack(pady=10)

entry_frame = tk.Frame(input_card, bg=CARD)
entry_frame.pack(pady=10)

def create_entry(parent, label):
    box = tk.Frame(parent, bg=CARD)
    box.pack(side="left", padx=8)

    tk.Label(
        box, text=label,
        bg=CARD, fg=CYAN,
        font=("Arial", 11, "bold")
    ).pack()

    entry = tk.Entry(
        box, width=8,
        font=("Arial", 14),
        justify="center",
        bg="#EAF2FF",
        fg="#10172A",
        relief="flat"
    )
    entry.pack(ipady=7, pady=5)
    return entry

day_entry = create_entry(entry_frame, "DAY")
month_entry = create_entry(entry_frame, "MONTH")
year_entry = create_entry(entry_frame, "YEAR")

# 📊 Result Card
result_card = tk.Frame(root, bg=CARD, padx=15, pady=15)
result_card.pack(padx=25, fill="x")

tk.Label(
    result_card,
    text="💖 YOUR CURRENT AGE",
    font=("Arial", 15, "bold"),
    bg=CARD,
    fg=GOLD
).pack(pady=8)

age_label = tk.Label(
    result_card,
    text="🎉  -- Years  |  -- Months  |  -- Days",
    font=("Arial", 13, "bold"),
    bg=CARD,
    fg=WHITE,
    wraplength=430
)
age_label.pack(pady=15)

tk.Frame(result_card, bg="#43516D", height=2).pack(fill="x", pady=8)

birthday_label = tk.Label(
    result_card,
    text="🎁 Your Birthday Countdown",
    font=("Arial", 17, "bold"),
    bg=CARD,
    fg=PINK
)
birthday_label.pack(pady=12)

birthday_date_label = tk.Label(
    result_card,
    text="✨ Calculate to see your birthday!",
    font=("Arial", 12),
    bg=CARD,
    fg=WHITE
)
birthday_date_label.pack(pady=5)

# 🎯 Calculate Function
def calculate_age():
    try:
        d = int(day_entry.get())
        m = int(month_entry.get())
        y = int(year_entry.get())

        dob = date(y, m, d)
        today = date.today()

        if dob > today:
            messagebox.showerror(
                "Oops! ❌",
                "Birth date cannot be in the future!"
            )
            return

        # Age Calculation
        years = today.year - y
        months = today.month - m
        days = today.day - d

        if days < 0:
            months -= 1

            if today.month == 1:
                pm, py = 12, today.year - 1
            else:
                pm, py = today.month - 1, today.year

            days += calendar.monthrange(py, pm)[1]

        if months < 0:
            years -= 1
            months += 12

        # Next Birthday
        next_year = today.year

        if (today.month, today.day) >= (m, d):
            next_year += 1

        next_day = min(
            d, calendar.monthrange(next_year, m)[1]
        )

        next_birthday = date(next_year, m, next_day)
        remaining = (next_birthday - today).days

        # Display Age
        age_label.config(
            text=f"🎉 {years} Years  |  {months} Months  |  {days} Days"
        )

        # Birthday Countdown
        if remaining == 0:
            birthday_label.config(
                text="🥳 HAPPY BIRTHDAY! 🎂",
                fg=GOLD
            )
        else:
            birthday_label.config(
                text=f"🎁 {remaining} DAYS LEFT!",
                fg=PINK
            )

        birthday_date_label.config(
            text=f"🎈 Birthday Date: {next_birthday.strftime('%d %B %Y')}"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input ❌",
            "Please enter a valid date!\nExample: 15 / 08 / 2005"
        )

# 🔄 Reset Function
def reset():
    day_entry.delete(0, tk.END)
    month_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)

    age_label.config(
        text="🎉  -- Years  |  -- Months  |  -- Days"
    )
    birthday_label.config(
        text="🎁 Your Birthday Countdown",
        fg=PINK
    )
    birthday_date_label.config(
        text="✨ Calculate to see your birthday!"
    )

# Buttons
button_frame = tk.Frame(root, bg=BG)
button_frame.pack(pady=20)

tk.Button(
    button_frame,
    text="✨ CALCULATE",
    command=calculate_age,
    bg=GOLD,
    fg="#10172A",
    font=("Arial", 13, "bold"),
    relief="flat",
    cursor="hand2",
    padx=22,
    pady=12
).pack(side="left", padx=10)

tk.Button(
    button_frame,
    text="🔄 RESET",
    command=reset,
    bg="#344563",
    fg=WHITE,
    font=("Arial", 13, "bold"),
    relief="flat",
    cursor="hand2",
    padx=22,
    pady=12
).pack(side="left", padx=10)

# Footer
tk.Label(
    root,
    text="💝 Made By Divya",
    font=("Arial", 11, "italic"),
    bg=BG,
    fg="#A8B8D0"
).pack(side="bottom", pady=18)

root.mainloop()
