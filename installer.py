#!/usr/bin/python3
import os
import sys

def main():
    path = sys.path[0]
    pathlist = path.split("/")
    user = pathlist[1]
    if user == 'root':
        user = '/root/'
    else:
        user = '/home/'+pathlist[2]+'/'
    if os.path.exists(path+"/siteopener.py"):
        pathlist.append("siteopener.py")
        path = '/'.join(pathlist)
    else:
        print("can't find siteopener.py in this directory.. check its here!")
        exit()
    bash_loc = user+".bashrc"
    try:
        bashrc = rcopener(bash_loc)
        if "alias ff='" in bashrc:
            print('already installed!')
        else:
            try:
                write_alias(bash_loc, bashrc, path)
                print('''
    success! now press ctrl+alt+backspace to restart
    your session, start a commandline (ctrl+alt+t) and type 'ff help'
    ''')
            except:
                print('something went wrong editing the bashrc file... ',
                      'perhaps a permissions thing')
    except:
        print("looks like something went wrong. check you have a .bashrc file",
              "in your home directory")

    

def write_alias(user, bashrc, path):
    new_line = "alias ff='"+path+"'"
    bashrc = bashrc + new_line
    file = open(user,'w')
    file.write(bashrc)
    file.close()
    
def rcopener(arg):
    file = open(arg, 'r')
    cont = file.read()
    file.close()
    return str(cont)

main()
