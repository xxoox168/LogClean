import re
import sys


class FunctionNameFalseException(Exception):
    '''自定义的异常类'''
    def __init__(self, functionname, argname):
        self.functionname = functionname
        self.argname = argname


def logchunkcheck(args):
    funname = sys._getframe(0).f_code.co_name
    callname = sys._getframe(1).f_code.co_name
    print(funname)

    if 'logchunk.py' != args[0].split('/')[-1]:
        print('%s 不能被 %s调用，只能被logchunk调用'%(funname, args[0].split('/')[-1]))
        raise FunctionNameFalseException(funname, callname)


def main():
    args = sys.argv
    logchunkcheck(args)


if __name__ == "__main__":
    main()