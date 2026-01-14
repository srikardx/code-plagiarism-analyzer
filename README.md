# Code Plagiarism Analyzer

A system that detects code plagiarism in programming assignments using token-based analysis and similarity comparison techniques.

## 🔍 Problem Statement
Plagiarism in programming assignments is difficult to detect manually, especially when variable names or formatting are changed. This project aims to automatically identify similarity between code files.

## 💡 Solution
The system tokenizes source code, removes comments and formatting differences, and calculates similarity using set-based comparison logic to produce a plagiarism score.

## ✨ Features
- Token-based code comparison
- Language-independent logic
- Percentage similarity score
- Simple and lightweight design
- Useful for colleges and instructors

## ⚙️ How It Works
1. Reads source code files
2. Removes comments and extra whitespace
3. Tokenizes identifiers and keywords
4. Computes similarity using Jaccard similarity
5. Flags high-plagiarism cases

## 🚀 How to Run
```bash
python app.py
