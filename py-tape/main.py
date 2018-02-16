import argparse,subprocess,glob,configparser,sys
from pathlib import Path
def main():    
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
        subprocess.call([sys.executable,file])
if __name__ == "__main__":
    main()