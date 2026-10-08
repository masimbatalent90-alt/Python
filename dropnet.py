import tkinter as tk
from tkinter import messagebox
import random

# Global data storage
ALL_USERS = {}
ALL_STORES = [
    {"name": "PP Store", "owner": "pp_owner"},
    {"name": "Enrichwards", "owner": "enrich_owner"}
]

class DropnetTkApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DROPNET")
        self.geometry("380x640")
        self.configure(bg="#1e1e1e")

        self.pending_user = {}
        self.current_user = {}
        self.generated_code = ""

        # Container frame for holding all screens
        self.container = tk.Frame(self, bg="#1e1e1e")
        self.container.pack(fill="both", expand=True)

        self.show_splash()

    def clear_screen(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    # --- SCREEN 1: Splash Screen ---
    def show_splash(self):
        self.clear_screen()
        
        lbl_title = tk.Label(self.container, text="DROPNET", font=("Helvetica", 24, "bold"), fg="#ffffff", bg="#1e1e1e")
        lbl_title.pack(pady=(80, 20))

        lbl_quote = tk.Label(self.container, text='"Quote of the day:\nInnovate your business"', font=("Helvetica", 12, "italic"), fg="#cccccc", bg="#1e1e1e")
        lbl_quote.pack(pady=20)

        btn = tk.Button(self.container, text="Continue", font=("Helvetica", 12), bg="#007acc", fg="#ffffff", command=self.show_simulation)
        btn.pack(pady=40, ipadx=20, ipady=5)

    # --- SCREEN 2: Simulation Screen ---
    def show_simulation(self):
        self.clear_screen()
        
        lbl = tk.Label(self.container, text="App Simulation & Customization", font=("Helvetica", 16, "bold"), fg="#ffffff", bg="#1e1e1e")
        lbl.pack(pady=30)

        lbl_sub = tk.Label(self.container, text="Experience local stores, ad displays,\nand inventory tracking.", font=("Helvetica", 11), fg="#cccccc", bg="#1e1e1e")
        lbl_sub.pack(pady=10)

        btn = tk.Button(self.container, text="View Terms & Conditions", bg="#007acc", fg="#ffffff", command=self.show_terms)
        btn.pack(pady=30, ipadx=10, ipady=5)

    # --- SCREEN 3: Terms Screen ---
    def show_terms(self):
        self.clear_screen()
        
        lbl = tk.Label(self.container, text="Terms and Conditions", font=("Helvetica", 16, "bold"), fg="#ffffff", bg="#1e1e1e")
        lbl.pack(pady=20)

        terms_text = "1. Respect community guidelines.\n2. Provide accurate product details."
        lbl_body = tk.Label(self.container, text=terms_text, font=("Helvetica", 11), fg="#cccccc", bg="#1e1e1e", justify="left")
        lbl_body.pack(pady=20)

        btn = tk.Button(self.container, text="Agree and Continue", bg="#28a745", fg="#ffffff", command=self.show_auth_choice)
        btn.pack(pady=30, ipadx=10, ipady=5)

    # --- SCREEN 4: Auth Choice ---
    def show_auth_choice(self):
        self.clear_screen()

        lbl = tk.Label(self.container, text="Welcome to Dropnet", font=("Helvetica", 18, "bold"), fg="#ffffff", bg="#1e1e1e")
        lbl.pack(pady=40)

        btn_signup = tk.Button(self.container, text="Sign Up", font=("Helvetica", 12), bg="#007acc", fg="#ffffff", command=self.show_signup)
        btn_signup.pack(pady=10, fill="x", padx=40)

        btn_signin = tk.Button(self.container, text="Sign In", font=("Helvetica", 12), bg="#6c757d", fg="#ffffff", command=self.show_signin)
        btn_signin.pack(pady=10, fill="x", padx=40)

    # --- SCREEN 5: Sign Up ---
    def show_signup(self):
        self.clear_screen()

        tk.Label(self.container, text="Create Account", font=("Helvetica", 16, "bold"), fg="#ffffff", bg="#1e1e1e").pack(pady=10)

        ent_user = tk.Entry(self.container)
        ent_user.insert(0, "Username")
        ent_user.pack(pady=5)

        ent_pass = tk.Entry(self.container, show="*")
        ent_pass.insert(0, "Password")
        ent_pass.pack(pady=5)

        ent_email = tk.Entry(self.container)
        ent_email.insert(0, "Email Address")
        ent_email.pack(pady=5)

        ent_phone = tk.Entry(self.container)
        ent_phone.insert(0, "Phone Number")
        ent_phone.pack(pady=5)

        def process_signup():
            if len(ent_pass.get()) < 8:
                messagebox.showerror("Error", "Password must be at least 8 characters!")
                return

            self.pending_user = {
                "username": ent_user.get(),
                "password": ent_pass.get(),
                "email": ent_email.get(),
                "phone": ent_phone.get()
            }
            self.generated_code = str(random.randint(100000, 999999))
            print(f"[DEBUG] Code Sent: {self.generated_code}")
            messagebox.showinfo("Verification", f"Code sent to terminal: {self.generated_code}")
            self.show_verify()

        btn = tk.Button(self.container, text="Submit & Send Code", bg="#28a745", fg="#ffffff", command=process_signup)
        btn.pack(pady=20)

    # --- SCREEN 6: Sign In ---
    def show_signin(self):
        self.clear_screen()

        tk.Label(self.container, text="Sign In", font=("Helvetica", 16, "bold"), fg="#ffffff", bg="#1e1e1e").pack(pady=20)

        ent_user = tk.Entry(self.container)
        ent_user.insert(0, "Username")
        ent_user.pack(pady=5)

        ent_pass = tk.Entry(self.container, show="*")
        ent_pass.pack(pady=5)

        def process_signin():
            user = ALL_USERS.get(ent_user.get())
            if user and user["password"] == ent_pass.get():
                self.current_user = user
                self.show_goals()
            else:
                messagebox.showerror("Error", "Invalid credentials!")

        btn = tk.Button(self.container, text="Sign In", bg="#007acc", fg="#ffffff", command=process_signin)
        btn.pack(pady=20)

    # --- SCREEN 7: Verification ---
    def show_verify(self):
        self.clear_screen()

        tk.Label(self.container, text="Enter 6-Digit Code", font=("Helvetica", 14, "bold"), fg="#ffffff", bg="#1e1e1e").pack(pady=20)

        ent_code = tk.Entry(self.container)
        ent_code.pack(pady=10)

        def verify():
            if ent_code.get() == self.generated_code:
                ALL_USERS[self.pending_user["username"]] = self.pending_user
                self.current_user = self.pending_user
                messagebox.showinfo("Success", "Verified Successfully!")
                self.show_goals()
            else:
                messagebox.showerror("Error", "Incorrect Code!")

        btn = tk.Button(self.container, text="Verify", bg="#28a745", fg="#ffffff", command=verify)
        btn.pack(pady=10)

    # --- SCREEN 8: Goals ---
    def show_goals(self):
        self.clear_screen()

        tk.Label(self.container, text="Tell us your goals with this app", font=("Helvetica", 12), fg="#ffffff", bg="#1e1e1e").pack(pady=20)

        txt_goals = tk.Text(self.container, height=4, width=25)
        txt_goals.pack(pady=10)

        btn = tk.Button(self.container, text="Continue", bg="#007acc", fg="#ffffff", command=self.show_store_options)
        btn.pack(pady=20)

    # --- SCREEN 9: Store Options ---
    def show_store_options(self):
        self.clear_screen()

        tk.Label(self.container, text="Select Store Option", font=("Helvetica", 16, "bold"), fg="#ffffff", bg="#1e1e1e").pack(pady=20)

        btn_create = tk.Button(self.container, text="Create Store With Us", bg="#007acc", fg="#ffffff", command=self.show_create_store)
        btn_create.pack(pady=10, fill="x", padx=40)

        btn_customer = tk.Button(self.container, text="Continue as Customer", bg="#6c757d", fg="#ffffff", command=self.show_main_app)
        btn_customer.pack(pady=10, fill="x", padx=40)

    # --- SCREEN 10: Create Store ---
    def show_create_store(self):
        self.clear_screen()

        tk.Label(self.container, text="Create Store", font=("Helvetica", 16, "bold"), fg="#ffffff", bg="#1e1e1e").pack(pady=10)

        ent_store = tk.Entry(self.container)
        ent_store.insert(0, "Store Name")
        ent_store.pack(pady=5)

        def save():
            if ent_store.get():
                ALL_STORES.append({"name": ent_store.get(), "owner": "current_user"})
                self.show_main_app()

        btn = tk.Button(self.container, text="Save Store", bg="#28a745", fg="#ffffff", command=save)
        btn.pack(pady=20)

    # --- SCREEN 11: Main Shell & 4-Button Nav ---
    def show_main_app(self):
        self.clear_screen()

        # Header
        lbl_head = tk.Label(self.container, text="DROPNET", font=("Helvetica", 18, "bold"), fg="#ffffff", bg="#333333")
        lbl_head.pack(fill="x", ipady=10)

        # Dynamic View Area
        view_area = tk.Label(self.container, text="", font=("Helvetica", 11), fg="#ffffff", bg="#1e1e1e", justify="left")
        view_area.pack(expand=True, fill="both", pady=10, padx=10)

        def load_view(name):
            if name == "ads":
                view_area.config(text="-- Advertisement Feed --\n\nFeatured Ad: Premium Wood Table\nStore Rating: 8/10 (High Efficiency)\nInterested People: 42")
            elif name == "stores":
                stores_text = "-- Local Stores Signed In --\n\n" + "\n".join([f"• {s['name']} (Available)" for s in ALL_STORES])
                view_area.config(text=stores_text)
            elif name == "leaderboard":
                view_area.config(text="-- Top Stores Leaderboard --\n\n1. PP Store - 9.8/10\n2. Enrichwards - 9.2/10")
            elif name == "profile":
                username = self.current_user.get("username", "Guest")
                view_area.config(text=f"-- User Profile: {username} --\n\n[Custom Photo Area]\n[Personal Inventory Tracker]")

        # Navigation Bar
        nav_frame = tk.Frame(self.container, bg="#333333")
        nav_frame.pack(side="bottom", fill="x")

        tk.Button(nav_frame, text="Ads", bg="#444444", fg="#ffffff", command=lambda: load_view("ads")).pack(side="left", expand=True, fill="x")
        tk.Button(nav_frame, text="Stores", bg="#444444", fg="#ffffff", command=lambda: load_view("stores")).pack(side="left", expand=True, fill="x")
        tk.Button(nav_frame, text="Leader", bg="#444444", fg="#ffffff", command=lambda: load_view("leaderboard")).pack(side="left", expand=True, fill="x")
        tk.Button(nav_frame, text="Profile", bg="#444444", fg="#ffffff", command=lambda: load_view("profile")).pack(side="left", expand=True, fill="x")

        load_view("ads")

if __name__ == "__main__":
    app = DropnetTkApp()
    app.mainloop()
