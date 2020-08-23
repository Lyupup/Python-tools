import requests
import hashlib


# For hack the box Emdee five for life
url = "http://docker.hackthebox.eu:31840"
header = {"Host": "docker.hackthebox.eu:31840",
          "User-Agent": "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
          "Accept-Language": "zh-CN,en-US;q=0.7,en;q=0.3", "Accept-Encoding": "gzip, deflate",
          "Cookie":"ajs_anonymous_id=%223ce3c44a-cdba-40e1-a55c-a71b876bb762%22; _ga=GA1.2.1053154107.1597369246; _gid=GA1.2.525328232.1597369246; PHPSESSID=37s0dl6hnn1hbahhqu6isshvp0",
          "Upgrade-Insecure-Requests": "1",
          "Connection": "close", "Cache-Control": "max-age=0"}
try:
    res = requests.get(url=url,headers=header)
    b = res.text.split("<h3 align='center'>")[1].split("</h3><center>")[0]
    print(b)
    c = hashlib.md5()
    c.update(b.encode())
    print(c.hexdigest())
    data = "hash=" + c.hexdigest()
    header = {"Host": "docker.hackthebox.eu:31840",
              "User-Agent": "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
              "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
              "Accept-Language": "zh-CN,en-US;q=0.7,en;q=0.3",
              "Referer": "http://docker.hackthebox.eu:31840/",
              "Content-Type": "application/x-www-form-urlencoded",
              "Accept-Encoding": "gzip, deflate",
              "Content-Length": str(len(data)),
              "Connection": "close",
              "Cookie": "ajs_anonymous_id=%223ce3c44a-cdba-40e1-a55c-a71b876bb762%22; _ga=GA1.2.1053154107.1597369246; _gid=GA1.2.525328232.1597369246; PHPSESSID=37s0dl6hnn1hbahhqu6isshvp0",
              "Upgrade-Insecure-Requests": "1",
              "Cache-Control": "max-age=0"}
    res2 = requests.post(url=url,headers=header,data=data)
    print(res2.text)
except Exception as e:
    print(e)


