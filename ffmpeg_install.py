import os
import requests
import subprocess
from time import sleep

class Ffmpeg:
    def __init__(self):
        ...

    def download(self):

        print("downloading ffmpeg...")
        # url = 'https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z'
        url = 'https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip'

        # checking if ffmpeg has already been downloaded
        current_dir_list = os.listdir()
        for file in current_dir_list:
            if "ffmpeg-release" in file:
                print("Ffmpeg seems to have been downloaded. Skipping...")
                return 0

        # actual download
        response = requests.get(url)
        with open(f'{os.getcwd()}/ffmpeg-release-essentials.zip', 'wb') as file:
            file.write(response.content)
        current_dir = os.listdir()

        # just debug messages I guess.
        if "ffmpeg-release-essentials.zip" in current_dir:
            print("downloaded ffmpeg!")
        else:
            print("ffmpeg has not been downloaded properly")

    def decompress(self):
        current_dir_list = os.listdir()
        for file in current_dir_list:
            if "ffmpeg-7.0-essentials_build" in file:
                print("Ffmpeg seems to have been decompressed. Skipping...")
                return 0

        print("decompressing...")
        try:
            # subprocess.call(['7z', 'x', 'ffmpeg-release-full.7z'])
            subprocess.call(['7z', 'x', 'ffmpeg-release-essentials.zip'])
            print("decompressed succesfully!\nDeleting the original zip file...")
            os.remove("ffmpeg-release-essentials.zip")
            print("Deleted the original zip file.")

        except:
            print("error during decompression.")

    def adding_ffmpeg_to_env_variables(self):
        print("adding ffmpeg to environment variables...")
        # os.environ["PATH"] += f"{os.getcwd()}\\ffmpeg-7.0-full_build.7z"
        try:
            current_dir = os.listdir()
            for file in current_dir:
                if "ffmpeg-" in file:
                    ffmpeg = file
            if "ffmpeg" not in file:
                file = "ffmpeg-7.0-essentials_build"
            # os.environ["PATH"] += f"{os.getcwd()}\\ffmpeg-7.0-full_build\\bin"


            with open("Path_Original.txt", "w") as file1: #writing original Path file.
                file1.write(os.environ["Path"])
                file1.close()
                
            new_env = os.environ["Path"] + f";{os.getcwd()}/{file}/bin" #this string is going to be the new path variable.
            
            with open("Path_New.txt", "w") as file2: #This is the New path file
                file2.write(new_env)
                file2.close()


            exp = f'setx Path "{new_env}"' #This is the command used to set the Path variable.
            subprocess.Popen(exp, shell=True).wait()
            os.environ.update()
            
            print("ffmpeg should have been added to the environment variables. Restart your system or logout to see the changes. Want to restart now? ")
            user_in = input("[y/n]: ")
            if user_in == "y":
                print("restarting in 3 seconds.")
                sleep(3)
                print("restarting...")
                os.system("shutdown /r /t 0")
                print("restarted - this is a debug message")
            else:
                print("ok. Auto close in 10 seconds")
                sleep(10)
                exit()

        except:
            print("error while adding ffmpeg to path\n")
            return "error"



# basically check if the os is widows or linux. If it's linux it's literally a single command that needs sudo permissions.
def linux_download():
    ...


ffmpeg_var = Ffmpeg()
ffmpeg_var.download()
ffmpeg_var.decompress()
ffmpeg_var.adding_ffmpeg_to_env_variables()
