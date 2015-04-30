#!/usr/bin/python
#coding=utf-8
#Filename:Clip.py
import sublime, sublime_plugin,os

class ClipsshCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		os.system("~/repo/scripts/clip.sh 10.232.31.8")
		self.view.insert(edit, self.view.sel()[0].b, sublime.get_clipboard())

class Cliptest0Command(sublime_plugin.TextCommand):
	def run(self, edit):
		os.system("~/repo/scripts/clip.sh 10.232.36.30")
		self.view.insert(edit, self.view.sel()[0].b, sublime.get_clipboard())

class Cliptest2Command(sublime_plugin.TextCommand):
	def run(self, edit):
		os.system("~/repo/scripts/clip.sh 10.232.36.32")
		self.view.insert(edit, self.view.sel()[0].b, sublime.get_clipboard())


