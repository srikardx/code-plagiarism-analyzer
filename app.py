from analyzer import calculate_similarity

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    file1 = read_file("samples/file1.py")
    file2 = read_file("samples/file2.py")

    score = calculate_similarity(file1, file2)

    print(f"Similarity Score: {score}%")

    if score > 50:
        print("⚠️ High chance of plagiarism")
    else:
        print("✅ Code appears original")




