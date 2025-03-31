# Travel Planner Using CrewAI

This project is an AI-powered travel planning application that leverages **CrewAI** to generate personalized travel itineraries. It provides three interfaces for users to interact with the application:

![Alt text](assests/Gemini_Generated_Image_e2lnpge2lnpge2ln.png)

1. **Streamlit Web App** (`streamlitapp.py`) - A user-friendly web interface.
2. **FastAPI Backend** (`fastapiapp.py`) - A RESTful API for programmatic access.
3. **Command-Line Interface (CLI)** (`cli_planner.py`) - A terminal-based interface for quick trip planning.

---

## Features

- **AI-Powered Itinerary Generation**: Uses CrewAI agents and tasks to create personalized travel plans.
- **Multiple Interfaces**: Access the application via a web app, API, or CLI.
- **Customizable Inputs**: Specify origin, destination, travel dates, and interests.
- **Health Check Endpoint**: Verify the API's status.
- **Environment Variable Support**: Securely manage API keys using `.env`.

---

## Prerequisites

- Python 3.9 or higher
- Required Python libraries (see `requirements.txt`)
- API keys for:
  - OpenAI (`OPENAI_API_KEY`)
  - Serper (`SERPER_API_KEY`)
  - Browserless (`BROWSERLESS_API_KEY`)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/travel-planner-using-crewai.git
   cd travel-planner-using-crewai
   ```
2. Create virtual environment and activate it 
 ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install Dependacies
```bash
  pip install -r requirements.txt

```

## Access the API
    - Root Endpoint: http://localhost:8080/
    - Swagger UI (API Docs): http://localhost:8080/docs
    - Redoc: http://localhost:8080/redoc

#### Endpoints

1. Health Check: /api/v1/health

    - Method: GET
    - Response: API health status and timestamp.

2. Plan Trip: /api/v1/plan-trip
    - Method: POST
    - Request Body:

Example Request Body:

```json
{
  "origin": "San Mateo, CA",
  "destination": "Bali, Indonesia",
  "start_date": "2024-03-01",
  "end_date": "2024-03-10",
  "interests": "2 adults who love swimming, dancing, hiking"
}
```

Example Response:

```json
{
  "status": "success",
  "message": "Trip plan generated successfully",
  "itinerary": "Your detailed itinerary here"
}
```

## CLI app

```bash
# command to run the app
python cli_planner.py -o "mumbai" -d "Crabi, Thailand" -s "2025-04-05" -e "2025-04-15" -i "2 adults who love swimming, dancing"

```

## Dir Structure
```
Travel-planner-using-crewai/
├── 
│           
├── tasks/
│   └── trip_tasks.py          # Defines CrewAI tasks for trip planning
├── tools/
│   ├── scraper.py             # Web scraping utilities
│   ├── calculator.py          # Calculation utilities
│   └── searper.py             # Search utilities
├── streamlitapp.py            # Streamlit web app
├── fastapiapp.py              # FastAPI backend
├── cli_planner.py             # Command-line interface
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (API keys)
|-- trip_agent.py              # Defines CrewAI agents for trip planning            
└── README.md   
```


