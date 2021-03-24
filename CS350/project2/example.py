
from nfa import *
import re

def lex(s):
    toks = []
    m = re.match(r"^\s*([a-z]|[0-9]|\||\(|\)|\*)", s)
    while m != None:
        toks.append(m.group(1))
        s = s[len(m.group(0)):]
        m = re.match(r"^\s*([a-z]|[0-9]|\||\(|\)|\*)", s)
    return toks

def parse(s):
    toks = lex(s)
    def peek(n):
        nonlocal toks
        if n < len(toks):
            return toks[n]
        else:
            return ""
    def expect(tok):
        nonlocal toks
        if peek(0) == tok:
            toks = toks[1:]
        else:
            print("Error, expected token '"+str(tok)+"', got: "+str(toks))
            exit(1)
    def isx(s):
        return re.match(r"^([a-z]|[0-9])$", s) != None
    def parseR():
        r = parseJ()
        while peek(0) == "|":
            expect("|")
            r = DisjRegex(r, parseJ())
        return r
    def parseJ():
        j = parseK()
        while isx(peek(0)) or peek(0) == "(":
            j = SeqRegex(j, parseK())
        return j
    def parseK():
        k = parseA()
        while peek(0) == "*":
            expect("*")
            k = StarRegex(k)
        return k
    def parseA():
        if peek(0) == "(":
            expect(peek(0))
            if peek(0) == ")":
                return EpsilonRegex()
            else:
                p = parseR()
                expect(")")
                return p
        elif isx(peek(0)):
            x = peek(0)
            expect(x)
            return CharRegex(x)
        else:
            print("Error!")
            exit(1)
    return parseR()
