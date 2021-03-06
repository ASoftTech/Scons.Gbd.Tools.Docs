"""
Used by scons on startup to look for plugins / tools
"""

from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

from Scons.Plugins import BasePlugin


class scons_gbd_docs(SconsBasePlugin):

    def get_metadata(self):
        """return metadata associated with the plugin"""
        self.metadata = {
            'name' = 'scons_gbd_docs',
            'description' = 'Documentation tools for use with SCons, e.g. MkDocs, Doxygen',
            'author' = 'grbd'}
        return self.metadata

    def on_tool_load(self):
        """return a list of namespace / toolpath pairs"""
        # Test multiple toolspecs
        tools =
        [
            {'namespace': 'Gbd.Docs.Mkdocs',
             'toolpath': PyPackageDir('scons_gbd_docs.Gbd.Docs.Mkdocs').abspath},
            {'namespace': 'Gbd.Docs.Doxygen',
             'toolpath': PyPackageDir('scons_gbd_docs.Gbd.Docs.Doxygen').abspath}
        ]
        self.toolspecs = tools
        return self.toolspecs


#    def on_tool_load(self):
#        """return a list of namespace / toolpath pairs"""
#        # Test single toolspec
#        tool = {
#                'namespace': 'Gbd.Docs',
#                'toolpath': PyPackageDir('scons_gbd_docs.Gbd.Docs').abspath,
#               }
#        self.toolspecs = [tool]
#        return self.toolspecs
