import os

# 获取进程的id
print(os.getpid())
# 获取父级进程id
print(os.getppid())

# 创建子进程(只在类Linux 和 类unix 系统中，有fork(),相当于复制程序)
# os.fork()

