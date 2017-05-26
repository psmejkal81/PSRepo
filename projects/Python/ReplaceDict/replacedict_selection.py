import sublime
import sublime_plugin
import re

class ReplacedictCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        colnames = eval(open('dictionary.txt', 'r').read())
        selection = self.view.sel()
        for region in selection:
            if not region.empty():
                sel_text = self.view.substr(region)
                pattern = re.compile(r'\b(' + '|'.join(colnames.keys()) + r')\b', re.IGNORECASE)
                result = pattern.sub(lambda x: colnames[x.group().upper()], sel_text)
                self.view.replace(edit, region, result)