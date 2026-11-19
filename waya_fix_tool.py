import tkinter as tk
from tkinter import messagebox
import subprocess
print("WAYA FIX TOOL - Safiyanu Mohammed")
root = tk.Tk()
root.title("WAYA FIX TOOL")
root.geometry("650x550")
tk.Label(root, text="WAYA FIX TOOL", font=("Arial", 22, "bold")).pack(pady=10)
tk.Label(root, text="Owner: Safiyanu Mohammed | Opay: 8113353315").pack()
tk.Button(root, text="0. DETECT PHONE - FREE", width=35, height=2).pack(pady=5)
tk.Button(root, text="1. READ INFO - FREE", width=35, height=2).pack(pady=5)
tk.Button(root, text="2. FACTORY RESET - 1 Credit", width=35, height=2).pack(pady=5)
tk.Button(root, text="5. CHECK IMEI / SERIAL - FREE", width=35, height=2).pack(pady=5)
tk.Button(root, text="6. CHECK FRP STATUS - FREE", width=35, height=2).pack(pady=5)
root.mainloop()
