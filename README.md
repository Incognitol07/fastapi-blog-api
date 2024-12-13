Here’s the README for the **Blog API**, focusing on setup, project structure, and a testing example using `curl`:

---

# Blog API

The Blog API allows users to create, manage, and interact with blog posts and comments. It supports secure user authentication and provides endpoints for CRUD operations on posts and comments.

---

## Installation

### Prerequisites
- Python 3.10+
- PostgreSQL (or SQLite as an alternative)

### Steps to Configure:

1. **Using SQLite (Default):**
   - The application is preconfigured to use SQLite with the database file `blog.db`.
   - You don’t need to make any changes if you’re fine with SQLite.

2. **Switching to a Different Database (e.g., PostgreSQL):**
   - Open the file `app/utils/config.py`.
   - Locate the following section:
     ```python
     # Uncomment the following line to use the DATABASE_URL from the environment variables (e.g., for PostgreSQL)
     # DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")

     # Comment the above line and uncomment the following line to use SQLite instead
     DATABASE_URL: str = os.getenv("DATABASE_URL", 'sqlite:///blog.db')
     ```
   - Uncomment the line for the environment-provided `DATABASE_URL`:
     ```python
     DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")
     ```
   - Comment out the SQLite configuration line:
     ```python
     # DATABASE_URL: str = os.getenv("DATABASE_URL", 'sqlite:///blog.db')
     ```

### Steps

1. **Clone the Repository**  
   Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Incognitol07/blog-api.git
   cd blog-api
   ```

2. **Set Up Virtual Environment**  
   Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Windows: .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**  
   Copy the `.env.example` file to `.env` and configure it with your settings:
   ```bash
   cp .env.example .env
   ```
   Edit the `.env` file:
   ```text
   ENVIRONMENT=development
   DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<dbname>
   JWT_SECRET_KEY=your_jwt_secret
   ```

5. **Run the Application**  
   Start the application:
   ```bash
   uvicorn app.main:app --reload
   ```
   The API will be accessible at `http://127.0.0.1:8000`.

---

## Project Structure

```text
blog-api/
├── app/
│   ├── main.py             # Application entry point
│   ├── routers/            # API endpoints (e.g., auth, posts, comments)
│   ├── schemas/            # Pydantic models for request validation
│   ├── utils/              # Utility functions (e.g., authentication helpers)
│   ├── models/             # SQLAlchemy models for database entities
│   ├── database.py         # Database connection and session handling
│   └── config.py           # Configuration settings
├── tests/                  # Test files for API endpoints
├── requirements.txt        # Python dependencies
├── .env.example            # Example environment variables
├── Dockerfile              # Dockerfile for containerization
├── docker-compose.yml      # Docker Compose file for multi-service setup
└── README.md               # Project documentation
```

---

## Testing the API

You can use `curl`, Postman, or the interactive API docs at `http://127.0.0.1:8000/docs` to test the API.

### Example Request

#### Register a User
```bash
curl -X POST "http://127.0.0.1:8000/auth/register" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-d '{
      "username": "testuser",
      "email": "test@user.com",
      "password": "securepassword"
    }'
```

### Response
```json
{
    "message": "User registered successfully",
    "id": 1,
    "username": "testuser",
    "email": "test@user.com"
}
```

---

## License
This project is licensed under the MIT License.