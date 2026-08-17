# 📝 Customer Feedback Analyzer

A full-stack application that analyzes customer reviews using Google Gemini AI. Features a Streamlit dashboard frontend and FastAPI backend with persistent SQLite storage.

## Features

- **Review Analysis**: Automatically analyze customer feedback using Google's Gemini 3.5 Flash model
- **Multi-dimensional Insights**: Each review is classified by:
  - **Sentiment**: Positive, negative, or neutral
  - **Score**: 1-5 rating scale (1=very bad, 5=very good)
  - **Theme**: Category of feedback (food, service, ambience, etc.)
- **Batch Processing**: Analyze multiple reviews at once (one per line)
- **Data Persistence**: All results stored in SQLite database for historical tracking
- **User-Friendly Dashboard**: Streamlit web interface for easy review submission and analysis

## Architecture

### Components

1. **Frontend** (`app.py`): Streamlit dashboard where users submit and analyze reviews
2. **Backend** (`api.py`): FastAPI service that processes reviews via Google Gemini API
3. **Database** (`database.py`): SQLite database management for storing analysis results

### Workflow

```
User Input (Streamlit) 
    ↓
HTTP POST Request (FastAPI endpoint)
    ↓
Google Gemini API (analyze review)
    ↓
Parse & Validate Response (Pydantic)
    ↓
Return Results to Dashboard
    ↓
Store in SQLite Database
```

## Requirements

- Python 3.14+
- Google Gemini API key
- Internet connection for API calls

## Installation

1. **UV Installation methods:**
   ```bash
   https://docs.astral.sh/uv/getting-started/installation/
   ```

2. **Clone or navigate to the project directory:**
   ```bash
   cd Customer-Feedback-Analyzer
   ```

3. **Install dependencies using uv:**
   ```bash
   uv pip install -e .
   ```

   Or install packages individually:
   ```bash
   uv pip install fastapi[standard] google-genai pydantic python-dotenv requests streamlit
   ```

## Configuration

### Set Up Environment Variables

Create a `.env` file in the project root with your Google Gemini API credentials:

```env
GOOGLE_API_KEY=your_api_key_here
```

To get your API key:
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click "Create API Key"
3. Copy the key and add it to `.env`

## Usage

### Initiate Virtual Environment

### Activate the Virtual Environment

1. Navigate to the project directory and activate the virtual environment:

   - **Windows (Command Prompt):**
     ```cmd
     .venv\Scripts\activate
     ```
   - **Windows (PowerShell):**
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   - **macOS / Linux:**
     ```bash
     source .venv/bin/activate
     ```

2. **Verify Activation:**
   Ensure the prompt shows `(.venv)` or verify the Python path:
   
   - **Windows:**
     ```cmd
     where python
     ```
   - **macOS / Linux:**
     ```bash
     which python
     ```

   **Expected Output:**
   The output should point to the `.venv` directory (e.g., `...\Customer-Feedback-Analyzer\.venv\Scripts\python.exe`).

### Start the Backend (API Server)

In one terminal, run the FastAPI server:

```bash
uv run python api.py
```

Or with uvicorn directly:
```bash
uv run uvicorn api:app --reload
```

Or with activated virtual environment terminal:
```bash
fastapi run api.py
```

The API will be available at `http://127.0.0.1:8000`

### Start the Frontend (Streamlit Dashboard)

In a second terminal, run the Streamlit app:

```bash
uv run streamlit run app.py
```

The dashboard will open at `http://localhost:8501`

### Analyze Reviews

1. Open the Streamlit dashboard in your browser
2. Paste customer reviews into the text area (one per line)
3. Click the "Analyze" button
4. View results in real-time with sentiment labels, scores, and themes

## API Endpoints

### POST `/analyze_feedback`

Analyzes a single customer review.

**Request:**
```json
{
  "content": "The food was excellent but the service was slow"
}
```

**Response:**
```json
{
  "label": "positive",
  "score": 4.0,
  "theme": "service"
}
```

## Database

### Storage

- **File**: `feedback.db` (SQLite database)
- **Table**: `feedback`
  - `id`: Auto-increment primary key
  - `review`: Customer review text
  - `label`: Sentiment classification (positive/negative/neutral)
  - `score`: Numerical rating (1-5)
  - `theme`: Topic category (one word)

### Data Persistence

All analyzed reviews are automatically saved to the database and can be retrieved for historical analysis and reporting.

## Project Structure

```
9_PROJECT_FEEDBACK_ANALYZER/
├── app.py                          # Streamlit frontend dashboard
├── api.py                          # FastAPI backend service
├── database.py                     # SQLite database management
├── pyproject.toml                  # Project configuration and dependencies
├── .env                            # Environment variables (API key)
├── feedback.db                     # SQLite database file (auto-created)
└── README.md                       # This file
```

## Dependencies

- **fastapi[standard]**: Web framework for the API backend
- **google-genai**: Google Generative AI client library
- **pydantic**: Data validation and settings management
- **python-dotenv**: Environment variable management
- **requests**: HTTP client for frontend API calls
- **streamlit**: Web app framework for the dashboard

## Notes

- The backend uses **Gemini 3.5 Flash** model for fast, cost-effective analysis
- Temperature set to 0.7 for balanced creativity and consistency
- Response format enforced as JSON using Pydantic schemas
- Frontend and backend must run in separate terminal windows
- Review analyses are stored immediately upon completion

## Troubleshooting

**API Connection Error**: Ensure the FastAPI backend is running (`python api.py`) before starting the frontend.

**API Key Error**: Verify your `.env` file contains a valid `GOOGLE_API_KEY`.

**Database Issues**: Delete `feedback.db` to reset the database (it will be recreated automatically).

## License

*This project is developed as part of the Python Generative AI and Agentic AI coursework using Google Gemini models.*