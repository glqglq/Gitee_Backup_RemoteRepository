# Product_Python_BackupRemoteRepository
## 0.环境要求
安装git、python、crontab
## 1.项目描述
每隔一段时间，将位于码云上iOceanPlus的项目代码给克隆到本地备份下来，主要是：
- 项目git地址抓取
- 根据git地址克隆到本地
## 2.使用方法
### 2.0安装依赖
```
sudo yum install fontconfig
pip install requests,selenium
# 下载phantomjs
wget https://bbuseruploads.s3.amazonaws.com/fd96ed93-2b32-46a7-9d2b-ecbc0988516a/downloads/396e7977-71fd-4592-8723-495ca4cfa7cc/phantomjs-2.1.1-linux-x86_64.tar.bz2?Signature=O7VG1bGL1UymUQ5iZgSDYP97nuE%3D&Expires=1506742857&AWSAccessKeyId=AKIAIQWXW6WLXMB5QZAQ&versionId=null&response-content-disposition=attachment%3B%20filename%3D%22phantomjs-2.1.1-linux-x86_64.tar.bz2%22
```
将phantomjs解压后添加到path路径中去
### 2.1配置程序
修改settings.py中的配置项
### 2.2设置计划任务
- 在centos命令行里输入：
```
service crond start #开启cron定时执行工具
chkconfig crond on   #开机自动启动
crontab -e  #编辑/var/spool/cron下对应用户的cron文件
```
- cron文件格式如下：

分     小时    日     月      星期     命令

对于本程序，要求每个月执行一次，则可以设置为：

15     11       29           *     * python  ~/Product_Python_BackupRemoteRepository/git_pull.py

意思是：每个月的29号11:15分执行一次python  ~/Product_Python_BackupRemoteRepository/git_pull.py
## 3.效果展示
![效果展示](http://ot0qvixbu.bkt.clouddn.com/QQ%E6%88%AA%E5%9B%BE20170930130337.png "效果展示")
