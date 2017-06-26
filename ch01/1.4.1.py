# -*- coding:utf-8 -*-

## 使用os模块中的fork方式实现多进程 (*nix系统适用)
# import os
# if __name__ == '__main__':
#     print 'current Process (%s) start ...' %(os.getpid())
#     pid = os.fork()
#     if pid < 0:
#         print 'error in fork'
#     elif pid == 0:
#         print 'I am child process(%s) and my parent process is (%s)',(os.getpid(),os.getppid())
#     else:
#         print 'I(%s) created a chlid process (%s).', (os.getpid(), pid)


# 使用multiprocessing模块创建多进程
import os
from multiprocessing import Process
# 子进程要执行的代码
def run_proc(name):
    print 'Child process %s (%s) Running...' % (name, os.getpid())
if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    for i in range(5):
        p = Process(target=run_proc, args=(str(i),))
        print 'Process will start.'
        p.start()
    p.join()
    print 'Process end.'