# -*- coding: utf-8 -*-

import os,datetime,requests,json
from settings import username,password,repo_path,repo_base_url,api_url
from get_git_url import Html

def clone_from_git(repo_url):
    os.system(r'git clone ' + r'https://' + username + r':' + password + r'@' + repo_url[8:] + ' ' + repo_path + r'//' + datetime.datetime.now().strftime('%Y-%m-%d') + r'//' + repo_url.split('/')[-1][:-4])


def clone_all_from_git(repo_urls):
    for repo_url in repo_urls:
        clone_from_git(repo_url)

if __name__ == '__main__':
    all_git_urls = []

    # 1.通过爬虫爬取git地址
    try:
        i = 1
        html = Html(repo_base_url + str(i))
        now_cookie = html.get_cookie()
        while (True):
            html = Html(repo_base_url + str(i))
            html.get_page_content(now_cookie)
            if html.has_data():
                break
            html.get_git_url()
            all_git_urls.extend(html.trans_git_url())
            i += 1
    except Exception:
        pass

    # 2.通过API获得git地址
    res = os.popen('curl -X POST --data-urlencode "grant_type=password" --data-urlencode "username=" --data-urlencode "password=" --data-urlencode "client_id=" --data-urlencode "client_secret=" --data-urlencode "scope=projects user_info issues notes" https://gitee.com/oauth/token').readline()
    now_token = json.loads(res)['access_token']
    if not all_git_urls:
        project_information_dict = None
        try:
            project_information_dict = json.loads(requests.get('https://gitee.com/api/v5/orgs/iOceanPlus/repos?access_token=' + now_token + '&type=all&page=1&per_page=999999999999').text)
        except Exception,e:
            print e

        if project_information_dict:
            for project_information in project_information_dict:
                if project_information.has_key('full_name'):
                    all_git_urls.append(r'https://gitee.com/' + project_information.get('full_name','') + '.git')
    print all_git_urls

    # 3.拉取备份
    if all_git_urls:
        clone_all_from_git(all_git_urls)
    else:
        print '出错，无法拉取备份'
