import tkinter as tk
import socket
import socks
import requests
from tkinter import messagebox
import threading

# 代理服务器的 IP（美国服务器的 IP）
PROXY_HOST = "your-us-vps-ip"
PROXY_PORT = 8388
PROXY_PASSWORD = "yourpassword"

# 设定 SOCKS5 代理
socks.set_default_proxy(socks.SOCKS5, PROXY_HOST, PROXY_PORT)
socket.socket = socks.socksocket

class AmericaBlueLineApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("America BlueLine")
        self.geometry("400x250")
        self.configure(bg="#1e1e1e")
        self.resizable(False, False)
        
        # 背景画布
        self.canvas = tk.Canvas(self, width=400, height=250, bg="#1e1e1e", bd=0, highlightthickness=0)
        self.canvas.pack()

        # 标签
        self.label = self.canvas.create_text(200, 50, text="Click the button to connect to the U.S. server", 
                                             fill="white", font=("Arial", 14, "bold"))
        
        # 按钮
        self.button = self.canvas.create_rectangle(100, 120, 300, 160, fill="#6200ea", outline="", width=0)
        self.canvas.create_text(200, 140, text="Connect to America", fill="white", font=("Arial", 12, "bold"))
        self.canvas.tag_bind(self.button, "<Button-1>", self.start_connection)

        # 进度条
        self.progress_bar = self.canvas.create_rectangle(50, 180, 350, 200, fill="#333333", outline="")
        self.progress_fill = self.canvas.create_rectangle(50, 180, 50, 200, fill="#03dac5", outline="")
        
    def start_connection(self, event):
        # 开始连接并更新按钮状态
        self.canvas.itemconfig(self.label, text="Connecting...")
        self.canvas.itemconfig(self.button, fill="#3700b3")
        
        # 在独立线程中运行连接过程
        threading.Thread(target=self.connect_to_us).start()

    def connect_to_us(self):
        try:
            response = requests.get("http://ipinfo.io/json")  # 获取 IP 以验证连接
            ip = response.json().get('ip')
            self.canvas.itemconfig(self.label, text=f"Connected! Your IP: {ip}")
            self.canvas.itemconfig(self.button, fill="#03dac5")
        except Exception as e:
            self.canvas.itemconfig(self.label, text=f"Failed to connect: {e}")
            self.canvas.itemconfig(self.button, fill="#b00020")

        # 模拟进度条动画
        for i in range(1, 11):
            self.canvas.coords(self.progress_fill, 50, 180, 50 + 30 * i, 200)
            self.update_idletasks()
            self.after(100)

# 运行应用
if __name__ == "__main__":
    app = AmericaBlueLineApp()
    app.mainloop()
