import sublime, sublime_plugin,os

class ClipCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		os.system("~/repo/scripts/clip.sh")
		self.view.insert(edit, 0, sublime.get_clipboard())
 