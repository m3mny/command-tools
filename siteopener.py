#!/usr/bin/python3
import os
import sys
dic_loc = sys.path[0]+"/.ff_sites.dict"

def check_sites():
        if os.path.exists(dic_loc):
                pass
        else:
                print('Writing defaults...')
                default_dic = {"fb":"www.facebook.com",
                       "yt":"www.youtube.com",
                       "inbox":"inbox.google.com",
                       "search":"www.duckduckgo.com/?q="}
                writer(default_dic)
                editor('print')         

def main():
        check_sites()
        if len(sys.argv)==1:
            open_url('blank')
        elif sys.argv[1] == 'add':
                editor('add')
        elif sys.argv[1] == 'remove':
                editor('remove')
        elif sys.argv[1] == 'print':
                editor('print')
        elif sys.argv[1] == 'search':
                term = sys.argv[2:]
                search(term)
        elif sys.argv[1] == 'help':
                print('''
Use 'ff' on its own to open firefox at your homepage

Use 'ff print' to print a list of saved websites you are currently able to open.
        its in the form {'name':'address'}

Use 'ff sitename' to open a saved address. Name multiple saved sites to open them
        all in new tabs, eg: 'ff yt fb' will open youtube and facebook.
        
Use 'ff add' to add a name and address to your list.
        for example 'ff add slipend www.slipend.co.uk'
        will mean you can open slipend.co.uk with  'ff slipend'.
        add will over-write an existing address if you use an existing name.
        
Use 'ff remove' to remove sites by name.
        multiple sites can be named to remove more than one at once.

Use 'ff search' to search any following terms in your favourite engine.
        for example: 'ff search something interesting to search for'
        by default it'll use duckduckgo, but you can change that by doing:
        'ff add search 'your_search_url_here''
        if you wanted to change to google for example, you'd use
        'google.com/search?q='
''')
        else:
                dic = reader()
                urls = []
                url_str = ''
                for i in dic:
                        for j in sys.argv[1:]:
                                if j == i:
                                        urls.append(i)
                if len(urls) == 0:
                        print ("I don't recognise this, try 'ff help'")
                        exit()
                elif len(urls) < len(sys.argv) - 1:
                        for m in sys.argv[1:]:
                                try:
                                        dic[m]
                                except:
                                        print ("I don't know {},".format(m),
                                               "you'll have to add it!")
                        print('Opening the ones I recognise...')
                        for l in urls:
                                url_str = url_str+dic[str(l)]+" "
                        open_url(url_str)
                else:
                        for l in urls:
                                url_str = url_str+dic[str(l)]+" "
                        open_url(url_str)

def reader():
        opener = open(dic_loc, 'r')
        dic = opener.read()
        opener.close()
        dic = eval(dic)
        return dic

def writer(args):
        dic = open(dic_loc, 'w')
        dic.write(str(args))
        dic.close()

def search(args):
        if len(args) == 0:
                print('You need something to search for!')
                exit()
        else:
                term = ''
                dic = reader()
                for i in args:
                        term = term+i+"+"
                term = term[:-1]
                try:
                        url = dic['search']+term+" "
                except:
                        print ("You had removed your search url,",
                               "added duckduckgo again for you...")
                        dic = reader()
                        dic['search'] = 'www.duckduckgo.com/?q='
                        writer(dic)
                        url = dic['search']+term+" "
                open_url(url)
        
def editor(fun):
        if fun == 'add':
                if len(sys.argv) != 4:
                        print('Syntax is: ff add name www.website.co.uk')
                else:
                        dic = reader()
                        dic[sys.argv[2]] = sys.argv[3]
                        writer(dic)
        elif fun == 'remove':
                if len(sys.argv) < 3:
                        print('You need to specify something to remove, can remove',
                              'more than one thing at once...')
                else:
                        args, dic = sys.argv[2:], reader()
                        for i in args:
                                try:
                                        print(dic[i],'removed')
                                        del dic[i]
                                        writer(dic)
                                except:
                                        print(i,'not in list')
                        
        elif fun == 'print':
                dic = reader()
                print(str(dic).replace(",", "\n"))

                
        
def open_url(args):
        if args == 'blank':
                print('Opening home page')
                os.system('firefox &')
        else:
                print ('Opening',args)
                os.system ('firefox '+args+'&')

main()
