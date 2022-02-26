from selenium import webdriver
import time
import json
import pyperclip

def main():
    option = webdriver.ChromeOptions()
    option.add_experimental_option(
        "excludeSwitches", ['enable-automation', 'enable-logging'])

    driver = webdriver.Chrome(
        # chromedriver.exe 位置
        executable_path="./chromedriver", options=option)

    driver.get('https://plogin.m.jd.com/login/login')
    input('登陆后按Enter键继续...')

    driver.get("https://home.m.jd.com/myJd/newhome.action")
    time.sleep(2)
    cookie = driver.get_cookies()
    jsonCookies = json.dumps(cookie)
    jsonCookies = json.loads(jsonCookies)
    # print(jsonCookies)
    for item in jsonCookies:
        if item["name"]=='pt_pin':
            pt_pin = item["value"]
        if item["name"]=='pt_key':
            pt_key = item["value"]
    jd_cookie = 'pt_key='+pt_key+';pt_pin='+pt_pin+';'
    
    print(jd_cookie)
    # pyperclip.copy(jd_cookie)
    # print('已复制到剪切板！')
    # input('按Enter键退出...')
    driver.close()


if __name__ == '__main__':
    main()
