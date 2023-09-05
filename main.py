import requests, re, os, html
regex_modid = re.compile(r'>Mod ID:\s+([^<]*)')
regex_workshopid = re.compile(r'>Workshop ID:\s+([^<]*)')
regex_mapfolder = re.compile(r'>Map Folder:\s+([^<]*)')
modid_list = []
workshopid_list = []
mapfolder_list = []

def fetch_url_cached(url):
    os.makedirs('dlcache', exist_ok=True)
    filename = re.sub(r'\W+', '-', url)
    filepath = f'dlcache{os.path.sep}{filename}'
    if os.path.exists(filepath): # use data from cached file, if it exists
        print(f'Use cached {filename}')
        with open(filepath, "r", encoding='utf-8-sig') as file:
            return(file.read())
    else: # else, download cache file and use response from URL.
        print(f'Downloading {url}')
        with open(filepath, "w", encoding='utf-8-sig') as file:
            resp = requests.get(url).text
            file.write(resp)
            return(resp)

with open('urls.txt', 'r', encoding='utf-8-sig') as file:
    for url in file:
        url = url.strip()
        # print(f'URL: {url}')
        res = fetch_url_cached(url)
        for x in regex_modid.findall(res):
            x = html.unescape(x).strip()
            if not x in modid_list:
                modid_list.append(x)
            # modid_str = modid_str+x+';'
        for x in regex_workshopid.findall(res):
            x = html.unescape(x).strip()
            if not x in workshopid_list:
                workshopid_list.append(x)
            # workshopid_str = workshopid_str+x+';'
        for x in regex_mapfolder.findall(res):
            x = html.unescape(x).strip()
            if not x in mapfolder_list:
                mapfolder_list.append(x)
            # mapfolder_str = mapfolder_str+x+';'
with open("output.txt", "w") as file:
    output_str = "Mod IDS: \n"
    for x in modid_list:
        output_str = output_str+x+';'
    output_str = output_str+"\nWorkshop IDS: \n"
    for x in workshopid_list:
        output_str = output_str+x+';'
    output_str = output_str+"\nMap Folders: \n"
    for x in mapfolder_list:
        output_str = output_str+x+';'
    output_str = output_str+"\n"
    print(f"\nPARSED OUTPUT COMPLETE:\n\n{output_str}")
    file.write(output_str)
