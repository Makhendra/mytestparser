#!/usr/bin/env python3
import os

PATH_DIR = os.getcwd()


def wrapper(val):
    txt = '<a href="/poems/'+val+'">'+val+'</a>'
    return txt


posts = os.listdir(PATH_DIR+'/poems')
posts = sorted(posts)
posts = map(wrapper, posts)

f = open(PATH_DIR+'/index.html', 'r')
print("Content-type: text/html\n")
posts_txt = '<br>'.join(posts)
print(f.read().format(posts=posts_txt))
