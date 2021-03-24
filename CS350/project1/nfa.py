#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# I *John Robertson* have written all of this project myself, without any
# unauthorized assistance, and have followed the academic honor code.


from nfa_regex import *
from state import *
# Note: You may want to use the provided generateSVG() method below for visualizing,
# your NFAs/DFAs and for debugging. If not, you may remove it and the following import.
# You are not required to provide a working generateSVG method, but you may find it useful.
try:
    from graphviz import Digraph
except:
	pass



# TODO: This is your class for modeling NFAs/DFAs! Some is already stubbed out for you.
class NFA:
    """A class for NFAs that can be constructed from a Regex"""
    def __init__(self, r = None):
        """Constructs an empty-language NFA when r==None,
            or constructs an NFA from the provided Regex object."""
        self.r = r #s Save a reference to the regex itself
        if r == None:
            # If no Regex instance is provided: the empty language
            start = State()
            self.Q = {start}
            self.Sigma = set()
            self.s = start
            self.F = set()
            self.delta = set()
        elif isinstance(r, EpsilonRegex):
            start = State()
            self.Q = {start}
            self.Sigma = set()
            self.s = start
            self.F = {start}
            self.delta = set()
        elif isinstance(r, StarRegex):
            nfa0 = NFA(r.r0)
            start = State()
            self.Q = {start} | nfa0.Q
            self.Sigma = nfa0.Sigma
            self.s = start
            self.F = {start}
            self.delta = ({(start, "", nfa0.s), (min(nfa0.F), "", start)} | nfa0.delta)
        elif isinstance(r, SeqRegex):
            nfa0 = NFA(r.r0)
            nfa1 = NFA(r.r1)
            self.Q = nfa0.Q | nfa1.Q
            self.Sigma = nfa0.Sigma | nfa1.Sigma
            self.s = nfa0.s
            self.F = nfa1.F
            self.delta = ({(min(nfa0.F), "", nfa1.s)} | nfa0.delta | nfa1.delta)
        elif isinstance(r, DisjRegex):
            # Note how this is exactly the Disjunction construction
            # we saw in the slides for converting RE -> NFA
            nfa0 = NFA(r.r0)
            nfa1 = NFA(r.r1)
            start = State()
            end = State()
            self.Q = {start, end} | nfa0.Q | nfa1.Q #dubious
            self.Sigma = nfa0.Sigma | nfa1.Sigma
            self.s = start #dubious
            self.F = {end}
            # Explanation: below, min is nice for selecting an arbitrary
            # element; as we maintain as an invariant that self.F is
            # a singleton for the duration of NFA construction, this works well
            # (may not be the case for DFAs; also note: empty string is epsilon)
            self.delta = ({(start, "", nfa0.s), (start, "", nfa1.s),
                           (min(nfa0.F), "", end), (min(nfa1.F), "", end)}
                          | nfa0.delta | nfa1.delta)
        elif isinstance(r, CharRegex):
            start = State()
            end = State()
            self.Q = {start, end}
            self.Sigma = {r.x}
            self.s = start
            self.F = {end}
            self.delta = ({(start, r.x, end)})
        else:
            raise "NFA must be constructed from a Regex (or None)."


    def matches(self, s):
        # Note how move and epsilon closure (written correctly) may be used to
        # simulate an NFA or DFA (this code can work for both!)
        # See also: the nfa-dfa and subset algorithm slides from class for move, epsilonClosure.
        current = self.epsilonClosure({self.s})
        for x in s:
            current = self.epsilonClosure(self.move(current, x))
        if current & self.F == set():
            return False
        else:
            return True

    def epsilonClosure(self, qs):
        """Returns the set of states reachable from those in qs without consuming any characters."""
        retVal = qs
        temp = set()
        while temp != retVal:
            temp = retVal
            for mov in self.delta:
                if mov[1] == "" and mov[0] in retVal:
                    retVal = retVal | {mov[2]}
        return retVal

    def move(self, qs, x):
        """Returns the set of states reachable from those in qs by consuming character x."""
        retVal = set()
        for mov in self.delta:
            if mov[1] == x and mov[0] in qs:
                retVal = retVal | {mov[2]}
        return retVal

    def NFA_to_DFA(self):
        """Returns a DFA equivalent to self."""
        dfa = NFA()
        dfa.r = self.r
        startset = self.epsilonClosure({self.s})
        start = State(frozenset(startset))
        dfa.Q = {start}
        dfa.s = start
        dfa.Sigma = self.Sigma
        dfa.delta = set()
        dfa.F = set()
        marked = {start}
        while marked:
            d = marked.pop()
            for s in dfa.Sigma:
                dmv = self.move(d.name, s)
                dmvEps = self.epsilonClosure(dmv)
                dmvEps = State(frozenset(dmvEps))
                if dmvEps not in dfa.Q:
                    dfa.Q = dfa.Q | {dmvEps}
                    marked = marked | {dmvEps}
                dfa.delta = (dfa.delta | {(d, s, dmvEps)})
        for q in dfa.Q:
            if q.name & self.F:
                dfa.F = dfa.F | {q}
        return dfa

    def statecount(self):
        return len(self.Q)

    def isDFA(self):
        # Checks to see if the NFA is also a DFA:
        # i.e., reports True iff self.delta is a function
        for q in self.Q:
            outgoingset = set()
            for e in self.delta:
                if q == e[0]:
                    if e[1] in outgoingset or e[1] == "":
                        return False
                    outgoingset.add(e[1])
        return True


    def minimizeDFA(self):
        """Takes a DFA and returns a minimized DFA"""
        if self.isDFA() == False:
            raise "minimizeDFA must be provided a DFA"

        # Use partition refinement (to a fixpoint)
        parts = set()
        if self.F != set(): parts.add(frozenset(self.F))
        # TODO: Use Hopcroft's algorithm to produce a new, minimal
        #       DFA, and return it.
        # ...
        work = {self.F}
        while work:
            for P in work:
                p = P.copy()
                work.remove(p)
                for s in self.Sigma:
                    preds = set(frozenset([q for q in self.d if q in p]))
                    for part in parts:
                        if part & preds != set() and part-preds != set():
                            if part in work:
                                work = (work-part) | {parts & preds, parts-preds}
                            elif len(parts & preds) <= len(parts-preds):
                                work = work | {parts & preds}
                            else:
                                work = work | {parts - preds}
        mdfa = NFA()
        # ...
        mdfa = self.copy()
        return mdfa

    # Note: You do not need to touch this function, but may, and may find it useful for
    # generating visualizations of the NFA/DFA for understanding and debugging purposes
    def generateSVG(self,file_name="nfa",title=True):
        """Writes the current NFA to a dot file and runs graphviz (must be locally installed!)"""

        # Setup
        dot = Digraph(name='nfa',comment='nfa')
        dot.attr(rankdir='LR')
        names = {}
        if title == True:
            dot.node("regex",label='<<FONT POINT-SIZE="24">'+str(self.r)+'</FONT>>', shape="square", style="rounded", height="0", width="0", margin="0.05")
        elif isinstance(title,str):
            dot.node("regex",label='<<FONT POINT-SIZE="24">'+title+'</FONT>>', shape="square", style="rounded", height="0", width="0", margin="0.05")
        dot.node("*", style="invis", height="0", width="0", margin="0")

        def pad_lab(s):
            """For some reason graphviz needs spaces padding this to render right."""
            return "  "+s+"  "
        def str_lab(s):
            if s == "": return "ε"
            else: return str(s)

        # Nodes and Edges
        def namer(n): return "<q<sub><font point-size=\"11\">"+n+"</font></sub>>"
        if self.s in self.F:
            dot.node(str(len(names)),namer(str(len(names))), shape="doublecircle")
        else:
            dot.node(str(len(names)),namer(str(len(names))), shape="circle")
        names[self.s] = len(names)
        for n in (self.Q - self.F - {self.s}):
            dot.node(str(len(names)),namer(str(len(names))), shape="circle")
            names[n] = len(names)
        for n in (self.F - {self.s}):
            dot.node(str(len(names)),namer(str(len(names))), shape="doublecircle")
            names[n] = len(names)
        pseudodelta = dict()
        for e in self.delta:
            if (e[0],e[2]) in pseudodelta:
                pseudodelta[(e[0],e[2])] |= frozenset({e[1]})
            else:
                pseudodelta[(e[0],e[2])] = frozenset({e[1]})
        for k in pseudodelta.keys():
            dot.edge(str(names[k[0]]), str(names[k[1]]), label=pad_lab(
                ",".join(list(map(str_lab,sorted(list(pseudodelta[k])))))))
        dot.edge("*", str(names[self.s]), label="")

        dot.format = 'svg'
        dot.render(filename=file_name, cleanup=True)
