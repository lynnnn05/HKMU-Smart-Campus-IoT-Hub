"""
Module: gui_app.py
Description: Modern Dark-Mode GUI for the HKMU Smart Campus IoT Hub.
             This module handles the presentation layer, separating user 
             interactions from the core business logic (Modular Programming).
             
             Key features:
             - Real-time energy and cost analytics (Polymorphism).
             - Asynchronous Command Queue visualization (Data Structures).
             - Event-driven device management.
"""
import tkinter as tk
from tkinter import messagebox, simpledialog
from devices import SmartAC, LabOscilloscope
from hub_controller import CampusIoTHub

# --- UI Color Palette (Industry Standard Dark Theme) ---
BG_MAIN = "#121212"       # Deep black background
BG_CARD = "#1E1E1E"       # Elevated surface color for cards
FG_TEXT = "#FFFFFF"       # Primary text
FG_SUB = "#AAAAAA"        # De-emphasized sub-text
ACCENT_BLUE = "#007ACC"   # Primary action color (Terminal Blue)
COLOR_ON = "#2EA043"      # Status: Operational (Green)
COLOR_OFF = "#F85149"     # Status: Power Off (Red)
QUEUE_BG = "#252526"      # Distinct background for the Task Queue

class CampusDashboardGUI:
    """
    Main Application Class for the Smart Campus IoT Dashboard.
    Manages the lifecycle of the Tkinter window and UI components.
    """
    
    def __init__(self, root):
        self.root = root
        self.root.title("HKMU Smart Campus - Edge IoT Dashboard")
        # Extended width to accommodate the Command Queue panel
        self.root.geometry("850x570")
        self.root.configure(bg=BG_MAIN)
        self.root.resizable(False, False)

        # Aggregation: The GUI 'has a' Hub Controller
        self.hub = CampusIoTHub("HKMU EECS Zone")
        self._init_devices()

        # Build UI Components
        self._build_header()
        self._build_main_layout()
        self.update_ui() # Initial UI refresh to sync data

    def _init_devices(self):
        """Pre-loads the system with sample HKMU IoT edge devices."""
        ac1 = SmartAC("AC-A0411", "Block A 0411")
        ac2 = SmartAC("AC-E0712", "Block E Lab", base_power=2500)
        osc1 = LabOscilloscope("OSC-01", "Block E Lab")
        
        self.hub.register_device(ac1)
        self.hub.register_device(ac2)
        self.hub.register_device(osc1)

    def _build_header(self):
        """Constructs the top analytic panel showing real-time power and cost."""
        self.header_frame = tk.Frame(self.root, bg=BG_CARD, pady=10)
        self.header_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(self.header_frame, text="⚡ IoT Edge Energy Controller", 
                 font=("Segoe UI", 16, "bold"), bg=BG_CARD, fg=ACCENT_BLUE).pack()
        
        # Real-time Power Label (Calculated via Polymorphism)
        self.lbl_power = tk.Label(self.header_frame, text="Real-time Draw: 0.00 W", 
                                   font=("Segoe UI", 13, "bold"), bg=BG_CARD, fg=FG_TEXT)
        self.lbl_power.pack()
        
        # Hourly Cost Label (Calculated via Polymorphism)
        self.lbl_cost = tk.Label(self.header_frame, text="Estimated Cost: HKD $0.00 / hr", 
                                  font=("Segoe UI", 11), bg=BG_CARD, fg=FG_SUB)
        self.lbl_cost.pack()

    def _build_main_layout(self):
        """Split-pane layout: Device Control (Left) vs. Command Queue (Right)."""
        main_pane = tk.Frame(self.root, bg=BG_MAIN)
        main_pane.pack(fill=tk.BOTH, expand=True, padx=15)

        # --- Left Pane: Device Management ---
        self.left_frame = tk.Frame(main_pane, bg=BG_MAIN)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        self.device_widgets = {}
        for device in self.hub.get_all_devices():
            card = tk.Frame(self.left_frame, bg=BG_CARD, pady=15, padx=15)
            card.pack(fill=tk.X, pady=8)
            
            name_lbl = tk.Label(card, text=f"{device.get_id()}", 
                                font=("Segoe UI", 12, "bold"), bg=BG_CARD, fg=FG_TEXT)
            name_lbl.pack(side=tk.LEFT)
            
            status_lbl = tk.Label(card, text="OFF", font=("Consolas", 12, "bold"), 
                                  bg=BG_CARD, fg=COLOR_OFF, width=12)
            status_lbl.pack(side=tk.LEFT, padx=10)
            
            # Interactive buttons that append tasks to the FIFO Queue
            btn_toggle = tk.Button(card, text="+ Queue Pwr", font=("Segoe UI", 9, "bold"), 
                                   bg="#444444", fg=FG_TEXT, relief="flat", cursor="hand2",
                                   command=lambda d=device: self.queue_power_toggle(d))
            btn_toggle.pack(side=tk.RIGHT, padx=5)

            btn_setting = tk.Button(card, text="+ Queue Set", font=("Segoe UI", 9), 
                                    bg="#333333", fg=FG_TEXT, relief="flat", cursor="hand2",
                                    command=lambda d=device: self.queue_setting(d))
            btn_setting.pack(side=tk.RIGHT)

            self.device_widgets[device.get_id()] = {"status_lbl": status_lbl, "btn_toggle": btn_toggle}

        # Immediate Action: Eco-Mode (Aggregation-level control)
        btn_eco = tk.Button(self.left_frame, text="🍃 Instant Eco-Mode", 
                            font=("Segoe UI", 12, "bold"), bg=COLOR_ON, fg="#000000", 
                            relief="flat", cursor="hand2", pady=5, command=self.trigger_eco)
        btn_eco.pack(fill=tk.X, pady=15)

        # --- Right Pane: Task Queue Visualization ---
        self.right_frame = tk.Frame(main_pane, bg=QUEUE_BG, padx=10, pady=10)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.Y)

        tk.Label(self.right_frame, text="Task Queue (FIFO Buffer)", 
                 font=("Segoe UI", 12, "bold"), bg=QUEUE_BG, fg=ACCENT_BLUE).pack(pady=(0, 10))
        
        self.queue_listbox = tk.Listbox(self.right_frame, bg="#000000", fg="#00FF00", 
                                        font=("Consolas", 10), width=35, height=15, 
                                        borderwidth=0, highlightthickness=0)
        self.queue_listbox.pack(fill=tk.BOTH, expand=True)

        btn_execute = tk.Button(self.right_frame, text="▶ Execute All (Batch)", 
                                font=("Segoe UI", 11, "bold"), bg="#005A9E", fg=FG_TEXT, 
                                relief="flat", cursor="hand2", pady=8, command=self.execute_queue)
        btn_execute.pack(fill=tk.X, pady=(15, 0))

    def queue_power_toggle(self, device):
        """Encapsulates a power-toggle task and adds it to the Hub's Command Queue."""
        action = lambda: device.turn_off() if device.get_status() else device.turn_on()
        self.hub.command_queue.enqueue(f"Toggle Power: {device.get_id()}", action)
        self.refresh_queue_ui()

    def queue_setting(self, device):
        """Encapsulates a setting-change task into the Queue (Polymorphic UI behavior)."""
        if isinstance(device, SmartAC):
            temp = simpledialog.askinteger("AC Control", f"Target temp for {device.get_id()} (18-30):", 
                                            minvalue=18, maxvalue=30)
            if temp:
                self.hub.command_queue.enqueue(f"Set Temp: {device.get_id()} to {temp}°C", 
                                               lambda: device.set_temperature(temp))
        elif isinstance(device, LabOscilloscope):
            ans = messagebox.askyesno("Oscilloscope Mode", "Switch to Active Mode?")
            if ans:
                self.hub.command_queue.enqueue(f"Set Mode: {device.get_id()} to Active", 
                                               lambda: device.set_active_mode())
            else:
                self.hub.command_queue.enqueue(f"Set Mode: {device.get_id()} to Standby", 
                                               lambda: device.set_standby_mode())
        self.refresh_queue_ui()

    def refresh_queue_ui(self):
        """Synchronizes the visual Listbox with the current state of the FIFO Queue."""
        self.queue_listbox.delete(0, tk.END)
        for i, desc in enumerate(self.hub.command_queue.get_descriptions()):
            self.queue_listbox.insert(tk.END, f"[{i+1}] {desc}")

    def execute_queue(self):
        """Triggers sequential processing of all queued commands."""
        if self.hub.command_queue.is_empty():
            messagebox.showinfo("Queue Empty", "No tasks currently in the buffer.")
            return
            
        executed = self.hub.execute_all_queued_commands()
        self.refresh_queue_ui()
        self.update_ui()
        messagebox.showinfo("Batch Execution", f"Successfully executed {executed} tasks.")

    def trigger_eco(self):
        """Instantly executes the Hub's Eco-Mode logic."""
        msg = self.hub.trigger_eco_mode()
        messagebox.showinfo("Eco Mode", msg)
        self.refresh_queue_ui()
        self.update_ui()

    def update_ui(self):
        """Recalculates system-wide analytics and refreshes dynamic UI elements."""
        # Update Analytics (Leveraging Polymorphism)
        total_w = self.hub.calculate_total_zone_power()
        total_cost = self.hub.calculate_total_hourly_cost()
        
        self.lbl_power.config(text=f"Real-time Draw: {total_w:.1f} W", 
                              fg=COLOR_OFF if total_w > 4000 else FG_TEXT)
        self.lbl_cost.config(text=f"Estimated Cost: HKD ${total_cost:.2f} / hr")

        # Update Device Status Labels
        for device in self.hub.get_all_devices():
            widgets = self.device_widgets[device.get_id()]
            if device.get_status():
                status_text = f"ON ({device._target_temp}°C)" if isinstance(device, SmartAC) else f"ON ({device._mode})"
                widgets["status_lbl"].config(text=status_text, fg=COLOR_ON)
                widgets["btn_toggle"].config(bg=ACCENT_BLUE)
            else:
                widgets["status_lbl"].config(text="OFF", fg=COLOR_OFF)
                widgets["btn_toggle"].config(bg="#444444")
