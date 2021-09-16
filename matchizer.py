import requests
import re 
import urllib3 
import argparse
import pyfiglet
from concurrent.futures import ThreadPoolExecutor as PoolExecutor
from sys import exit 


# Version 1.2 -------------------------------------------------------------------+
#                               requamtch.py
# +------------------------------------------------------------------------------+


#======================= Start Arguments ====================
parser_arg_menu = argparse.ArgumentParser(prog='tool', formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=20))
parser_arg_menu.add_argument("-urls", help="urls file to request Ex: urls.txt", metavar="<file>",  required=False)
parser_arg_menu.add_argument("-match", help="String Match Ex.. \"admin-panel\"",  metavar="<string>", required=False)
parser_arg_menu.add_argument("-URL", help="If You Need To Plus additional path on all urls in Get Request",  metavar="<string>", required=False)
parser_arg_menu.add_argument("-include", help="Return Matching Value",  required=False , action='store_true')
parser_arg_menu.add_argument("-exclude", help="Return Not Matching Value",  required=False , action='store_true')
parser_arg_menu.add_argument("-thread", help="Enter Thread Number To MultiProccess Python [Speed Tool]",  metavar="<20>", default=100, required=False)
parser_arg_menu.add_argument("-banner", help="Print Banner",  required=False )
parser_arg_menu.add_argument("-o", help="Output File", metavar="<file>",  required=False)

arg_menu = parser_arg_menu.parse_args()
MAX_CONECTION_THREAD = int(arg_menu.thread) if arg_menu.thread else int(100)

#======================= End Arguments  =====================

class color:
    header = '\035[90m'
    blue = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'
    underLine = '\033[4m'
    notic = '\033[5;91m'


urllib3.disable_warnings()

# Print Banner
if arg_menu.banner:
    result = pyfiglet.figlet_format(arg_menu.banner)
    print(color.bold + color.red + result + color.end)


def main(single_url):
    url = single_url
    global search
    search = None

    try:
        # [if statement inside variable] if found -URL arg var response = url+value -URL else response = url
        response = requests.get(url+arg_menu.URL) if arg_menu.URL else requests.get(url)
        search = re.search(arg_menu.match , response.text)
        search = bool(search)

    except Exception as er:
    	pass

    if arg_menu.include:
        if search == True:
            if arg_menu.o:
                # [print with if statement] print url with value -URL arg if found , if not found -URL arg print single url 
                print(color.green + url+arg_menu.URL + color.end if arg_menu.URL else color.green + url + color.end ,end='\n')
                a_file = open(arg_menu.o , 'a+')
                a_file.writelines(url+'\n')
                a_file.close()

            else:
                # [print with if statement] print url with value -URL arg if found , if not found -URL arg print single url 
                print(color.green + url+arg_menu.URL + color.end if arg_menu.URL else color.green + url + color.end ,end='\n')
                #print(color.green + url + color.end ,end='\n')

    elif arg_menu.exclude:
        if search == False:
            if arg_menu.o:
                print(color.green + url+ color.end ,end='\n')
                a_file = open(arg_menu.o , 'a+')
                a_file.writelines(url+'\n')
                a_file.close()
            else:
                print(color.green + url+ color.end ,end='\n')


#  Making sure we are running this script directly..
#  not importing it from another script 
if __name__ == "__main__":

	# Make some checks
    if not arg_menu.urls:
        print("-urls needed")
        exit(1)
  
    if not arg_menu.match:
        print("-match needed")
        exit(1)

    if not arg_menu.include and not arg_menu.exclude:
        print("-include or -exclude should selected")
        exit(1)

    with open(arg_menu.urls, 'r') as f:
        urls_list = [line.rstrip() for line in f]

    with PoolExecutor(max_workers=20) as executor:
        for _ in executor.map(main, urls_list):
            pass
