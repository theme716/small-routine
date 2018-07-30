import os


def main():
    for i in range(2):
        os.fork()
        print('hello fork')


if __name__ == '__main__':
    main()

'''
第一次: 1*2d
第二次: 1*2*2
第三次: 1*2*2*2

i = 0

子
    print 1
    
    i = 1
        主
            print 2 
        子 
            print 2 
            
主
    print 1
    
    i = 1
        主:
            print 2
        子:
            print 2
            i=2


'''