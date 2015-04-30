#!/usr/bin/python
#coding=utf-8
#Filename:Clip.py
import sublime, sublime_plugin,os

class MdpreviewCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename=self.view.file_name()
        path= '/home/cxh/share/md_preview'
        os.system("pandoc %s -o %s/tmp.html --template=%s/default.html"%(filename, path, path))
        os.system("google-chrome %s/tmp.html"%path)
