# 🤖 AI-Stack

Welcome to the **AI-Stack** repository! This is the central hub for building, training, evaluating, and integrating cutting-edge AI models within the Doubtroom ecosystem. Whether you're a new contributor or a seasoned AI developer, this guide will walk you through setting up your environment, contributing to the codebase, and understanding the project structure.

---

## 📝 Table of Contents

- 📦 [Prerequisites](#-prerequisites)
- 🚀 [Project Setup Instructions](#-project-setup-instructions)
- 🔧 [Setting Up Your Local Repo](#-setting-up-your-local-repo)
- 📂 [Working on Your Changes](#-working-on-your-changes)
- ✅ [Committing & Pushing](#-committing--pushing)
- 📬 [Creating a Pull Request](#-creating-a-pull-request)
- 📌 [Rules for All Contributors](#-rules-for-all-contributors)
- 📁 [Project Structure](#-project-structure)
- 📚 [MongoDB Integration Guide](#-mongodb-integration-guide)

---

## 📦 Prerequisites

Ensure you have the following installed:

- Git: [Download Git](https://git-scm.com/)
- Python 3.8+
- `pip` or `conda` for managing dependencies
- GitHub account

💡 *Optional but recommended: Create a virtual environment*

**Using `venv`:**
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```


Using conda:
```bash
conda create --name ai-env python=3.10
conda activate ai-env
```

🚀 Project Setup Instructions

Fork the Repository

Go to: https://github.com/Doubtroom/AI-Stack.git
Click Fork (top-right corner)

Clone the Forked Repository

```bash
git clone https://github.com/your-username/AI-Stack.git
cd AI-Stack

``` 
Install Dependencies
```bash
pip install -r requirements.txt
```
🔧 Setting Up Your Local Repo
Add the Upstream Repository


```bash
git remote add upstream https://github.com/Doubtroom/AI-Stack.git
```
Sync with Latest Code

```bash
git checkout main
git pull upstream main

```

Create a Feature Branch

```bash
git checkout -b <feature-name>
```


📂 Working on Your Changes

Branch Naming Convention


| Purpose   | Pattern             | Example                   |
|-----------|---------------------|---------------------------|
| Data      | `data/<description>`  | `data/data-ingestion`     |
| Pipeline  | `pipeline/<desc>`     | `pipeline/fortextextrct`  |
| Model     | `model/<desc>`        | `model/ocrmodel`          |
| Fix       | `fix/<desc>`          | `fix/dataingestionpipe`   |
| Chore     | `chore/<task>`        | `chore/update-dependencies` |
| Refactor  | `refactor/<desc>`     | `refactor/ingestionproc`  |
| Template  | `template/<usecase>`  | `template/forapp`         |
| Docs      | `docs/<desc>`         | `docs/llmreadme`          |

✅ Committing & Pushing
Stage and Commit Changes


```bash
git add .
git commit -m "✨ Added <your feature or fix summary>"
```
Push to Your Branch


```bash
git push origin <feature-name>
```
❗ Never push directly to main.


📬 Creating a Pull Request
Go to your forked repo on GitHub

Click Compare & pull request

Fill in a descriptive title and explanation

Submit the PR

Once reviewed, changes will be suggested or merged.

📌 Rules for All Contributors
🚫 Do NOT push to main directly

🔁 Always pull from main before creating a PR

✅ Keep commits small, atomic, and meaningful

🧠 Use descriptive commit messages (type: description)

👀 Review your changes before committing

📁 Project Structure

AI-Stack/
├── src/                 
│   ├── data/             
│   ├── models/           
│   ├── pipelines/        
│   ├── prompts/          
│   ├── utils/          
│   ├── log.py            
│   └── exception.py      
│
├── configs/             
│   ├── model/            
│   ├── training/         
│   └── evaluation/       
│
├── artifacts/           
│   ├── models/           
│   ├── tokenizer/        
│   └── results/          
│
├── templates/            # Web Dev Team Only
│   ├── system/           
│   ├── user/             
│   └── eval/             
│
├── notebooks/           
│   ├── data-analysis.ipynb     
│   ├── model-eval.ipynb        
│   └── experiment-001.ipynb    
│
├── experiments/         
│   ├── exp001/           
│   └── exp002/           
│
├── integrations/        
│   ├── api/              
│   ├── langchain/        
│   └── openai/           
│
├── tests/               
├── requirements.txt     
├── .env.example         
├── README.md            
└── setup.py             
📚 MongoDB Integration Guide
Fetching Data Using PyMongo

🧰 Prerequisites
Install the required library:



pip install pymongo
🔌 Connect to MongoDB
python
```bash
import pymongo

# Replace <your-connection-string> with actual URI
client = pymongo.MongoClient('<your-mongo-uri>')

# Connect to the database
db = client['<database-name>']

# Connect to collections
users = db['users']
questions = db['questions']

# Example query
for user in users.find():
    print(user)

```
If you have any confusion or questions, feel free to reach out to the team on Slack or Discord. Happy Contributing! 💙

Maintained by the AI Team @ Doubtroom
GitHub: https://github.com/Doubtroom