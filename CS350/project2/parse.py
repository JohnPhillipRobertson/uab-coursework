#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from syntax import *


# I *John Robertson* have written all of this project myself, without any
# unauthorized assistance, and have followed the academic honor code.


def lex(s):
    # TODO: scan input string and return a list of its tokens
    s = s.strip()
    toks = []
    comp = re.compile(r".*(\/\*[\s\n\S]*?\*\/|\/\/[^\n]*).*", re.DOTALL)
    preM = re.match(comp, s)
    while preM != None:
        s = s.replace(preM.group(1), "").strip()
        preM = re.match(comp, s)

    # The interesting stuff is below
    m = re.match(r"^\s*([\(\)\{\}\-\*\^\+</=,:;]|[a-zA-Z0-9_\.]+)", s)
    while m != None:
        toks.append(m.group(1))
        s = s[len(m.group(0)):]
        m = re.match(
            r"^\s*([\(\)\{\}\-\*\^\+</=,:;]|[a-zA-Z0-9_\.]+)", s)
    return toks


def parse(tokens):
    # TODO: parse and return an AST node or ErrorMsg object
    # PSLXCETFARQ
    errors = []

    def peek(n):
        nonlocal tokens
        if n < len(tokens):
            return tokens[n]
        else:
            return ""

    def expect(tok):
        nonlocal tokens
        if peek(0) == tok:
            tokens = tokens[1:]
        else:
            # maybe this should return the ErrorMsg() obj instead
            print("Error, expected token '"+str(tok)+"', got: "+str(tokens))
            nonlocal errors
            errors.append(ErrorMsg(tok))

    def isx(s):
        return re.match(r"^[A-Za-z_0-9.]*$", s) != None

    def parseP():
        p = parseS()
        while peek(0) == ";":
            expect(";")
            p = SeqStmt(p, parseS())
        return p

    def parseS():
        statement = None
        if peek(0) == "proc":
            expect("proc")
            f = peek(0)
            try:
                assert isx(f)
                expect(f)
                expect("(")
                params = parseL([])
                expect(")")
                expect("{")
                body = parseP()
                expect("}")
                statement = ProcStmt(Var(f), params, body)
            except AssertionError:
                statement = ErrorMsg(f)

        elif peek(0) == "if":
            expect("if")
            guard = parseC()
            expect("{")
            thenbody = parseP()
            expect("}")
            expect("else")
            expect("{")
            elsebody = parseP()
            expect("}")
            statement = IfStmt(guard, thenbody, elsebody)

        elif peek(0) == "while":
            expect("while")
            guard = parseC()
            expect("{")
            body = parseP()
            expect("}")

            statement = WhileStmt(guard, body)

        elif peek(0) == "print":
            expect("print")
            rhs = parseC()
            statement = PrintStmt(rhs)
        else:
            statement = parseC()

        return statement

    def parseL(l):
        if isx(peek(0)):
            x = peek(0)
            expect(x)
            l.append(Var(x))
        while peek(0) == ",":
            expect(",")
            x = parseL(l)

        return l

    def parseC():
        e = parseE()
        if peek(0) == "<":
            expect("<")
            rhs = parseE()
            e = LessThan(e, rhs)
        elif peek(0) == "=":
            expect("=")
            rhs = parseE()
            e = Equal(e, rhs)
        return e

    def parseE():
        t = parseT()
        while peek(0) == "+" or peek(0) == "-":
            if peek(0) == "+":
                expect("+")
                rhs = parseT()
                t = Plus(t, rhs)
            elif peek(0) == "-":
                expect("-")
                rhs = parseT()
                t = Minus(t, rhs)
        return t

    def parseT():
        f = parseF()
        while peek(0) == "*" or peek(0) == "/":
            if peek(0) == "*":
                expect("*")
                rhs = parseF()
                f = Mult(f, rhs)
            elif peek(0) == "/":
                expect("/")
                rhs = parseF()
                f = Div(f, rhs)
        return f

    def parseF():
        a = parseA()
        while peek(0) == "^":
            expect("^")
            lhs = parseA()
            a = Expo(a, lhs)
        return a

    def parseA():
        ret = None
        p2 = None
        p = peek(0)
        try:
            p2 = peek(1) + peek(2)
        except IndexError:
            pass
        if p == "(":
            expect(p)
            ret = parseC()
            expect(")")
        elif set(list(p)).issubset(set(list("0123456789."))):
            expect(p)
            ret = Lit(p)
        elif p[0].isalpha() or p == "_" or p2 == ":=":
            if p2 == ":=":
                expect(p)
                expect(":")
                expect("=")
                rhs = parseC()
                ret = Assign(Var(p), rhs)
            elif "(" == p2[0]:
                f = p
                expect(f)
                expect("(")
                args = parseR()
                ret = Call(Var(f), args)
                expect(")")
            else:
                ident = p
                expect(ident)
                ret = Var(ident)

        else:
            ret = ErrorMsg(p)

        return ret

    def parseR():
        c = []
        if peek(0) != "":
            if isx(peek(0)):
                c.append(parseC())
            while peek(0) == ",":
                expect(",")
                c += parseR()
        return c

    return parseP()


program = """
proc ack(ack, m, n) {
    if m = 0 {
        np := n + 1;
        np
    }
    else {
        if m > 0 {
            one := 1;
            mp := m - one;
            if n = 0 {
                ack(ack, mp, one)
            }
            else {
                np := n - 1;
                retack := ack(ack, m, np);
                ack(ack, mp, retack)
            }
        }
    }
};

a := 2
b := 2
print ack(ack, 2, 2)

"""

parse(lex(program))
