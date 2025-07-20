# Generated from Interfaces.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .InterfacesParser import InterfacesParser
else:
    from InterfacesParser import InterfacesParser

# This class defines a complete listener for a parse tree produced by InterfacesParser.
class InterfacesListener(ParseTreeListener):

    # Enter a parse tree produced by InterfacesParser#file_.
    def enterFile_(self, ctx:InterfacesParser.File_Context):
        pass

    # Exit a parse tree produced by InterfacesParser#file_.
    def exitFile_(self, ctx:InterfacesParser.File_Context):
        pass


    # Enter a parse tree produced by InterfacesParser#auto.
    def enterAuto(self, ctx:InterfacesParser.AutoContext):
        pass

    # Exit a parse tree produced by InterfacesParser#auto.
    def exitAuto(self, ctx:InterfacesParser.AutoContext):
        pass


    # Enter a parse tree produced by InterfacesParser#iface.
    def enterIface(self, ctx:InterfacesParser.IfaceContext):
        pass

    # Exit a parse tree produced by InterfacesParser#iface.
    def exitIface(self, ctx:InterfacesParser.IfaceContext):
        pass


    # Enter a parse tree produced by InterfacesParser#config.
    def enterConfig(self, ctx:InterfacesParser.ConfigContext):
        pass

    # Exit a parse tree produced by InterfacesParser#config.
    def exitConfig(self, ctx:InterfacesParser.ConfigContext):
        pass



del InterfacesParser