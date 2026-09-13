# AI Diet Meal Planner

A FastAPI application that helps users plan meals based on their available ingredients and dietary preferences. It provides endpoints to check inventory, get diet-friendly suggestions, generate meal plans, and receive recipe recommendations.

## Features

- Check which ingredients are usable from a list of items
- Filter ingredients and meals by dietary preference
- Combine inventory and diet inputs for meal suggestions
- Generate step-by-step recipe plans
- Recommend multiple recipes based on ingredients and diet

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/SadekAlSaabari/ai-diet-meal-planner.git
cd ai-diet-meal-planner
```

### 2. Create a .env file

Create a local .env file in the project root in the format of the .env.example and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

You can obtain a Groq API key from the Groq console.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
uvicorn main:app --reload
```

The API will be available at:

```bash
http://127.0.0.1:8000
```

## Usage

The API exposes the following endpoints:

- `GET /` — Health check
- `POST /inventory` — Analyze inventory items
- `POST /diet` — Get diet-based ingredient and recipe suggestions
- `POST /ask` — Combine inventory and diet checks
- `POST /plan` — Generate a recipe plan
- `POST /recommend` — Recommend recipes based on items and diet

You can test the endpoints using Swagger UI at:

```bash
http://127.0.0.1:8000/docs
```

## Docker

### Build the image

```bash
docker build -t ai-diet-planner .
```

### Run the container

```bash
docker run --env-file .env --name ai-diet-planner -p 8000:8000 ai-diet-planner:latest
```
