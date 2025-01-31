# HNG12 Stage 0 Backend API

## Description
This is a simple public API for the HNG12 Stage 0 Backend task. The API provides basic information, including:
- The registered email address used on the HNG12 Slack workspace.
- The current datetime in ISO 8601 format (UTC).
- The GitHub repository URL for this project.

## Technologies Used
- Python
- Flask
- Flask-CORS
- Gunicorn

## Setup Instructions
### Prerequisites
Ensure you have Python installed (version 3.7 or later). If not, download and install it from [python.org](https://www.python.org/).

### Steps to Run Locally
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   ```
2. Navigate into the project directory:
   ```bash
   cd your-repo
   ```
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the Flask application:
   ```bash
   python app.py
   ```
6. The API will be accessible at:
   ```
   http://127.0.0.1:5000/
   ```

## API Documentation
### Endpoint
**GET /**

### Response Format (200 OK)
```json
{
  "email": "nmurigi@kabarak.ac.ke",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
```

### Example Usage
#### Using cURL
```bash
curl -X GET https://hng-12-2.onrender.com/
```

#### Using Python Requests
```python
import requests

response = requests.get("https://hng-12-2.onrender.com/")
print(response.json())
```

## Deployment
The API is hosted at: [https://hng-12-2.onrender.com](https://hng-12-2.onrender.com)

## Acceptance Criteria
### Functionality
- The API must accept GET requests and return the required JSON response.
- The `current_datetime` field must be dynamically generated in ISO 8601 format (UTC).
- The API must provide an appropriate HTTP status code.

### Code Quality
- Organized code structure.

### Documentation
- The `README.md` includes:
  - A clear project description.
  - Setup instructions for running the project locally.
  - API documentation with endpoint details, request/response format, and example usage.

## Additional Resources
For more information about Python development, visit:
[Hire Python Developers](https://hng.tech/hire/python-developers)

## License
This project is licensed under the MIT License.

---

Feel free to modify the repository URL and deployment URL accordingly. 🚀

