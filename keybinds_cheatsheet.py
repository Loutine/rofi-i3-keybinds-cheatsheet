#!/usr/bin/env python
#set padding
import sys
import re
bindsym = re.compile("bindsym (.*?) (.*)")
mode = re.compile("mode \"(.*)\" {([\S\s]*)}")
clear_exec = re.compile("exec( --no-startup-id)? ")

def find_symbind(dict, text,mode="default"):
    if mode not in dict:
        dict[mode] = []
    for tuple in bindsym.findall(text):
        dict[mode].append(tuple)
        
def key_bind_paddding(mode, tuple, padding_length):
    if mode == "default":
        mode = ""
    else:
        mode = "(" + mode + ")"
    keybind, intro = tuple
    intro = clear_exec.sub("", intro)
    keybind = keybind + mode
    return keybind.ljust(padding_length, " ") + intro

if __name__ == "__main__":
    dict = {}
    i3_config = sys.argv[1]
    padding = int(sys.argv[2])
    with open(i3_config, "r") as f:
        text = f.read()
    for modeblock in mode.findall(text):
        find_symbind(dict, modeblock[1], mode=modeblock[0])
    text = mode.sub("", text)
    find_symbind(dict, text)
    print("\0prompt\x1fI3 binds:")
    for mode in dict:
        for tuple in dict[mode]:
            print(key_bind_paddding(mode,tuple,padding))
    
        
