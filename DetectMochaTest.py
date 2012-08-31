import sublime, sublime_plugin
import os

class MochaDetectFileTypeCommand(sublime_plugin.EventListener):
  """ Detects test files written in js"""
  """ Modified for Mocha tests and Sublime Text 2 """
  """ Original Gist for Rails here: https://gist.github.com/925008 """

  def on_load(self, view):
    filename = view.file_name()
    if not filename: # buffer has never been saved
      return

    name = os.path.basename(filename.lower())
    dirname = os.path.dirname(filename.lower()).rpartition('/')[2]
    if dirname[:4] == "test":
      set_syntax(view, "Mocha", "Mocha")


def set_syntax(view, syntax, path=None):
  if path is None:
    path = syntax
  view.settings().set('syntax', 'Packages/'+ path + '/' + syntax + '.tmLanguage')
  print "Switched syntax to: " + syntax