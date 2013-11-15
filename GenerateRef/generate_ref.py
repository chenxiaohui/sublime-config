#!/usr/bin/python
#coding=utf-8
#Filename:generate_ref.py

import sublime, sublime_plugin

class GeneraterefCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sels = self.view.sel()
        lines=[]
        for sel in sels:
            lines += (self.view.substr(sel)).strip("\n").split("\n")
        outlines=[]
        for line in lines:
            idx1 = line.find(":")
            index = line[:idx1]
            idx2 = line.find('"', idx1)
            url = line[idx1+1:idx2].strip(' ')
            title = line[idx2:].strip('"')
            outlines.append('\n>\%s %s, <%s>'%(index,title,url))
        self.view.insert(edit, sel.end(),"\n###参考文献:\n".decode("utf-8") + "\n".join(outlines))
