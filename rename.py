# coding=utf-8
import os
import datetime


#将指定的文件夹下的文件根据创建日期重命名
#文件名格式为 2015-01-08.jpg
#若是同一天有多个文件则为2015-01-08_12-2-3.jpg
def batchRename(dir):
    fs = os.listdir(dir);
    #需切换到该目录，应该下面遍历时的fn仅仅是文件名，不包含路径
    os.chdir(dir)
    for fn  in fs:
        timestamp = os.path.getmtime(fn);
        date = datetime.datetime.fromtimestamp(timestamp)
        newfilename = date.strftime('%Y-%m-%d.jpg')
        if os.path.exists(newfilename):
                print newfilename;
                #文件名不能包含 : 冒号，在windows系统下会报错哦
                newfilename=date.strftime('%Y-%m-%d_%H-%M-%S.jpg')
        os.rename(fn,newfilename)
        
if __name__ == '__main__':
    dir = "c:\\Camera";
    batchRename(dir);
    
