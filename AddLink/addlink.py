#!/usr/bin/env python
#coding=utf-8
#Filename:add_Link.py

import sublime, sublime_plugin

def split(msg):
    """"""
    idx, url, title = '', '', ''
    pos = msg.find(' ')
    if pos > 0:
        idx = msg[:pos].strip()
        msg = msg[pos:].strip()
        pos = msg.find(' ')
        if pos > 0:
            url = msg[:pos].strip()
            title = msg[pos:].strip()
        else:
            url = msg
    return idx, url, title

def done(msg):
    """"""
    try:
        idx, url, title = split(msg)
        window = sublime.active_window()
        view = window.active_view()
        edit = view.begin_edit()

        sels = view.sel()
        assert len(sels) == 1
        sel = sels[0]
        content = view.substr(sel)
        view.replace(edit, sel, "[%s][%s]" % (content, idx))

        view.insert(edit, view.size(), '\n[%s]: %s "%s"' % (idx, url, title))

        view.end_edit(edit)
    except Exception:
        pass

def change(url):
    """"""
    pass

def cancel():
    """"""
    pass

class AddlinkCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        window = sublime.active_window()
        window.show_input_panel("input idx+url", "", done, change, cancel)
