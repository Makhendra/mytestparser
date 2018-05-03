#!/usr/bin/env python3
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

import os
import cgi


PATH_DIR = os.getcwd()


def wrapper(val):
    txt = '<a href="?poem='+val+'">'+val+'</a>'
    return txt


print("Content-type: text/html\n")
arguments = cgi.FieldStorage()


if len(arguments.keys()) >= 1:
    f = open('./poems/'+arguments['poem'].value, 'r', encoding="utf-8")
    text = f.read()
    print(text)
    print('ААА авыа')
    f.close()
else:
    f = open(PATH_DIR+'/index.html', 'r')
    posts = os.listdir('./poems')
    posts = sorted(posts)
    posts = list(map(wrapper, posts))
    posts_txt = '<br>'.join(posts)
    print(f.read().format(posts=posts_txt))
    f.close()
