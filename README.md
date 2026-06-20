A little project to explore ERP concepts.

## Setup Instructions

### 1. Clone repository

```bash
git clone https://github.com/collinshields/Storystock.git
cd Storystock/backend
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

### 3. Activate Environment

#### Windows Powershell

```Bash
.venv\Scripts\Activate
```

### 4. Install Dependencies

```Bash
pip install -r requirements.txt
```

## 5. Run the application

```Bash
uvicorn app.main:app --reload
```
