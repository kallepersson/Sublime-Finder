import sublime_plugin
import os
import subprocess


class FinderCommand():
    def get_path(self, paths):
        if paths:
            return paths[0]
        elif self.window.active_view():
            return self.window.active_view().file_name()
        elif self.window.folders():
            return self.window.folders()[0]
        else:
            return '.'


class OpenFinderCommand(sublime_plugin.WindowCommand, FinderCommand):
    def run(self, paths=[], parameters=None):

        path = self.get_path(paths)

        arg = ['open', '-R', path]
        subprocess.Popen(arg)
