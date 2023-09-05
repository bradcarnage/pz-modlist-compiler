# pz-modlist-compiler
Create my config entries automatically; Thank you!

I got sick of searching, editing, and formatting my mod IDs; So here is this script!

# Downloading & Installing

Click "Code", "Download ZIP". 

Extract zip file to a folder, and run `windows_launcher.bat`. (You may need to install python 3.11, too)

Run main.py with `python3.11` if running another software stack other than windows.

# Usage
Edit `urls.txt`, and put in your desired list of mod URLs, ordered by importance.

The script will download and parse the content for **Mod IDs**, **Workshop IDs**, and **Map Folders**.

open `output.txt` or view console output to get the desired formatting.

# Additional Notes
This script downloads content only once. If you need to fetch a new version of a mod, please clear `dlcache` folder to redownload.

# Screenshots
![screenshot](https://github.com/bradcarnage/pz-modlist-compiler/assets/8689194/24e69f62-7ba6-4cb4-b8d1-e0a46d4dbfa8)
