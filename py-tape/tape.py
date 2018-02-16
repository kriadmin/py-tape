import os,sys,argparse,runpy,configparser,glob,subprocess
from pathlib import Path
from colorama import *
os.system('')
def printf(condition,comment,message=None):
    if comment != None:
        if condition == 'ok':
            print(f'\n    {Fore.GREEN} √ {Style.RESET_ALL}{comment}')
        elif condition == 'not_ok':
            print(f'''\n{Fore.RED}
      × {comment}
      -------------------
      {Fore.BLUE}{message}{Style.RESET_ALL}
'''.strip())
class Tape():
    def __init__(self):
        pass
    def true(self,val,comment='should be truthy'):
        if (val == True) & (type(val) == bool):
            printf('ok',comment)
        else:
            printf('not_ok',comment)
    def equal(self,val1,val2,comment='should be equal'):
        if (val1==val2) & (type(val1) == type(val2)):
            printf('ok',comment)
        else:
            printf('not_ok',comment)
    def throws(self,fn,args=[],exception=None,comment='should throw a error'):
        e = None
        try:
            fn(*args)
        except:
            e = sys.exc_info()[0]
        finally:
            if (exception != None) & (e !=None):
                if e == exception:
                    printf('ok',comment)
                else:
                    printf('not_ok',comment)
            elif e != None:
                printf('ok',comment)
            else:
                printf('not_ok',comment)

tape = Tape()
def test(comment,fn):
    print(f'\n  \033[4m{comment}\033[0m')
    fn(tape)
def exec_full(filepath):
    global_namespace = {
        "__file__": filepath,
        "__name__": "__main__",
    }
    with open(filepath, 'rb') as file:
        exec(compile(file.read(), filepath, 'exec'), global_namespace)

'''if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('files',help="Run tape on all the provided files.",type=str,nargs='*')
    parser.add_argument('--ini','-i',help="Ini file configuration.")
    args = parser.parse_args()
    if args.ini == None:
        args.ini = 'config.ini'
    if Path(args.ini).is_file():
        config = configparser.ConfigParser()
        config.read(args.ini)
        python_files = config['tape']['python_files']
    else:
        python_files = '*_test.py'
    files =args.files+ glob.glob('**/'+python_files,recursive=True)
    for file in files:
        subprocess.call([sys.executable,file])'''