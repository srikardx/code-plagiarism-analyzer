import re

def tokenize(code):
    # remove single-line comments
    code = re.sub(r"#.*", "", code)

    # normalize whitespace
    code = re.sub(r"\s+", " ", code)

    # extract identifiers, keywords, numbers
    tokens = re.findall(r"[A-Za-z_]+|\d+", code)

    return set(tokens)
