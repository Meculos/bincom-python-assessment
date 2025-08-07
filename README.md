# Bincom ICT Python Developer Assessment

This project is a solution to the Bincom ICT Developer Assessment. It analyzes color data from an HTML page, performs statistical computations, saves results to a PostgreSQL database, and includes additional Python programming challenges.

---

## Requirements

- Python 3.6+
- PostgreSQL
- pip (Python package installer)

---

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/bincom-python-assessment.git
cd bincom-python-assessment
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate # mac
venv\scripts\activate # windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Create a .env file in the root directory**

Add your PostgreSQL configuration:

```env
DB_NAME=''
DB_USER=''
DB_PASSWORD=''
DB_HOST='localhost'
DB_PORT=5432
```
5. **Run the assessment script**

Ensure Postgres is running then run:

```bash
python assessment.py
```

**File Structure**
```bash
.
├── assessment.py
├── bincom_colors.html
├── .env
├── requirements.txt
└── README.md
```

**Note**
Make sure PostgreSQL is running before executing the script.

