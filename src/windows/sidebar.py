import tkinter as tk
from tkinter import ttk

class Sidebar(tk.Frame):
    def __init__(self, master, controller, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.controller = controller
        self.config(bg="#20232a", width=180)
        self.grid_propagate(False)

        title = tk.Label(
            self,
            text="PyMacroRecord",
            bg="#20232a",
            fg="#ffffff",
            font=("Segoe UI", 12, "bold")
        )
        title.grid(row=0, column=0, padx=12, pady=(12, 8), sticky="w")

        self._make_button("● Record", self.controller.start_record, row=1)
        self._make_button("■ Stop", self.controller.stop_record, row=2)
        self._make_button("▶ Play", self.controller.start_playback, row=3)

        ttk.Separator(self, orient="horizontal").grid(
            row=4, column=0, sticky="ew", padx=10, pady=8
        )

        self._make_button("Open macro…", self.controller.open_macro, row=5)
        self._make_button("Save macro…", self.controller.save_macro, row=6)

        ttk.Separator(self, orient="horizontal").grid(
            row=7, column=0, sticky="ew", padx=10, pady=8
        )

        self._make_button("Repetitions / Loop", self.controller.open_repetitions, row=8)
        self._make_button("Speed & Interval", self.controller.open_speed_interval, row=9)
        self._make_button("Schedule", self.controller.open_schedule, row=10)
        self._make_button("After playback", self.controller.open_after_playback, row=11)

        ttk.Separator(self, orient="horizontal").grid(
            row=12, column=0, sticky="ew", padx=10, pady=8
        )

        self._make_button("Settings / Hotkeys", self.controller.open_settings, row=13)

        self.rowconfigure(list(range(14)), weight=0)
        self.rowconfigure(99, weight=1)

    def _make_button(self, text, command, row):
        btn = tk.Button(
            self,
            text=text,
            command=command,
            anchor="w",
            relief="flat",
            bg="#20232a",
            fg="#ffffff",
            activebackground="#2c313c",
            activeforeground="#ffffff",
            padx=12,
            pady=4,
            borderwidth=0,
            highlightthickness=0,
        )
        btn.grid(row=row, column=0, sticky="ew", padx=6, pady=2)
