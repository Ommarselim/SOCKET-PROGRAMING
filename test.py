window_height = window_main.winfo_screenheight()
window_width = window_main.winfo_screenwidth() // 2

x = window_main.winfo_screenwidth() // 2
y = 0

window_main.geometry(f"{window_width}x{window_height}+{x}+{y}")