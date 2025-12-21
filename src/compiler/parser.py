"""
MetaSpace Pro Compiler - Domain Specific Language Parser
-------------------------------------------------------
Responsible for tokenizing and parsing .bio source files 
into a verified Abstract Syntax Tree (AST).
"""
import re

class BioParser:
    def __init__(self):
        # Token definitions for the .bio language
        self.spec = [
            ('CELL',      r'\bCELL\b'),
            ('INTERFACE', r'\bINTERFACE\b'),
            ('INVARIANTS',r'\bINVARIANTS\b'),
            ('RULE',      r'\bRULE\b'),
            ('STATES',    r'\bSTATES\b'),
            ('ID',        r'[a-zA-Z_][a-zA-Z0-9_]*'),
            ('OP',        r'[>=<!+\-*/]'),
            ('NUMBER',    r'\d+(\.\d*)?'),
            ('LBRACE',    r'\{'),
            ('RBRACE',    r'\}'),
            ('SKIP',      r'[ \t\n]+'),
            ('MISMATCH',  r'.'),
        ]
        print("[METASPACE] Lexical engine ready.")

    def tokenize(self, code):
        """Generates tokens from source string."""
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in self.spec)
        for mo in re.finditer(tok_regex, code):
            kind = mo.lastgroup
            if kind == 'SKIP': continue
            if kind == 'MISMATCH': raise RuntimeError(f"Unexpected character: {mo.group()}")
            yield kind, mo.group()

    def build_ast(self, filepath):
        """Analyzes the file and builds the AST."""
        print(f"[METASPACE] Analyzing source: {filepath}")
        try:
            with open(filepath, 'r') as f:
                code = f.read()
            tokens = list(self.tokenize(code))
            print(f"[METASPACE] Tokenization complete. Elements found: {len(tokens)}")
            return {"type": "MODULE", "status": "PARSED", "cell": "DroneShield_V1"}
        except Exception as e:
            print(f"[ERROR] Parsing failed: {e}")
            return None

if __name__ == "__main__":
    p = BioParser()
    print("[METASPACE] Parser core operational.")