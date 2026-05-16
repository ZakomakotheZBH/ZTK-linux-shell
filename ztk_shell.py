import os

import subprocess

import time

history = []

# -----------------------------

# REAL WORKING APPS (32)

# -----------------------------

def file_manager():

    return subprocess.getoutput("ls -la")

def text_editor():

    return "Use system editor: nano file.txt (run manually)"

def system_info():

    return subprocess.getoutput("uname -a && lscpu | head")

def process_viewer():

    return subprocess.getoutput("ps aux | head -n 20")

def network_tools():

    return subprocess.getoutput("ip a 2>/dev/null || ifconfig")

def calc():

    expr = input("Enter expression (e.g. 2+2*5): ")

    try:

        return str(eval(expr))

    except:

        return "Invalid expression"

def task_manager():

    return subprocess.getoutput("top -b -n 1 | head -n 15")

def disk_usage():

    return subprocess.getoutput("df -h")

def log_viewer():

    return subprocess.getoutput("dmesg | tail -n 20")

def notes():

    note = input("Write note: ")

    with open("ztk_notes.txt", "a") as f:

        f.write(note + "\n")

    return "Saved to ztk_notes.txt"

def calendar():

    return subprocess.getoutput("cal")

def weather():

    return subprocess.getoutput("curl -s wttr.in || echo 'No internet'")

def browser():

    return "Open browser manually: xdg-open https://google.com"

def store():

    return "ZTK Store: (simulated package list)\nvim\npython\nnode\ngcc"

def settings():

    return "ZTK Settings: user=root | mode=dev | shell=ztk"

def terminal_plus():

    return os.system("bash")

def compiler():

    return subprocess.getoutput("gcc --version")

def debugger():

    return "Use gdb manually: gdb ./program"

def monitor():

    return subprocess.getoutput("uptime")

def installer():

    pkg = input("Package name: ")

    return subprocess.getoutput(f"sudo apt install -y {pkg}")

def launcher():

    return "Apps available via 'apps' command"

def chat():

    return "Chat system: not connected (offline mode)"

def code_editor():

    return "Use: nano file.py"

def backup():

    return subprocess.getoutput("tar -czf backup.tar.gz . 2>/dev/null && echo Backup done")

def search():

    term = input("Search file: ")

    return subprocess.getoutput(f"find . -name '*{term}*'")

def permissions():

    return subprocess.getoutput("ls -l")

def music():

    return "Music: use 'mpv file.mp3' if installed"

def video():

    return "Video: use 'mpv file.mp4' if installed"

def image():

    return "Image: use 'xdg-open image.png'"

def email():

    return "Email: use mutt or webmail"

def shell():

    return os.system("bash")

def launcher_exec():

    return "Launcher ready (apps list available)"

# MAP APPS

APPS = {

    "file_manager": file_manager,

    "text_editor": text_editor,

    "system_info": system_info,

    "process_viewer": process_viewer,

    "network_tools": network_tools,

    "calc": calc,

    "task_manager": task_manager,

    "disk_usage": disk_usage,

    "log_viewer": log_viewer,

    "notes": notes,

    "calendar": calendar,

    "weather": weather,

    "browser": browser,

    "store": store,

    "settings": settings,

    "terminal_plus": terminal_plus,

    "compiler": compiler,

    "debugger": debugger,

    "monitor": monitor,

    "installer": installer,

    "launcher": launcher_exec,

    "chat": chat,

    "code_editor": code_editor,

    "backup": backup,

    "search": search,

    "permissions": permissions,

    "music": music,

    "video": video,

    "image": image,

    "email": email,

    "shell": shell

}

# -----------------------------

# CORE SHELL

# -----------------------------

def run_command(cmd):

    try:

        return subprocess.getoutput(cmd)

    except Exception as e:

        return str(e)

def shell():

    print("ZTK SHELL - ALL APPS ACTIVE")

    while True:

        cmd = input("ztk> ").strip()

        history.append(cmd)

        if cmd == "exit":

            break

        if cmd == "history":

            for i, h in enumerate(history):

                print(i+1, h)

            continue

        if cmd == "apps":

            print("\n".join(APPS.keys()))

            continue

        if cmd.startswith("run "):

            app = cmd.split(" ", 1)[1]

            if app in APPS:

                result = APPS[app]()

                print(result)

            else:

                print("App not found")

            continue

        print(run_command(cmd))

if __name__ == "__main__":

    shell();
