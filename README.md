# AI Test Automation Demo
A minimal demonstration of why LLM‑only test generation is brittle — and how a simple IR‑driven pipeline fixes it.

---

## CRISP‑DM Framing

### 1. Business Understanding
Modern UI test automation is slow, brittle, and expensive to maintain.  
Teams increasingly attempt to use LLMs to generate Playwright or Selenium tests directly from manual test cases — but these tests often fail due to hallucinated selectors, inconsistent structure, and nondeterministic output.

### Business Problem
**How can we reduce brittleness in AI‑generated UI tests so they become stable, repeatable, and maintainable?**

### Business Objective
Demonstrate, with a minimal reproducible example, that introducing a small amount of structure — an Intermediate Representation (IR) and a selector‑mapping layer — dramatically improves reliability compared to LLM‑only test generation.

### 2. Data Understanding
The “data” in this project is a natural‑language test case describing a simple login flow.  
This NL input is intentionally ambiguous and incomplete, mirroring real‑world manual test scripts.

### 3. Data Preparation
The NL test case is parsed into:
- raw steps  
- interpreted actions  
- logical selectors  
- structured IR fields  

This preparation step is what enables deterministic code generation.

### 4. Modeling
Two contrasting models are demonstrated:

- **Deterministic Model:**  
  NL → IR → Selector Mapping → Template‑Driven Codegen → Playwright Test

- **LLM‑Only Model:**  
  NL → LLM → Direct Code Generation (hallucinated selectors)

### 5. Evaluation
Success is measured by execution stability:
- The deterministic pipeline produces a **passing** Playwright test.  
- The LLM‑only pipeline produces a **failing** test due to incorrect selectors.

### 6. Deployment
The project is packaged as a simple GitHub demo showing both pipelines side‑by‑side, enabling teams to understand the architectural difference and why IR‑driven automation scales while LLM‑only approaches do not.

---

## Overview

This project demonstrates three contrasting pipelines:

1. **Deterministic Pipeline (Passes)**  
   Natural‑language → IR → Selector Mapping → Deterministic Codegen → Playwright → Pass

2. **LLM‑Simulator Pipeline (Fails)**  
   Natural‑language → LLM‑style hallucinations → Wrong selectors → Playwright → Fail

3. **Real LLM Output Pipeline (Sometimes Passes, Sometimes Fails)**  
   Natural‑language → ChatGPT/Gemini/Claude/Groq → Raw Playwright → Unpredictable outcome

Together, these pipelines illustrate why structure matters in AI‑assisted test automation.

---

## Why This Exists

LLM‑generated UI tests fail because LLMs:

- hallucinate selectors  
- guess at application structure  
- produce inconsistent code  
- cannot reason about state  
- cannot guarantee determinism  

A small amount of structure — IR + selector mapping — eliminates brittleness.

---

## What This Demo Contains

### Tiny Testbed App
A simple login page with stable selectors.

### Natural‑Language Test Case
Goal: Verify user can log in

Steps:
- Navigate to /login  
- Enter username "demo"  
- Enter password "password123"  
- Click login button  
- Verify dashboard_heading visible  

### Deterministic Pipeline (Passes)
- Parse NL  
- Interpret into IR  
- Map logical selectors → real CSS selectors  
- Generate Playwright code  
- Execute and collect artifacts  

### LLM‑Only Pipeline (Fails)
- Feed the same NL test case to an LLM  
- Save the generated Playwright code  
- Run it  
- Test fails due to hallucinated selectors  

---

## Repository Structure

```plaintext
```plaintext
ai-test-automation-demo/
│
├── app-under-test/                 # legacy tiny login page
│
├── artifacts/                      # execution artifacts (collapsed)
│   ├── flask_app_run/              # multiple timestamped runs
│   └── todomvc_run/
│
├── artifacts-demo/
│   └── test_login_valid_credentials/
│
├── demo-app/                       # Flask app deployed on Render
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       ├── dashboard.html
│       ├── index.html
│       └── login.html
│
├── docs/                           # documentation (WIP)
│
├── generated-tests/                # deterministic + LLM-generated tests
│   ├── *_test.py
│   └── todomvc_*.py
│
├── generated-tests-demo/
│   └── test_login_valid_credentials.py
│
├── LICENSE
│
├── notebooks/
│   ├── ai_test_automation_demo.ipynb     # main demo notebook
│   ├── generated_brittle_test.py
│   ├── generated_test_login.py
│   ├── pipeline_test_login.py
│   ├── pipeline_test_login_llm_brittle.py
│   ├── pipeline_test_login_llm_real.py
│   ├── archived/                          # older pipeline notebooks
│   │   ├── 01 - NL_to_IR.ipynb
│   │   ├── 02 - IR Visualization.ipynb
│   │   ├── 03 - Mapping Layer.ipynb
│   │   ├── 04 - Playwright Code Generation.ipynb
│   │   ├── 05 - Playwright Execution.ipynb
│   │   ├── 06 - Artifact Analysis.ipynb
│   │   ├── Full_Batch_Pipeline.ipynb
│   │   └── Simple batch file.ipynb
│   └── artifacts/
│       ├── brittle/
│       ├── good/
│       └── real_llm/
│
├── README.md
├── render.yaml
│
└── sample-data/
    ├── ir_examples/                 # IR outputs (unmapped + mapped)
    ├── ir_examples_mapped/
    ├── mapping_output/
    │   └── login_mapping.json
    └── test_cases/
        ├── test_dashboard_navigation.txt
        ├── test_home_page.txt
        ├── test_login_brittle_llm.txt
        ├── test_login_failure.txt
        ├── test_login_success.txt
        └── test_logout_flow.txt

```
## How the LLM‑Only Pipeline Fails

1. **Feed the same NL test case into an LLM**  
2. **Ask it to generate Playwright code**  
3. **The LLM confidently outputs selectors like:**  
   - `#username-input`  
   - `#password-field`  
   - `button[type=submit]`  
4. **These selectors do not exist in the app**  
5. **The test fails immediately**  

This failure is intentional — it demonstrates brittleness.

## What This Demo Proves

- LLMs understand **intent**, but guess **selectors**  
- Deterministic pipelines eliminate brittleness  
- IR + mapping = stable, repeatable tests  
- AI should assist, not autonomously generate automation  

This is the architectural pattern that scales.


## 🧩 Natural Language → IR → Playwright: Why Determinism Wins

This project demonstrates three different approaches to generating Playwright tests from natural‑language instructions. Each approach highlights a different part of the reliability spectrum — from fully deterministic to fully stochastic — and shows why a structured NL → IR → Code pipeline is essential for stable test automation.

---

## 🚀 1. Deterministic Pipeline (Always Passes)

The deterministic pipeline converts natural‑language test cases into a structured **Intermediate Representation (IR)**.  
From that IR, selectors and actions are generated deterministically, producing Playwright code that:

- Uses **correct selectors**
- Follows **correct navigation flows**
- Handles **wait conditions predictably**
- **Always passes** as long as the application behaves correctly

This pipeline is the backbone of the project and demonstrates how NL → IR → Code avoids the brittleness of direct LLM‑to‑code generation.

---

## 🧪 2. LLM‑Simulator Pipeline (Always Fails)

To illustrate how LLMs typically behave when asked to generate UI automation code, the project includes an **LLM simulator** that intentionally produces:

- Hallucinated selectors  
- Incorrect button names  
- Wrong heading IDs  
- Misaligned flows  
- Missing waits  

This pipeline is expected to **fail every time**, and it does so in a controlled, reproducible way.  
It’s a safe, offline demonstration of the brittleness inherent in unconstrained LLM‑generated test code.

---

## 🤖 3. Real LLM Output Pipeline (Sometimes Passes, Sometimes Fails)

In this pipeline, the user copies natural‑language test steps into a real GenAI model (ChatGPT, Gemini, Claude, Groq, etc.) and pastes the generated Playwright code back into the notebook.

This produces the most important insight of the entire project:

### LLM‑generated Playwright code is **unpredictable**.

- Sometimes the LLM guesses selectors correctly → **the test passes**
- Sometimes it guesses wrong → **the test fails**
- Sometimes it uses unsupported APIs → **the test errors**
- Sometimes it mixes frameworks (pytest‑playwright vs raw Playwright)
- Sometimes it wraps code in `__main__` blocks or async functions

This variability is the core problem the deterministic pipeline solves.

---

## 🎯 Why This Matters

UI automation requires **precision**:

- Correct selectors  
- Correct flows  
- Correct waits  
- Correct browser lifecycle  
- Correct error handling  

LLMs are powerful, but they are **not deterministic**.  
They guess. They hallucinate. They vary from run to run.

This project shows:

> You cannot build reliable UI automation on top of guesswork.  
> Deterministic pipelines eliminate guesswork entirely.

---

## 🏁 Summary

This project demonstrates, with real code and real LLMs, that:

- Deterministic NL → IR → Code generation is **stable and reliable**  
- LLM‑simulated generation is **brittle and failure‑prone**  
- Real LLM generation is **unpredictable and inconsistent**  

Together, these pipelines make a compelling case for structured, deterministic automation systems — especially in environments where correctness and repeatability matter.

## The Real Solution: A Robust NL → IR Parser

The core lesson of this project is simple:

**The only reliable way to generate stable UI automation from natural‑language test cases is to introduce a deterministic NL → IR parsing layer.**

LLMs are excellent at interpreting *intent*, but they are unreliable at producing *execution‑ready selectors and actions*.  
A robust NL → IR parser solves this by enforcing structure:

1. **Humans write or review NL test cases**
2. **The NL → IR parser converts them into structured actions**
3. **Humans review and fix the IR when needed**
4. **Selector mapping + deterministic codegen produce stable Playwright tests**

This workflow mirrors how real QA teams operate:

- Humans provide domain knowledge  
- The parser enforces structure  
- The mapping layer ensures selector correctness  
- The codegen layer ensures consistency  
- The final output is deterministic and repeatable  

In other words:

> **LLMs help interpret intent, but humans validate structure.  
> Determinism handles execution.**

This hybrid approach — NL → IR → Code with human‑in‑the‑loop IR validation — is the scalable, production‑ready pattern for AI‑assisted test automation.

