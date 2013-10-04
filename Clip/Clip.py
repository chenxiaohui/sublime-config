import sublime, sublime_plugin,os

class ClipsshCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		os.system("~/repo/scripts/clip.sh")
		self.view.insert(edit, self.view.sel()[0].b, sublime.get_clipboard())

