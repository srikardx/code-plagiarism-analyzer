# Code Plagiarism Analyzer

A powerful tool to automatically detect plagiarism in programming assignments using token analysis and similarity comparison.

## 🔍 Problem Statement
Manually detecting code plagiarism is time-consuming and error-prone, especially when students rename variables or change formatting.

## 💡 Solution
This system tokenizes source code, normalizes it, and uses similarity metrics to flag potential plagiarism cases.

## ✨ Features
- Token-based analysis (ignores variable names & formatting)
- Supports multiple programming languages
- Percentage-based similarity score
- Simple CLI interface
- Great for educators and teaching assistants

## ⚙️ How It Works
1. Load student code files
2. Remove comments and whitespace
3. Tokenize code structure
4. Calculate Jaccard / Cosine similarity
5. Generate detailed reports

## 🚀 How to Run
```bash
git clone https://github.com/srikardx/code-plagiarism-analyzer.git
cd code-plagiarism-analyzer
pip install -r requirements.txt
python app.py
```

## 📊 Example Output
```
Similarity between file1.py and file2.py: 87% → HIGH PLAGIARISM RISK
```

---

Made with ❤️ by [Srikar Reddy](https://github.com/srikardx)
