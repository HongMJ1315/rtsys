import time
import os
import math
import ntplib
from flask import Flask, request, render_template, redirect, url_for
import jinja2
import time
import datetime
app = Flask(__name__)

PASSWORD="123456"

time_list=[]

time_int=["09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00"]

allow = time.strptime("2022/11/17 17:07:00",'%Y/%m/%d %H:%M:%S')

memweek = { 0:"星期一" , 1:"星期二", 2:"星期三", 3:"星期四", 4:"星期五", 5:"星期六", 6:"星期日"}


def get_now():
    c = ntplib.NTPClient()
    try:
        response = c.request('time.cloudflare.com')
        print("ntp server")
        ts = response.tx_time
    except: ts=time.time()
    return ts

@app.route('/login')
def root():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    global allow
    global time_list
    if request.method == 'POST':
        try:
            password = request.form['password']
            if(password==PASSWORD):
                return render_template("settime.html")
            else:
                #回到首頁
                return redirect(url_for('mainPage'))
        except:
            times = request.form['times']
            print(times)
            try: 
                allow=time.strptime(times,'%Y/%m/%d %H:%M:%S')
                return str(times +"<a href='/'>Go Back</a>")
            except:
                if(times=="clear"):
                    print("clear")
                    for i in range(0,7):
                        for j in range(0,14):
                            time_list[i][j]=0
                    f=open("mem.txt","w",encoding="utf-8")
                    f.write(str(time_list))
                    f.close()
                    return str("all clear<a href='/'>Go Back</a>")
            return render_template('error.html' )
                    
@app.route("/")
def mainPage():
    now = math.floor(time.mktime(allow)-get_now())
    if(now>=0):
        s=now%60
        ss=""
        if(s<10): ss="0"+str(s)
        else: ss=str(s)
        res=str(now//60)+":"+ss
    else:
        res="Start!!"
    sheet="<table><thead><td>時間</td><td>星期一</td><td>星期二</td><td>星期三</td><td>星期四</td><td>星期五</td><td>星期六</td><td>星期日</td></thead><tbody>"
    for j in range(0,14):
        sheet+="<tr><td style='color: white;background-color: darkblue;'>"+time_int[j]+"</td>"
        for i in range(0,7):
            sheet+="<td"
            if(time_list[i][j]==0):
                sheet+=">"+chr(ord('A')+j)
            else:
                sheet+=" class='used'>"+time_list[i][j]
            sheet+="</td>"
        sheet+="</tr>"
    sheet+='</tbody></table>'           
    
    return render_template('index.html',timer=res,sheet=sheet)

class Band:
    week = 0
    times = 0
    name=""
    def __init__(self,week,times,name):
        self.week = week
        self.times = times
        self.name = name
    

    
def process(band_list):
    print("in proess")
    f=open("mem.txt","w",encoding="utf-8")
    
    ret=[]
    for i in range(0,len(band_list)):
        # print(len(band_list[i].times))
        # print(band_list[i].week)
        # print(len(band_list[i].name))
        
        if(band_list[i].name==""):
            continue
        elif(len(band_list[i].times)==0):
            ret.append(2)
            continue
        elif(band_list[i].week==-1):
            ret.append(2)
            continue
        isok=0
        for j in band_list[i].times:
            if(time_list[int(band_list[i].week)][int(j)]==0):
                isok=1
            else: 
                isok=0
                break
        if(isok==1):
            for j in band_list[i].times:
                time_list[int(band_list[i].week)][int(j)]=band_list[i].name
            ret.append(1)
        else: ret.append(0)
    f.write(str(time_list))
    f.close()
    return ret
            

@app.route("/submit",methods=['POST','GET'])
def getForm():
    if request.method == 'POST':
        now=get_now()
        try:
            if(now-time.mktime(allow)>=0):
                try: print(now-time.mktime(allow))
                except:
                    print(type(now), type(time.mktime(allow)))
                band_list=[]
                for i in range(1,6):
                    bn="band_name"+str(i)
                    w="week"+str(i)
                    t="time_interval"+str(i)
                    try: name=request.form[bn]
                    except: name=""
                    try: week=int(request.form[w])
                    except: week=-1
                    try : times=request.form.getlist(t)
                    except : times=[]
                    band=(Band(week,times,name))
                    band_list.append(band)
                res=process(band_list)
                print("result ",res)
                inner=""
                for i in range(0, len(res)):
                    if(res[i]!=2):
                        inner+="<tr><td>"+band_list[i].name+"</td><td>"+memweek[band_list[i].week]+"</td><td>"
                        for j in band_list[i].times:
                            inner+=chr(ord('A')+int(j))
                        if(res[i]==0):
                            inner+="</td><td class='wr'>Too Late</td></tr>"
                        elif(res[i]==1):
                            inner+="</td><td class='ac'>Accept</td></tr>"
                        else:
                            inner+="</td><td class='wr'>Denied</td></tr>"
                    elif(res[i]==2):
                        inner+="<tr><td>"+band_list[i].name+" </td><td></td><td></td><td class='wr'>Denied</td></li>"
                return render_template('submit.html', result=inner)
            else:
                return render_template('quick.html' )
        except:
            return render_template('error.html' )

if __name__ == '__main__':
    for i in range(0,7):
        time_list.append([])
        for j in range(0,14):
            time_list[i].append(0)
    f=open("mem.txt","r",encoding="utf-8")
    time_list=eval(f.read())
    f.close()
    # app.run()
    app.run('0.0.0.0')
