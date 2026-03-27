# Python Beginner + Backend Starter

This project is made for beginners.

It has:
- `basics/` for Python fundamentals.
- `backend/` for a simple API using FastAPI.

## 1) Setup (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If `python` does not work, try:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 2) Run Python Basics

Run each file one by one:

```powershell
python basics\01_variables_and_types.py
python basics\02_conditions_and_loops.py
python basics\03_functions.py
python basics\04_lists_and_dicts.py
```

## 3) Run Backend Server

```powershell
uvicorn backend.main:app --reload
```

Then open:
- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/health`
- `http://127.0.0.1:8000/items`
- `http://127.0.0.1:8000/docs` (interactive API docs)

## 4) Test POST API in Swagger Docs

1. Open `http://127.0.0.1:8000/docs`
2. Find `POST /items`
3. Click **Try it out**
4. Send:

```json
{
  "name": "Notebook",
  "price": 5.5
}
```

## 5) Next Learning Steps

After this, learn in this order:
1. Functions and return values
2. File handling (`open`, read, write)
3. Classes and OOP
4. FastAPI path/query parameters
5. Database basics (SQLite + SQLAlchemy)

## 6) Day-By-Day Track (Beginner Friendly)

Open:
- `LEARNING_PLAN.md`

Start Week 1 practice:

```powershell
python practice\week1\day01_variables_input.py
```

Check your answer:

```powershell
python practice\week1\solutions\day01_variables_input_solution.py
```
