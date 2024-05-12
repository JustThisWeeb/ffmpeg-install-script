# ffmpeg-install-script
Install ffmpeg automatically.


# Requirements
- 7zip
- python3.x


  # usage and fair warning
  To use the script you simply need to double click on it. It will automatically download the newest release of ffmpeg, unzip it using 7zip (you do need to add it to path) so it can be used through the command line - open cmd and type 7z to test if it works), and then add it to your environment variables Path so that it can be used through the command line.
  
  -- The fair warning here is that this script has *NOT* been extensively tested. I tested it for 30 minutes and was able to figure out a strange but that might be more related to windows than anything and it's that I couldn't add new environment variables through the gui or the normal way. I was able to add them using the setx command which my script uses to add ffmpeg to Path in the first place. If you encounter the same error I am not really able to help you much other than tell you how to add new directories to Path.

  setx Path "(current path);(new directory)"

inside the "" you have to use your previous path. My script will write the original path and the new path to 2 separate files titled "Path_Original.txt" and "Path_New.txt" from where you can readily copy and paste whichever version of Path you want to keep. 
