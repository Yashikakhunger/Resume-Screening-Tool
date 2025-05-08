# AI-Based Resume Screening Tool

An intelligent resume screening system that uses Natural Language Processing (NLP) and Machine Learning to automate the resume parsing, analysis, and candidate ranking process for recruiters.

## Project Overview

The AI Resume Screening Tool is designed to help recruiters efficiently manage large volumes of job applications by automatically extracting information from resumes and ranking candidates based on their match with job requirements. The system uses advanced NLP techniques to understand resume content and provide objective candidate evaluations.

**Developed by:**
-Yashika Khunger and Mahak Chawla

## Features

- **Automated Resume Parsing**: Extract key details from resumes (PDF/DOCX) including:
  - Personal information (name, email, phone, location)
  - Skills and technologies
  - Education history
  - Work experience
  
- **Intelligent Candidate Ranking**:
  - Match candidates against job descriptions
  - Score based on skills, experience, education, and semantic relevance
  - Objective evaluation to reduce bias
  
- **Interactive API**:
  - Upload and process resumes
  - Create and manage job descriptions
  - Generate candidate rankings
  - RESTful interface for easy integration

- **NLP-Powered Analysis**:
  - Entity recognition for identifying key information
  - Semantic similarity using BERT embeddings
  - Skill matching against comprehensive database

## Prerequisites

Before getting started, ensure you have the following installed:

- **Python 3.8+** - For backend server
- **MongoDB** - For database storage
- **Node.js & npm** - For front-end (if using the React frontend)
- **Git** - For version control

## Installation

Follow these steps to set up the project locally:

### Clone the Repository

```bash
git clone <repository-url>
cd resume-screening-tool
```

### Backend Setup

1. Set up a Python virtual environment:

```bash
# Windows
python -m venv venv-backend
.\venv-backend\Scripts\activate

# Linux/MacOS
python -m venv venv-backend
source venv-backend/bin/activate
```

2. Install required Python packages:

```bash
pip install -r backend/requirements.txt
```

3. Download the spaCy language model:

```bash
python -m spacy download en_core_web_md
```

## MongoDB Setup

1. Install MongoDB Community Edition:
   - [Windows Installation Guide](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/)
   - [macOS Installation Guide](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)
   - [Linux Installation Guide](https://docs.mongodb.com/manual/administration/install-on-linux/)

2. Start MongoDB service:
   - Windows: `net start MongoDB`
   - macOS/Linux: `sudo systemctl start mongod` (may vary by distribution)

3. Create a database (automatically created when first accessed):
   - Default database name is `resume_screening` (configurable in .env)

## Configuration

1. Create a `.env` file in the backend directory (or update the existing one):

```
# Application Settings
APP_NAME="AI Resume Screening Tool"
APP_VERSION="1.0.0"
APP_ENVIRONMENT="development"
APP_DEBUG=true

# MongoDB Settings
APP_MONGODB_URI="mongodb://localhost:27017"
APP_DATABASE_NAME="resume_screening"

# NLP Model Settings
APP_SPACY_MODEL="en_core_web_md"
APP_BERT_MODEL="bert-base-uncased"
```

You can modify these settings based on your requirements.

## Running the Application

### Start the Backend Server

1. Activate the virtual environment if not already activated.
2. Navigate to the backend directory:

```bash
cd backend
```

3. Run the server:

```bash
# Option 1: Using Python directly
python main.py

# Option 2: Using Uvicorn
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API server should now be running at `http://localhost:8000`.

### Access the API Documentation

Once the server is running, you can access the interactive API documentation:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

Here are the main API endpoints available:

### Health Check
- `GET /`: Basic health check endpoint

### Resume Management
- `POST /api/resumes`: Upload and process a resume
- `GET /api/resumes`: Get all processed resumes
- `GET /api/resumes/{resume_id}`: Get a specific resume by ID

### Job Description Management
- `POST /api/jobs`: Create a new job description
- `GET /api/jobs`: Get all job descriptions
- `GET /api/jobs/{job_id}`: Get a specific job description by ID

### Candidate Ranking
- `POST /api/rank`: Rank candidates against a job description
- `GET /api/rank/{ranking_id}`: Get a specific ranking result by ID

## Example Usage Scenarios

### Scenario 1: Upload and Process Resumes

1. Send a POST request to `/api/resumes` with a resume file (PDF or DOCX).
2. The system will parse the resume and extract structured information.
3. Receive a response with the parsed information and a unique resume ID.

Example using cURL:
```bash
curl -X POST "http://localhost:8000/api/resumes" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@/path/to/resume.pdf"
```

### Scenario 2: Create a Job Description

1. Send a POST request to `/api/jobs` with job details.
2. The system will create and store the job description.
3. Receive a response with the job ID and details.

Example using cURL:
```bash
curl -X POST "http://localhost:8000/api/jobs" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"title\":\"Senior Python Developer\",\"company\":\"Tech Inc\",\"description\":\"Looking for an experienced Python developer...\",\"required_skills\":[\"Python\",\"Django\",\"SQL\"],\"preferred_skills\":[\"AWS\",\"Docker\"],\"experience_required\":3}"
```

### Scenario 3: Rank Candidates Against a Job

1. Send a POST request to `/api/rank` with a job ID and (optionally) specific resume IDs.
2. The system will score and rank the candidates based on the job requirements.
3. Receive a response with the ranked list of candidates and their scores.

Example using cURL:
```bash
curl -X POST "http://localhost:8000/api/rank" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "job_id=123&resume_ids=456&resume_ids=789"
```

## Future Enhancements

- Frontend web interface using React
- User authentication and role-based access control
- Improved ML algorithms for more accurate ranking
- Resume deduplication and similarity checking
- Bulk resume processing capabilities
- Integration with applicant tracking systems

