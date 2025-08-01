## Download libs 
import subprocess

print("This is a keylogger btw :p")

def check_playsound():
    download = subprocess.run('pip freeze | findstr playsound', shell=True, stdout=subprocess.PIPE)
    download = download.stdout.decode("utf-8")
    if download == "":
        subprocess.run('pip install playsound==1.2.2')
    

def check_pywin():
    download = subprocess.run('pip freeze | findstr pywin32', shell=True, stdout=subprocess.PIPE)
    download = download.stdout.decode("utf-8")
    if download == "":
        subprocess.run('pip install pywin32')

check_playsound()
check_pywin()
## The epicness begins
subprocess.run(["python", "boom.py"])
