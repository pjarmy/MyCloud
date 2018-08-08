# 摘自 https://www.cnblogs.com/yeayee/p/4952022.html

# 单线程

from time import ctime,sleep

def music():
    for i in range(2):
        print("I was listening to music. %s" %ctime())
        sleep(1)

def move():
    for i in range(2):
        print("I was at the movies! %s" %ctime())
        sleep(5)

if __name__ == '__main__':
    music()
    move()
    print("all over %s" %ctime())


=========================== RESTART ================================
I was listening to music. Wed Aug  8 10:02:38 2018
I was listening to music. Wed Aug  8 10:02:39 2018
I was at the movies! Wed Aug  8 10:02:40 2018
I was at the movies! Wed Aug  8 10:02:45 2018
all over Wed Aug  8 10:02:50 2018



# coding=utf-8
import threading
from time import ctime,sleep

def music(func):
    for i in range(2):
        print("I was listening to %s. %s" %(func, ctime()))
        sleep(1)

def move(func):
    for i in range(2):
        print("I was at the %s! %s" %(func, ctime()))
        sleep(5)

if __name__ == '__main__':
    music(u'爱情买卖')
    move(u'阿凡达')
    print("all over %s" %ctime())

=========================== RESTART ================================
I was listening to 爱情买卖. Wed Aug  8 10:07:52 2018
I was listening to 爱情买卖. Wed Aug  8 10:07:53 2018
I was at the 阿凡达! Wed Aug  8 10:07:54 2018
I was at the 阿凡达! Wed Aug  8 10:07:59 2018
all over Wed Aug  8 10:08:04 2018





# 多线程
# thread有缺点，threading得到了弥补，所以直接学threading

# coding=utf-8
import threading
from time import ctime,sleep

def music(func):
    for i in range(2):
        print ("I was listening to %s. %s" %(func,ctime()))
        sleep(1)

def move(func):
    for i in range(2):
        print ("I was at the %s! %s" %(func,ctime()))
        sleep(5)

threads = []
t1 = threading.Thread(target=music, args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move, args=(u'阿凡达',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    print("all over %s" %ctime())


=========================== RESTART ================================
I was listening to 爱情买卖. Wed Aug  8 10:16:06 2018
all over Wed Aug  8 10:16:06 2018I was at the 阿凡达! Wed Aug  8 10:16:06 2018


I was listening to 爱情买卖. Wed Aug  8 10:16:07 2018
I was at the 阿凡达! Wed Aug  8 10:16:11 2018



setDaemon()
#     setDaemon(True)将线程声明为守护线程，必须在start()方法调用之前设置，如果不设置为守护进程，程序会被无限挂起。
# 子线程启动后，父线程也继续执行下去，当父线程执行完最后一条语句"all over..."后，没有等待子线程，直接退出了，同时子线程也一同结束

start()
    # 开始线程活动

#     从执行结果来看，子线程（muisc 、move ）和主线程（print "all over %s" %ctime()）都是同一时间启动，
# 但由于主线程执行完结束，所以导致子线程也终止。



# coding=utf-8
import threading
from time import ctime,sleep

def music(func):
    for i in range(2):
        print ("I was listening to %s. %s" %(func,ctime()))
        sleep(1)

def move(func):
    for i in range(2):
        print ("I was at the %s! %s" %(func,ctime()))
        sleep(5)

threads = []
t1 = threading.Thread(target=music, args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move, args=(u'阿凡达',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    t.join()

    print("all over %s" %ctime())

=========================== RESTART ================================
I was listening to 爱情买卖. Wed Aug  8 10:18:15 2018
I was at the 阿凡达! Wed Aug  8 10:18:15 2018
I was listening to 爱情买卖. Wed Aug  8 10:18:16 2018
I was at the 阿凡达! Wed Aug  8 10:18:20 2018
all over Wed Aug  8 10:18:25 2018

# 我们只对上面的程序加了个join()方法，用于等待线程终止。join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞。
# 注意:  join()方法的位置是在for循环外的，也就是说必须等待for循环里的两个进程都结束后，才去执行主进程。






...
def music(func):
    for i in range(2):
        print ("I was listening to %s. %s" %(func,ctime()))
        sleep(4)
...

=========================== RESTART ================================
I was listening to 爱情买卖. Wed Aug  8 10:28:18 2018
I was at the 阿凡达! Wed Aug  8 10:28:18 2018
I was listening to 爱情买卖. Wed Aug  8 10:28:22 2018
I was at the 阿凡达! Wed Aug  8 10:28:23 2018
all over Wed Aug  8 10:28:28 2018

# 虽然music每首歌曲从1秒延长到了4 ，但通多程线的方式运行脚本，总的时间没变化。





# player.py

# coding=utf-8
from time import sleep, ctime
import threading

def music(func):
    for i in range(2):
        print('Start playing:  %s! %s' %(func, ctime()))
        sleep(2)

def move(func):
    for i in range(2):
        print('Start playing: %s! %s' %(func, ctime()))
        sleep(5)

def player(name):
    r = name.split('.')[1]
    if r == 'mp3':
        music(name)
    else:
        if r == 'mp4':
            move(name)
        else:
            print('error: The format is not recongnized!')

list = ['爱情买卖.mp3','阿凡达.mp4']

threads = []
files = range(len(list))

# 创建线程
for i in files:
    t = threading.Thread(target=player,args=(list[i],))
    threads.append(t)

if __name__ == '__main__':
    # 启动线程
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()

    # 主线程
    print('end: %s' %ctime())

=========================== RESTART ================================
Start playing:  爱情买卖.mp3! Wed Aug  8 10:40:28 2018
Start playing: 阿凡达.mp4! Wed Aug  8 10:40:28 2018
Start playing:  爱情买卖.mp3! Wed Aug  8 10:40:30 2018
Start playing: 阿凡达.mp4! Wed Aug  8 10:40:33 2018
end: Wed Aug  8 10:40:38 2018





# super_player.py

# coding=utf-8
from time import sleep, ctime
import threading

def super_player(file,time):
    for i in range(2):
        print('Strar playing: %s! %s' %(file, ctime()))
        sleep(time)

# 播放的文件与播放时长
list = {'爱情买卖.mp3':3,'阿凡达.mp4':5,'我和你.mp3':4}

threads = []
files = range(len(list))

# 创建线程
for file,time in list.items():
    t = threading.Thread(target=super_player, args=(file, time))
    threads.append(t)

if __name__ == '__main__':
    # 启动线程
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()

    # 主线程
    print('end: %s' %ctime())


=========================== RESTART ================================
Strar playing: 爱情买卖.mp3! Wed Aug  8 10:53:49 2018
Strar playing: 阿凡达.mp4! Wed Aug  8 10:53:49 2018
Strar playing: 我和你.mp3! Wed Aug  8 10:53:49 2018
Strar playing: 爱情买卖.mp3! Wed Aug  8 10:53:52 2018
Strar playing: 我和你.mp3! Wed Aug  8 10:53:53 2018
Strar playing: 阿凡达.mp4! Wed Aug  8 10:53:54 2018
end: Wed Aug  8 10:53:59 2018





# 创建自己的多线程

# coding=utf-8
import threading
from time improt sleep, ctime

class MyThread(threading.Thread):

    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name=name
        self.func=func
        self.args=args

    def run(self):
        apply(self.func, self.args)

def super_player(file, time):
    for i in range(2):
        print('Start playing: %s! %s' %(file,ctime()))
        sleep(time)

list = {'爱情买卖.mp3':3,'阿凡达.mp4':5}

# 创建线程
threads = []
files = range(len(list))

for k,v in list.items():
    t



































1
