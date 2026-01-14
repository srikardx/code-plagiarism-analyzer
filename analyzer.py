from utils.tokenizer import tokenize

def calculate_similarity(code1, code2):
    tokens1 = tokenize(code1)
    tokens2 = tokenize(code2)

    if not tokens1 or not tokens2:
        return 0.0

    intersection = tokens1.intersection(tokens2)
    union = tokens1.union(tokens2)

    similarity = len(intersection) / len(union)
    return round(similarity * 100, 2)
