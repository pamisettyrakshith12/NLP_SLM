# 🌐 English to Telugu Glossary Translator

An NLP-based application that extracts domain-specific glossary terms from an English PDF and translates them into Telugu using a Small Language Model (SLM).

## 📌 Project Overview

The system accepts an English glossary PDF as input, extracts the glossary terms and definitions, and translates them from English to Telugu.

The application uses a Small Language Model for machine translation and provides an interactive Streamlit web interface.

## ✨ Features

- 📄 Upload English glossary PDF
- 🔍 Extract glossary terms and definitions
- 🧠 Small Language Model based translation
- 🇬🇧 English → 🇮🇳 Telugu translation
- 📚 Domain-specific glossary support
- 📊 Display English and Telugu results
- ⬇️ Download translated glossary as CSV
- 🖥️ Simple and interactive Streamlit UI

## 🏗️ System Architecture

```text
English Glossary PDF
        ↓
   PDF Text Extraction
        ↓
   Glossary Term Extraction
        ↓
    Small Language Model
        ↓
 English → Telugu Translation
        ↓
   Streamlit Web Interface
        ↓
   Telugu Glossary / CSV