# Environment Variables and Configuration

## Why Do We Need This?

Imagine you're building an app that connects to a database. You might write:

```python
# BAD: Don't do this!
connection = connect_to_database(
    host="localhost",
    user="myuser", 
    password="supersecret123",
    database="myapp"
)
```

**Problems with this approach:**
1. **Security Risk**: Your password is visible in the code
2. **Hard to Change**: Need to modify code to change settings
3. **Different Environments**: Your local database is different from production
4. **Version Control**: You'll accidentally commit secrets to Git

**The solution:** Use environment variables and configuration files to keep secrets separate from code.

---

## Environment Variables

### What Are Environment Variables?

Environment variables are key-value pairs that exist in your operating system. They're like global variables that any program can access.

```bash
# Setting an environment variable (in terminal)
export DATABASE_URL="postgresql://user:pass@localhost/db"
export API_KEY="sk-1234567890abcdef"
```

### Reading Environment Variables in Python

```python
import os

# Method 1: os.environ (will raise KeyError if missing)
database_url = os.environ['DATABASE_URL']  # Crashes if not set

# Method 2: os.getenv() (safer, can provide default)
database_url = os.getenv('DATABASE_URL')  # Returns None if not set
api_key = os.getenv('API_KEY', 'default-key')  # Returns 'default-key' if not set
```

**Always prefer `os.getenv()`** because it won't crash your program if the variable is missing.


---

## Using .env Files

### The Problem with System Environment Variables

Setting environment variables in your terminal is annoying:
```bash
export DATABASE_URL="..."
export API_KEY="..."
export DEBUG="True"
python app.py  # Only works in this terminal session
```

### Solution: .env Files

Create a `.env` file in your project root:

```bash
# .env
DATABASE_URL=postgresql://user:password@localhost/myapp
API_KEY=sk-1234567890abcdef
DEBUG=True
MAX_CONNECTIONS=50
```

### Loading .env Files

Install python-dotenv:
```bash
pip install python-dotenv
```

Use it in your code:
```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Now you can access them normally
DATABASE_URL = os.getenv('DATABASE_URL')
API_KEY = os.getenv('API_KEY')
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

print(f"Connecting to: {DATABASE_URL}")
print(f"Debug mode: {DEBUG}")
```

### Important: Add .env to .gitignore

**Never commit .env files to version control!**

Create or update your `.gitignore`:
```gitignore
# Environment variables
.env
.env.local
.env.production

# Other common ignores
__pycache__/
*.pyc
.vscode/
.DS_Store
```

---

## Configuration Files

### What Goes Where?

**Use `.env` for:**
- Secrets (passwords, API keys, tokens)
- Environment-specific settings (database URLs, debug flags)
- Things that change between development/production

**Use config files for:**
- Application constants
- Non-secret settings
- Default values
- Lists and complex data

### Simple Config with Python Files

Create a `config.py` file:

```python
# config.py
"""Application configuration."""

# Application settings
DEFAULT_PAGE_SIZE = 20
MAX_FILE_SIZE_MB = 10
ALLOWED_FILE_TYPES = ['.jpg', '.png', '.pdf', '.txt']

# Cache settings
CACHE_TIMEOUT = 300  # 5 minutes in seconds

# API settings
REQUEST_TIMEOUT = 30  # seconds
MAX_RETRIES = 3

# Feature flags
ENABLE_EMAIL_NOTIFICATIONS = True
ENABLE_FILE_UPLOAD = True
```

Using the config:
```python
# app.py
import config

print(f"Page size: {config.DEFAULT_PAGE_SIZE}")
print(f"Allowed files: {config.ALLOWED_FILE_TYPES}")

if config.ENABLE_EMAIL_NOTIFICATIONS:
    print("Email notifications are enabled")
```
