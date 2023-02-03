import os
import time
import requests
import re


def require_audio():
    headers = {
        'user-agent': 'XXXXXXX'
    }
    filepath = r"C:\project\my_env_two\pcr"
    path_index_people = "https://wiki.biligame.com/pcr/%E8%A7%92%E8%89%B2%E5%9B%BE%E9%89%B4"
    path_index = "https://wiki.biligame.com"
    response = requests.get(path_index_people, headers=headers)
    html = response.text
    urls = re.findall('<a href="(.*?)" title="(.*?)"', html)
    urls = list(set(urls))
    print(urls)
    length = (len(urls))
    print((urls[0]))
    print((urls[0][0]))
    for url in urls:
        time.sleep(1)
        if url[1] == '角色图鉴' or url[1] == '帮助:常见问题' or url[1] == '本页面受到保护。&#10;您可以查看其源代码[e]' \
                or url[1] == '您的提醒' or url[1] == '本页面过去的版本[h]' or url[1] == '首页':
            print("不符合要求：" + url[1])
        else:
            print("正在下载:" + url[1])
            print("地址:" + path_index + url[0])
            html_download = requests.get(path_index + url[0], headers=headers)
            urls_download = re.findall('<audio src="(.*?)"', html_download.text)
            len_urls_download = len(urls_download)
            num = 1
            for url_download in urls_download:
                path_name = filepath + "\\" + url[1]
                if not os.path.isdir(path_name):
                    # 创建文件夹
                    os.mkdir(path_name)
                time.sleep(0.5)
                response_download = requests.get(url_download, headers=headers)
                file_name = url_download.split("/")[-1]
                with open(path_name + "\\" + file_name, 'wb') as f:
                    f.write(response_download.content)
                print("已完成:" + str(num) + "/" + str(len_urls_download))
                num = num + 1


if __name__ == '__main__':
    require_audio()
