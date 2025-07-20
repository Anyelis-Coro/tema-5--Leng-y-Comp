# Generated from Interfaces.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,9,35,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,4,0,11,8,0,11,0,
        12,0,12,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,4,2,27,8,
        2,11,2,12,2,28,1,3,1,3,1,3,1,3,1,3,0,0,4,0,2,4,6,0,0,33,0,10,1,0,
        0,0,2,16,1,0,0,0,4,20,1,0,0,0,6,30,1,0,0,0,8,11,3,2,1,0,9,11,3,4,
        2,0,10,8,1,0,0,0,10,9,1,0,0,0,11,12,1,0,0,0,12,10,1,0,0,0,12,13,
        1,0,0,0,13,14,1,0,0,0,14,15,5,0,0,1,15,1,1,0,0,0,16,17,5,1,0,0,17,
        18,5,6,0,0,18,19,5,8,0,0,19,3,1,0,0,0,20,21,5,2,0,0,21,22,5,6,0,
        0,22,23,5,4,0,0,23,24,5,5,0,0,24,26,5,8,0,0,25,27,3,6,3,0,26,25,
        1,0,0,0,27,28,1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,29,5,1,0,0,0,30,
        31,5,3,0,0,31,32,5,7,0,0,32,33,5,8,0,0,33,7,1,0,0,0,3,10,12,28
    ]

class InterfacesParser ( Parser ):

    grammarFileName = "Interfaces.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'auto'", "'iface'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "DIRECTIVE", 
                      "FAMILY", "METHOD", "ID", "IP", "NEWLINE", "WS" ]

    RULE_file_ = 0
    RULE_auto = 1
    RULE_iface = 2
    RULE_config = 3

    ruleNames =  [ "file_", "auto", "iface", "config" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    DIRECTIVE=3
    FAMILY=4
    METHOD=5
    ID=6
    IP=7
    NEWLINE=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class File_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(InterfacesParser.EOF, 0)

        def auto(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InterfacesParser.AutoContext)
            else:
                return self.getTypedRuleContext(InterfacesParser.AutoContext,i)


        def iface(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InterfacesParser.IfaceContext)
            else:
                return self.getTypedRuleContext(InterfacesParser.IfaceContext,i)


        def getRuleIndex(self):
            return InterfacesParser.RULE_file_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile_" ):
                listener.enterFile_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile_" ):
                listener.exitFile_(self)




    def file_(self):

        localctx = InterfacesParser.File_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 8
                    self.auto()
                    pass
                elif token in [2]:
                    self.state = 9
                    self.iface()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 12 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==2):
                    break

            self.state = 14
            self.match(InterfacesParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AutoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(InterfacesParser.ID, 0)

        def NEWLINE(self):
            return self.getToken(InterfacesParser.NEWLINE, 0)

        def getRuleIndex(self):
            return InterfacesParser.RULE_auto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAuto" ):
                listener.enterAuto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAuto" ):
                listener.exitAuto(self)




    def auto(self):

        localctx = InterfacesParser.AutoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_auto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(InterfacesParser.T__0)
            self.state = 17
            self.match(InterfacesParser.ID)
            self.state = 18
            self.match(InterfacesParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(InterfacesParser.ID, 0)

        def FAMILY(self):
            return self.getToken(InterfacesParser.FAMILY, 0)

        def METHOD(self):
            return self.getToken(InterfacesParser.METHOD, 0)

        def NEWLINE(self):
            return self.getToken(InterfacesParser.NEWLINE, 0)

        def config(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InterfacesParser.ConfigContext)
            else:
                return self.getTypedRuleContext(InterfacesParser.ConfigContext,i)


        def getRuleIndex(self):
            return InterfacesParser.RULE_iface

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIface" ):
                listener.enterIface(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIface" ):
                listener.exitIface(self)




    def iface(self):

        localctx = InterfacesParser.IfaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_iface)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(InterfacesParser.T__1)
            self.state = 21
            self.match(InterfacesParser.ID)
            self.state = 22
            self.match(InterfacesParser.FAMILY)
            self.state = 23
            self.match(InterfacesParser.METHOD)
            self.state = 24
            self.match(InterfacesParser.NEWLINE)
            self.state = 26 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 25
                self.config()
                self.state = 28 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConfigContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIRECTIVE(self):
            return self.getToken(InterfacesParser.DIRECTIVE, 0)

        def IP(self):
            return self.getToken(InterfacesParser.IP, 0)

        def NEWLINE(self):
            return self.getToken(InterfacesParser.NEWLINE, 0)

        def getRuleIndex(self):
            return InterfacesParser.RULE_config

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfig" ):
                listener.enterConfig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfig" ):
                listener.exitConfig(self)




    def config(self):

        localctx = InterfacesParser.ConfigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_config)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(InterfacesParser.DIRECTIVE)
            self.state = 31
            self.match(InterfacesParser.IP)
            self.state = 32
            self.match(InterfacesParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





