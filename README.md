                                KAKEIBO (家計簿)

A minimal, self-hosted expense tracker.

Kakeibo (家計簿) is a Japanese word meaning:

> 家 (ka) — home  
> 計 (kei) — to measure / calculate  
> 簿 (bo) — ledger / book  

Together: **“household financial ledger.”**

This project is a digital implementation of that concept:
quiet, intentional, without noise or distraction.

No cloud.  
No ads.  
No analytics.  
Just clarity.

________________

Purpose

Most modern finance trackers store personal data in their cloud
and use it to analyze spending behavior.

This project exists for the opposite reason:

> I want full control of my financial data.  
> Local-first. Self-hosted. Private.

The goal is not to become a product with a hundred features.
The goal is to remain a 'clear tool that improves only when needed'.

Little About - [ABOUT.md](assets/ABOUT.md)
________________

Core principles
◎ Clarity over complexit  
◇ One screen. One form. One table.

◎ Local-firt  
◇ All data stored in SQLite (later Postgres).  
◇ No external services.

◎ Iterative developmen*  
◇ Build → use → improve.  
◇ README will change along with the code.

________________

Current functionality (MVP v0.1)

-  Add expense or income through HTML form
-  Store data in SQLite using SQLAlchemy
-  Display last 50 transactions
-  Show basic totals (income / expense)
-  Configurable via .env (ignored by git)

________________

Structure:

```
kakeibo_public/                     ← Git repository (this goes to GitHub)
│
├── app.py                          ← Flask entrypoint
├── database.py                     ← DB engine + session + init
├── models.py                       ← SQLAlchemy models
│
├── templates/
│   └── index.html                  ← UI (form + table)
│
├── requirements.txt
├── README.md
├── ABOUT.md
├── .env.example                    ← template (no secrets)
├── .gitignore
│
└── data/                           ← SQLite DB runtime folder (ignored by git)
    └── (empty)
```
________________


Run locally:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python app.py

Open:

http://localhost:5000
```
________________

License

This project is released under AGPL-3.0.

It remains open-source,
but modified versions deployed as a service must also remain open-source.

________________

Status

- Actively developed.
- Actively used.
- README evolves with the project.

<>Kakeibo is a tool, not a product.
Simplicity is the feature.<>

「家計簿」 — track with intention.

![Kakeibo](assets/kakeibo.png)
