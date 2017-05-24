from metakernel import MetaKernel
from calysto_prolog import prolog
import sys, copy, re

class PrologKernel(MetaKernel):
    implementation = 'Prolog'
    implementation_version = '1.0'
    language = 'prolog'
    language_version = '0.1'
    banner = "Prolog kernel - evaluates Prolog programs"
    search = None
    language_info = {
        'mimetype': 'text/x-prolog',
        'name': 'prolog',
        'codemirror_mode': {'name': 'prolog'},
        'pygments_lexer': 'prolog',
    }

    kernel_json = {
        "argv": [sys.executable, 
                 "-m", "calysto_prolog", 
                 "-f", "{connection_file}"],
        "display_name": "Calysto Prolog",
        "language": "prolog",
        "codemirror_mode": "prolog",
        "name": "calysto_prolog"
    }
    magic_prefixes = dict(magic='%', shell='!', help='?')
    help_suffix = None

    def get_usage(self):
        return """This is the Prolog kernel.

Example Rules:
    child(stephanie).
    child(thad).
    mother_child(trude, sally).
 
    father_child(tom, sally).
    father_child(tom, erica).
    father_child(mike, tom).
 
    sibling(X, Y)      :- parent_child(Z, X), parent_child(Z, Y).
 
    parent_child(X, Y) :- father_child(X, Y).
    parent_child(X, Y) :- mother_child(X, Y).

Example Queries:
    child(NAME)?
    sibling(sally, erica)?
    father_child(Father, Child)?
"""

    def do_execute_direct(self, code):
        prolog.print_function = self.Print
        result = None
        for line in code.strip().split("\n"):
            if line:
                result = self.do_execute_line(line.strip())
        return result

    def do_execute_line(self, sent):
        s = re.sub("#.*", "", sent) # clip comments
        s = re.sub(" is ", "*is*", s)    # protect "is" operator
        s = re.sub(" ",  "", s)           # remove spaces
        if s == "" : 
            return

        if s[-1] in '?.' : 
            punc=s[-1]; s=s[:-1]
        else             : 
            punc='.'

        if   s == '%untrace' : prolog.trace = 0
        elif s == '%trace' : prolog.trace = 1
        elif s == '%dump'  :
            self.Print("Database rules:")
            for rule in prolog.rules : 
                self.Print("    " + str(rule))
        elif s in ["%cont", "%continue"]:
            return self.continue_search()
        elif punc == '?' : 
            try:
                self.search = prolog.search(prolog.Term(s))
                return self.continue_search()
            except:
                self.Error("Unable to process query. Please restate.")
        else             : 
            try:
                prolog.rules.append(prolog.Rule(s))
                self.Print("Rule added to database.")
            except:
                self.Error("Unable to process statement. Please restate.")

    def continue_search(self):
        if self.search:
            try:
                result = next(self.search)
                if result:
                    self.Print("Use '%continue' for more results.")
            except StopIteration:
                result = None
                self.Print("No more results.")
            return result
        else:
            self.Error("Ask a question first.")

    def get_completions(self, info):
        token = info["help_obj"]
        keywords = ["%cont", "%continue", "%dump", "is", "%untrace", "%trace", "cut", "fail"]
        return [word for word in keywords if word.startswith(token)]

    def get_kernel_help_on(self, info, level=0, none_on_fail=False):
        expr = info["code"]
        if none_on_fail:
            return None
        else:
            return "Sorry, no available help for '%s'" % expr
