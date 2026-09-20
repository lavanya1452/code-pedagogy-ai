# ⚡ AI Code Review Assistant

An AI-powered pedagogical static code analysis and refactoring engine built with **Streamlit** and powered by open-source Large Language Models via the **Hugging Face Inference API** (`Qwen/Qwen2.5-Coder-32B-Instruct`).

Designed to assist computer science students and developer teams by providing targeted, read-only feedback on time complexity, memory footprint, readability, and software engineering best practices.

---

## 🌟 Key Features

* **Targeted Dynamic Analysis:** Modular inspection parameters allowing users to isolate evaluations for:
  * ⏱️ **Time Complexity:** Algorithmic runtime bottleneck identification (Big-O analysis).
  * 🧠 **Memory Usage:** In-place comparisons, pointer optimizations, and heap space allocation checks.
  * 🧹 **Readability & Clean Code:** Refactoring for idiomatic naming conventions, PEP 8 compliance, and code hygiene.
  * 📋 **General Review:** Comprehensive static analysis and architectural feedback.
* **Open-Source LLM Integration:** Powered by `Qwen/Qwen2.5-Coder-32B-Instruct` hosted serverlessly via Hugging Face.
* **Modern Developer UI:** Responsive two-column dark-mode interface with custom CSS styling and real-time execution feedback.
* **Educational Guardrails:** Read-only suggestions structured to prevent auto-commit side effects and promote step-by-step learning.

---

## 🏗️ Architecture & Stack

* **Frontend / Framework:** Streamlit
* **AI Client Library:** `huggingface_hub` (`InferenceClient`)
* **Model Endpoint:** `Qwen/Qwen2.5-Coder-32B-Instruct`
* **Language Support:** Python, Java, C++, JavaScript, SQL, C#

---

## 🚀 Quickstart Guide

### Prerequisites

* Python 3.10+
* A free Hugging Face User Access Token (`hf_...`) from [Hugging Face Tokens](https://huggingface.co/settings/tokens)

### Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/lavanya1452/ai-code-review-assistant.git](https://github.com/lavanya1452/ai-code-review-assistant.git)
   cd ai-code-review-assistant
