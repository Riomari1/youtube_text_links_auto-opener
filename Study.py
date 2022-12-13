import re
import IPython.display
import webbrowser
import pyautogui
from io import open

screenWidth, screenHeight = pyautogui.size()
screenWidth, screenHeight
(2560, 1600)
currentMouseX, currentMouseY = pyautogui.position()


pattern = r'https://www.youtube.com/watch\?v=[A-Za-z0-9_]+'


# Read the list of video URLs from the text file
with open('/Users/karamhejazin/Downloads/Chapter_7_T-distribution_and_Inference.txt') as f:
    text = f.readlines()

videos = []

# Loop over the lines in the text file
for line in text:
    # Search for the pattern in each line
    matches = re.findall(pattern, line)
    # Add any matching URLs to the list of videos
    videos.extend(matches)

for video in videos:
      #Open the URL in the web browser
        webbrowser.get('open -a /Applications/Opera\ GX.app %s').open_new_tab(video)
        pyautogui.moveTo(360, 360, duration=1.5)
        pyautogui.moveTo(360, 360, duration=3)
        pyautogui.click()
