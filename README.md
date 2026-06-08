# ai-test-automation-demo
Public demo repository for an AI-assisted deterministic test automation pipeline.

by Jeff Goode

## 📐 CRISP‑DM Framework Alignment

This project follows the CRISP‑DM methodology to structure the transformation of natural‑language test cases into deterministic, executable UI tests. Although the system is not a traditional ML model, the pipeline maps cleanly onto CRISP‑DM because it processes unstructured input, transforms it into structured representations, and evaluates outcomes through execution artifacts.

---

### **1. Business Understanding**

Modern UI test automation is slow, brittle, and expensive. Teams spend significant time writing tests, maintaining selectors, and diagnosing failures.

**Business Objective:**  
Reduce the cost and effort of UI test automation by automatically converting natural‑language test cases into stable, executable tests with deterministic behavior.

**Guiding Question:**  
**How can we automatically transform natural‑language test cases into reliable UI tests that reduce manual QA effort and improve test stability?**

---

### **2. Data Understanding**

In real software teams, the “data” that drives test automation does not begin as structured test steps. It begins as **human‑authored intent**, typically expressed in several layers:

- **User stories** — high‑level descriptions of user goals  
- **Acceptance criteria** — conditions that define “done”  
- **Manual test cases** — step‑by‑step instructions written by QA  
- **Natural‑language test steps** — the final form before automation  

These inputs are unstructured, inconsistent, and vary widely in style and detail.  
The goal of this project is to transform these human‑authored artifacts into structured representations that can be executed deterministically.

The system therefore works with several forms of “data”:

- **User stories and acceptance criteria** (initial product intent)  
- **Natural‑language test cases** (QA intent)  
- **Intermediate Representations (IR)** describing structured test steps  
- **UI model and selector mappings** (application structure and stable targets)  
- **Execution artifacts** (logs, traces, screenshots)  
- **Failure patterns** (signals used for analysis and classification)

This combination of unstructured and structured data forms the foundation of the automation pipeline.


### **3. Data Preparation**

Data preparation corresponds to structuring and normalizing the inputs:

- Parsing natural‑language test cases into IR  
- Normalizing actions and targets  
- Resolving logical targets into selectors via the mapping layer  
- Validating IR against the app model  

This phase ensures that downstream code generation is deterministic and stable.

---

### **4. Modeling**

In this project, “modeling” refers to building the compiler‑style pipeline that transforms structured IR into executable test code:

- IR → deterministic Python/Selenium/Playwright code  
- Selector resolution strategies  
- Stable action sequencing  
- Deterministic test generation  

This phase defines how the system behaves when converting structured intent into executable automation.

---

### **5. Evaluation**

Evaluation occurs through test execution and artifact analysis:

- Running generated tests  
- Capturing logs, traces, and screenshots  
- Detecting failures  
- Classifying failure types  
- Assessing selector stability and determinism  

This phase validates whether the generated tests behave reliably in real execution environments.

---

### **6. Deployment**

Deployment focuses on integrating the pipeline into real workflows:

- Running multiple test cases in batch  
- Integrating with CI/CD  
- Versioning IR, mappings, and selectors  
- Producing structured reports for engineering teams  
- Scaling the pipeline to larger test suites  

This phase ensures the system can operate as part of a production automation strategy.

---

### **Summary**

By aligning the project with CRISP‑DM, the pipeline becomes a clear, structured, and repeatable process:

**Natural‑language → IR → Mapping → Code → Execution → Artifacts → Analysis**

This framing makes the project easier to understand, maintain, and extend — and positions it as a serious, architecture‑driven automation system.

# **AI Test Automation Demo**  
*A public demonstration of a deterministic, AI‑assisted test automation pipeline.*

This repository showcases the **public-facing components** of a system designed to transform messy user stories and manual test cases into **structured, repeatable, automated tests**.

It includes:

- a small **testbed web application**  
- **sample user stories** and **test cases**  
- a clean **Intermediate Representation (IR)** format  
- **notebooks** demonstrating parsing, code generation, and execution  
- **example generated tests**  
- **artifacts** from real test runs  
- documentation explaining the architecture and design philosophy  

This repo is intentionally **demo‑only**.  
The private core engine — IR parser, mapping logic, code generation templates, and feedback loop — lives in a separate private repository.

---

## **🎯 Why This Project Exists**

Modern software teams face the same problems:

- brittle UI tests  
- flaky selectors  
- inconsistent manual test cases  
- unclear user stories  
- slow regression cycles  
- expensive QA maintenance  

Many companies have tried “AI agents that write tests,” but these systems fail because they lack:

- structure  
- determinism  
- repeatability  
- separation of concerns  
- a stable mapping between test logic and UI elements  

This project demonstrates a different approach:

> **AI as a compiler front‑end, not an autonomous agent.**  
>  
> Natural language → structured IR → deterministic code generation → stable automated tests.

---

## **🧩 Architecture Overview**

The full system (private repo) consists of five major components:

1. **Input Parsing**  
   Converts user stories and manual test cases into a structured IR.

2. **Intermediate Representation (IR)**  
   A strict schema describing actions, targets, assertions, and metadata.

3. **Application Model Mapping**  
   Maps logical targets (e.g., `login_button`) to real selectors.

4. **Deterministic Code Generation**  
   Template‑driven generation of Playwright/Pytest tests.

5. **Execution + Feedback Loop**  
   Runs tests, captures artifacts, classifies failures, and suggests fixes.

This public repo demonstrates the **concepts**, **workflow**, and **outputs** without exposing proprietary engine code.

See `docs/architecture-overview.md` for details.

---

## **📦 Repository Structure**

```
ai-test-automation-demo/
│
├── docs/                     # Architecture, IR explanation, diagrams
├── notebooks/                # Parsing, IR, codegen, execution demos
├── app-under-test/           # Small demo web app (frontend + backend)
├── sample-data/              # User stories, test cases, IR examples
├── generated-tests-demo/     # Example generated pytest files
├── artifacts-demo/           # Screenshots, logs, traces from test runs
├── README.md                 # You are here
└── requirements.txt
```

Each folder is designed to illustrate a piece of the pipeline.

---

## **📘 What This Demo Shows**

### **1. Parsing messy test cases into IR**  
See `notebooks/01_parse_test_case_to_IR.ipynb`.

### **2. Visualizing and validating IR**  
See `notebooks/02_visualize_IR.ipynb`.

### **3. Generating deterministic test code**  
See `notebooks/03_generate_test_code.ipynb`.

### **4. Running tests against the testbed app**  
See `notebooks/04_run_tests_and_collect_artifacts.ipynb`.

### **5. Analyzing failures**  
See `notebooks/05_failure_analysis_demo.ipynb`.

---

## **🧪 Testbed Web Application**

The `app-under-test/` folder contains a small demo application with:

- login flow  
- CRUD operations  
- dynamic elements  
- intentionally flaky components  

This environment allows you to demonstrate:

- selector drift  
- timing issues  
- ambiguous test steps  
- regression behavior  

It’s a safe sandbox for showcasing the pipeline.

---

## **🛠️ Example Generated Tests**

The `generated-tests-demo/` folder contains sample pytest files produced by the pipeline.

These illustrate:

- deterministic structure  
- stable selectors  
- clean, readable code  
- repeatable execution  

They are intentionally simple — the private repo contains the full engine.

---

## **📊 Artifacts From Test Runs**

The `artifacts-demo/` folder includes:

- screenshots  
- logs  
- traces  

These demonstrate how the execution harness captures evidence for debugging and analysis.

---

## **🔒 What’s Not Included Here**

This public repo does **not** include:

- IR parser implementation  
- mapping logic  
- selector resolution  
- code generation templates  
- feedback loop logic  
- Jira/Confluence integration  
- LLM prompt templates  
- execution harness internals  

These live in a private repository as part of a consulting offering and future product direction.

---

## **💼 Consulting & Professional Use**

This project is part of a broader initiative to help engineering teams:

- modernize QA  
- reduce flaky tests  
- accelerate regression cycles  
- integrate AI safely and deterministically  
- improve test coverage  
- standardize test case structure  

If your organization is exploring AI‑assisted test automation, this demo illustrates the architectural approach that avoids the brittleness of agent‑based systems.

---

## **📬 Contact**

For consulting inquiries, architecture reviews, or integration discussions, please reach out via
[LinkedIn](https://www.linkedin.com/in/jeffreylgoode)

---

