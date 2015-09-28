#-*- coding:utf-8 -*-
#-------------------------------------------------
# 功能:实现东北大学ip网关的登陆，免去了打开浏览器登陆的麻烦
# 作者：王一凡
# 完成时间：2015年6月22日
# 版本：0.0.3
# 注意：采用了base64加密。如果有人得到你的存储文件还是能把账号密码还原出来
# 2015年6月30日 校园网取消了国内国际的限制。故将var1和相应的range取消
#-------------------------------------------------
import urllib
import urllib2
import BeautifulSoup
import Tkinter
import tkMessageBox
import os
import base64
#-------------------------------------------------
postData = {    'uid':'',
                'password':'',
                'range': '2',
                'operation': '',
                'timeout': '1',
            }
posturl = 'http://ipgw.neu.edu.cn/ipgw/ipgw.ipgw'
#-------------------------------------------------------------------------------------------------
if os.path.exists('nevertouch1.balabala') and os.path.exists('nevertouch2.balabala'):
    uid = open('nevertouch1.balabala','rb')
    pwd = open('nevertouch2.balabala','rb')
    postData['uid'] = base64.decodestring(uid.readline())
    postData['password'] = base64.decodestring(pwd.readline())
    uid.close()
    pwd.close()
#这段文件读取的程序特别蛋疼。。当把用户名和密码存储在同一个文件时会出现在第二次运行时密码默认为换行符的bug  
#而且好像比较麻烦。。所以采用了两个文件的方式。分别存储用户名和密码   只存储一行  即没有那个问题。但是安全性就是问题了
#-------------------------------------------------------------------------------------------------
def reg(postData,posturl):
    headers = {
               'User-Agent':'Mozilla/5.0 (Windows N9T 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
               'Referer':'http://ipgw.neu.edu.cn/basic.html',
        }
    postData['uid'] = username.get()
    postData['password'] = pwd.get()
#    if var1.get()==1:
#            postData['range'] = '1'
#    elif var1.get()==2:
#            postData['range'] = '2'
    if var2.get()==1:
            postData['operation'] = 'connect'
    elif var2.get()==2:
            postData['operation'] = 'disconnectall'
    postData = urllib.urlencode(postData)
    try:
        request = urllib2.Request(posturl,postData,headers)
        conn = urllib2.urlopen(request)
        html = conn.read()
        conn.close()
        html = unicode(html,'gb2312').encode('utf8')
        soup = BeautifulSoup.BeautifulSoup(html)
        tkMessageBox.showinfo("Tips", soup.td.text)
    except:
        tkMessageBox.showerror('Error', 'Please Check Your Connection To The Internet!')
    fp1 = open('nevertouch1.balabala','wb')
    fp2 = open('nevertouch2.balabala','wb')
    a = base64.encodestring(username.get())
    b = base64.encodestring(pwd.get())
    fp1.write(a)
    fp2.write(b)
    #a = username.get()+'\n'+pwd.get()
    fp1.close()
    fp2.close()
#------------------------------------------------------------------------------------------------
root = Tkinter.Tk()
root.title(unicode('connect'))
#root.geometry(100*100)
#var1 = Tkinter.IntVar()
var2 = Tkinter.IntVar()
pwd = Tkinter.Entry()
pwd.grid(row = 1,column = 2)
pwd.insert(0, postData['password'])
pwd['show'] = '*'
pwd_show = Tkinter.Label(root,text = 'password: ')
pwd_show.grid(row = 1,column = 0)
username = Tkinter.Entry(root)
username.grid(row = 0,column =2)
username.insert(0, postData['uid'])
username_show = Tkinter.Label(root,text = 'username: ')
username_show.grid(row = 0,column = 0)
#range1 = Tkinter.Radiobutton(root,variable = var1,text = 'in',value = 2)
#range1.grid(row = 2,column = 1)
#range2 = Tkinter.Radiobutton(root,variable = var1,text = 'out',value = 1)
#range2.grid(row = 2,column = 2)
op1 = Tkinter.Radiobutton(root,variable = var2,text = 'connect',value = 1)
op1.grid(row = 3,column = 1)
op2 = Tkinter.Radiobutton(root,variable = var2,text = 'disconnect',value = 2)
op2.grid(row = 3,column = 2)
submit = Tkinter.Button(root,text = 'log in',command = lambda:reg(postData,posturl))
submit.grid(row = 4,column = 1)
cancle = Tkinter.Button(root,text = 'quit',command = root.quit)
cancle.grid(row = 4,column = 2)
root.mainloop()
