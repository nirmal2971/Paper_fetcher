# 📄 PubMed Paper Fetcher

A command-line Python tool to fetch research papers from [PubMed](https://pubmed.ncbi.nlm.nih.gov/) using a search query, and filter out papers that include authors affiliated with **pharmaceutical or biotech companies**. Useful for analyzing industry participation in research.

---

## ✨ Features

- 🔍 Search PubMed using advanced query syntax (e.g., `"cancer AND 2023[dp]"`)
- 🧪 Filters for **non-academic authors** using affiliation heuristics
- 🏢 Detects company-affiliated contributors
- 📧 Attempts to extract corresponding author emails
- 📦 Outputs results to console or CSV file
- ⚙️ Simple CLI built using Typer
- 🧪 Modular and extendable with Poetry

---

---

## 🚀 Installation

> 🔧 This project uses [Poetry](https://python-poetry.org/) for package and dependency management.

### 1. Clone the repository

```bash
git clone https://github.com/nirmal2971/Paper_fetcher.git
cd Paper_fetcher
