import socket
import tkinter as tk
from tkinter import messagebox

def scan_ports(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def start_scan():
    host = host_entry.get()
    start_port = int(start_port_entry.get())
    end_port = int(end_port_entry.get())
    open_ports = scan_ports(host, start_port, end_port)
    if open_ports:
        messagebox.showinfo("Scan Results", f"Port yang Terbuka: {open_ports}")
    else:
        messagebox.showinfo("Scan Results", "Tidak ada Port yang Terbuka.")

root = tk.Tk()
root.title("Final Project Scanning Ports")

host_label = tk.Label(root, text="Masukkan Host\t\t:")
host_label.grid(row=0, column=0, padx=15, pady=5)

host_entry = tk.Entry(root)
host_entry.grid(row=0, column=1, padx=15, pady=5)

start_port_label = tk.Label(root, text="Masukkan Port Awal\t:")
start_port_label.grid(row=1, column=0, padx=15, pady=5)

start_port_entry = tk.Entry(root)
start_port_entry.grid(row=1, column=1, padx=15, pady=5)

end_port_label = tk.Label(root, text="Masukkan Port Akhir\t:")
end_port_label.grid(row=2, column=0, padx=15, pady=5)

end_port_entry = tk.Entry(root)
end_port_entry.grid(row=2, column=1, padx=15, pady=5)

scan_button = tk.Button(root, text="Mulai Scan", command=start_scan)
scan_button.grid(row=3, column=0, columnspan=2, padx=15, pady=5)
root.mainloop()

