import os
import requests


def TikTokToGIF(URL):
    dir_list = os.listdir('Videos')
    if len(dir_list) != 1:
        dir_list.sort()
        num = int(dir_list[-1][-5]) + 1
    else:
        num = 1
    file_name = f'Videos/TikTok{num}.gif'

    r = requests.get(URL, stream = True)

    with open(file_name, 'wb') as f:
        for chunk in r.iter_content(chunk_size = 1024*1024):
            if chunk:
                f.write(chunk)

        


URL = "https://v16-webapp.tiktok.com/3e7c4246b80912a0bdd5737c22ae303c/62e858a1/video/tos/maliva/tos-maliva-ve-0068c799-us/ccac3f27695a46e2bb736ebe6b086502/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=2890&bt=1445&btag=80000&cs=0&ds=3&ft=eXd.6H-oMyq8ZhTjKwe2NPtwyl7Gb&mime_type=video_mp4&qs=0&rc=ZGg5aDxoOzc1ZGVlaDk8NEBpMzV3Mzc6Znh5ZDMzZzczNEAvYDQxYzJeXi4xYzYzMDIyYSNibXFvcjQwb25gLS1kMS9zcw%3D%3D&l=202208011649520101880612282447399C"
TikTokToGIF(URL)