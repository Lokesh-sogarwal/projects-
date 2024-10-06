import tkinter
from tkinter import messagebox, Tk, Label, Entry, Button, Frame


class BankAccount:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def get_account_details(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance
        }


class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page using Python")
        self.root.geometry('450x300')
        self.root.configure(bg='lightgrey')
        self.clr = "#3a3b39"

        self.login_label = Label(self.root, text="****---XYZ BANK---****", bg=self.clr, fg="white", font=("Arial", 18),
                                 padx=110, pady=8)
        self.login_label.place(x=0, y=0)

        self.username_label = Label(self.root, text="USERNAME", bg='lightgrey', fg="black", font=("Arial", 16, 'bold'))
        self.username_label.place(x=20, y=80)

        self.password_label = Label(self.root, text="PASSWORD", bg='lightgrey', fg="black", font=("Arial", 16, 'bold'))
        self.password_label.place(x=20, y=120)

        self.username_entry = Entry(self.root, font=("arial", 12))
        self.username_entry.place(x=180, y=80)

        self.password_entry = Entry(self.root, show="*", font=("Arial", 12))
        self.password_entry.place(x=180, y=120)

        self.login_button = Button(self.root, text="Login", bg=self.clr, fg="white", font=("Arial"), command=self.login,
                                   padx=10)
        self.login_button.place(x=110, y=180)

        # Exit button
        self.exit_button = Button(self.root, text="Exit", bg=self.clr, fg="white", font=("Arial"),
                                  command=self.exit_app, padx=15)
        self.exit_button.place(x=250, y=179)

    def login(self):
        username = "Ricky"
        password = "1234"
        if self.username_entry.get() == username and self.password_entry.get() == password:
            messagebox.showinfo(title="Login Successful!", message="You successfully logged in.")
            self.clear_screen()
            BankAccGUI(self.root)
        else:
            messagebox.showerror(title="Error", message="Invalid login.")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def exit_app(self):
        self.root.destroy()


class BankAccGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("BANK MANAGEMENT SYSTEM")
        self.root.geometry("500x300")
        self.root.configure(bg="lightgrey")

        self.account = BankAccount("123456789", "Ankesh", 5000.0)

        self.create_widgets()

    def create_widgets(self):
        self.clr = "#3a3b39"
        self.title_label = Label(self.root, text="***BANK MANAGEMENT SYSTEM***", font=("arial", 14), bg=self.clr,
                                 fg="white", padx=100, pady=10)
        self.title_label.place(x=0, y=0)

        self.balance_button = Button(self.root, text="View Balance", command=self.view_balance, bg=self.clr, fg="white",
                                     font=("arial"), padx=14)
        self.balance_button.place(y=130, x=300)

        self.deposit_button = Button(self.root, text="Deposit", command=self.deposit_money, bg=self.clr, fg="white",
                                     font=("arial"), padx=44)
        self.deposit_button.place(y=130, x=50)

        self.withdraw_button = Button(self.root, text="Withdraw", command=self.withdraw_money, bg=self.clr, fg="white",
                                      font=("arial"), padx=32)
        self.withdraw_button.place(y=80, x=300)

        self.details_button = Button(self.root, text="Customer Details", command=self.show_customer_details,
                                     bg=self.clr, fg="white", font=("arial"))
        self.details_button.place(y=80, x=50)

        # Exit button
        self.exit_button = Button(self.root, text="Exit", bg=self.clr, fg="white", font=("arial"),
                                  command=self.exit_app, padx=39)
        self.exit_button.place(y=200, x=180)

    def view_balance(self):
        balance = self.account.get_balance()
        messagebox.showinfo("Balance", f"Your current balance is: Rs {balance:.2f}")

    def show_customer_details(self):
        self.clear_screen()
        details = self.account.get_account_details()
        details_text = (f"Account Number: {details['account_number']}\n"
                        f"Name: {details['name']}\n"
                        f"Balance: Rs {details['balance']:.2f}")

        self.details_label = Label(self.root, text=details_text, font=("arial", 12), bg="lightgrey")
        self.details_label.pack(pady=10)

        self.back_button = Button(self.root, text="Back", command=self.back_to_main, bg=self.clr, fg="white",
                                  font=("arial"))
        self.back_button.pack(pady=10)

    def deposit_money(self):
        self.clear_screen()
        self.amount_label = Label(self.root, text="Enter amount to deposit:", font=("arial", 12), bg="lightgrey")
        self.amount_label.pack(pady=10)

        self.amount_entry = Entry(self.root)
        self.amount_entry.pack(pady=10)

        self.deposit_button = Button(self.root, text="Deposit", command=self.perform_deposit, bg=self.clr, fg="white",
                                     font=("arial"))
        self.deposit_button.pack(pady=10)

        self.back_button = Button(self.root, text="Back", command=self.back_to_main, bg=self.clr, fg="white",
                                  font=("arial"))
        self.back_button.pack(pady=10)

    def withdraw_money(self):
        self.clear_screen()
        self.amount_label = Label(self.root, text="Enter amount to withdraw:", font=("arial", 12), bg="lightgrey")
        self.amount_label.pack(pady=10)

        self.amount_entry = Entry(self.root)
        self.amount_entry.pack(pady=10)

        self.withdraw_button = Button(self.root, text="Withdraw", command=self.perform_withdraw, bg=self.clr,
                                      fg="white", font=("arial"))
        self.withdraw_button.pack(pady=10)

        self.back_button = Button(self.root, text="Back", command=self.back_to_main, bg=self.clr, fg="white",
                                  font=("arial"))
        self.back_button.pack(pady=10)

    def perform_deposit(self):
        try:
            amount = float(self.amount_entry.get())
            if self.account.deposit(amount):
                messagebox.showinfo("Success", f"Deposited Rs {amount:.2f} successfully")
            else:
                messagebox.showerror("Error", "Invalid deposit amount")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")
        self.back_to_main()

    def perform_withdraw(self):
        try:
            amount = float(self.amount_entry.get())
            if self.account.withdraw(amount):
                messagebox.showinfo("Success", f"Withdrew Rs {amount:.2f} successfully")
            else:
                messagebox.showerror("Error", "Invalid or insufficient funds for withdrawal")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")
        self.back_to_main()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def back_to_main(self):
        self.clear_screen()
        self.create_widgets()

    def exit_app(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    login_page = LoginPage(root)
    root.mainloop()


