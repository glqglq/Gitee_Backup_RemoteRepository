# -*- coding: utf-8 -*-
import re
import requests

from selenium import webdriver

git_url_re = r'i> <a href=\\"/iOceanPlus/(.*?)"'

class Html(object):
    def __init__(self,url):
        self.__url  = url
        self.__content = None
        self.__git_url = None

    def get_page_content(self,now_cookie):
        self.__content = requests.get(self.__url,cookies = now_cookie).text

    """
    根据xpath抽取git_url    
    """
    def get_git_url(self):
        self.__git_url = re.findall(git_url_re,self.__content)

    def trans_git_url(self):
        for i in range(len(self.__git_url)):
            self.__git_url[i] = 'https://gitee.com/iOceanPlus/' + self.__git_url[i][:-1] + '.git'
        for url in self.__git_url:
            print url
        return self.__git_url

    def has_data(self):
        if "无数据" in self.__content.encode('utf-8'):
            return True
        return False

    def get_cookie(self):
        url_login = 'https://gitee.com/login'
        driver = webdriver.PhantomJS()
        driver.get(url_login)
        driver.find_element_by_xpath('//*[@id="user_login"]').send_keys('luckygong')  # 改成你的微博账号
        driver.find_element_by_xpath('//*[@id="user_password"]').send_keys('7758521')  # 改成你的微博密码

        driver.find_element_by_xpath('//*[@id="new_user"]/div[2]/div[4]/input').click()  # 点击登录

        # 获得 cookie信息
        cookie_list = driver.get_cookies()
        print "当前cookie是：",cookie_list
        # return cookie_list

        cookie_dict = {}
        for cookie in cookie_list:
            if cookie.has_key('name') and cookie.has_key('value'):
                cookie_dict[cookie['name']] = cookie['value']

        return cookie_dict


if __name__ == '__main__':

    i = 1
    html = Html(r'https://gitee.com/organizations/iOceanPlus/projects?page=' + str(i))
    now_cookie = html.get_cookie()
    while (True):
        html = Html(r'https://gitee.com/organizations/iOceanPlus/projects?page=' + str(i))
        # print 'page ' + str(i)
        html.get_page_content(now_cookie)
        if html.has_data():
            break
        html.get_git_url()
        html.trans_git_url()
        i += 1
