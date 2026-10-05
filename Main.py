import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from pathlib import Path
from PIL import Image
from TkinterGUISaturnTheme import apply_theme



def select_folder():
    folder = filedialog.askdirectory(title="Select PNG folder")

    if folder:
        folder_var.set(folder)


def create_gif():
    folder = folder_var.get()

    if not folder:
        messagebox.showwarning(
            "No folder",
            "Please select a folder first."
        )
        return

    folder = Path(folder)

    if not folder.exists():
        messagebox.showerror(
            "Error",
            "The selected folder does not exist."
        )
        return

    # Get PNG files
    files = sorted(folder.glob("*.png"))

    if not files:
        messagebox.showwarning(
            "No PNG files",
            "No PNG files were found in the selected folder."
        )
        return

    try:
        fps = float(fps_var.get())

        if fps <= 0:
            raise ValueError

    except ValueError:
        messagebox.showerror(
            "Invalid FPS",
            "Please enter a valid FPS value."
        )
        return

    duration = int(1000 / fps)

    try:
        # Load frames
        frames = []

        for file in files:
            img = Image.open(file).convert("RGBA")
            frames.append(img)

        # Output file
        output_file = folder / "animation.gif"

        # Save GIF
        frames[0].save(
            output_file,
            save_all=True,
            append_images=frames[1:],
            duration=duration,
            loop=0
        )

        messagebox.showinfo(
            "Success",
            f"GIF created successfully!\n\n"
            f"Frames: {len(frames)}\n"
            f"FPS: {fps}\n\n"
            f"Saved to:\n{output_file}"
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            f"Failed to create GIF:\n\n{e}"
        )

#GUI lives here

root = tk.Tk()
apply_theme()
root.title("GIFford")
root.geometry("600x300")

folder_var = tk.StringVar()
fps_var = tk.StringVar(value="10")

# ttk widgets to match modern Tk styling
ttk.Label(root, text="PNG Folder:").pack(anchor="w", padx=20, pady=(20, 5))

folder_frame = ttk.Frame(root)
folder_frame.pack(fill="x", padx=20)
ttk.Entry(folder_frame, textvariable=folder_var).pack(side="left", fill="x", expand=True)
ttk.Button(folder_frame, text="Browse...", command=select_folder).pack(side="left", padx=(10, 0))

fps_frame = ttk.Frame(root)
fps_frame.pack(anchor="w", padx=20, pady=20)

ttk.Label(fps_frame, text="FPS:").pack(side="left")
ttk.Entry(fps_frame, textvariable=fps_var, width=8).pack(side="left", padx=10)
ttk.Label(fps_frame, text="(e.g. 10 = 10 frames per second)").pack(side="left")
ttk.Button(root, text="CREATE GIF", command=create_gif).pack(pady=5)

root.mainloop()