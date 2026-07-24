# Image Generation API
A FastAPI-based image genearatuib system that analyzes user requests, collects missing information through dynamic questions, builds optimizzed prompts, generates images, and supports image editing.

The project contains two main development approaches:
* `main` branch: Static prompt analysis approach
* `feature/dynamic-analyze` branch: Dynamic checklist-based analysis approach

---

# Peoject Overview

The system receives:
* Product information(`order_details`)
* User description (`user_prompt`)
* Oprional clarification answers

Then it:

1. Analyzes the user request
2. Idetifies missing information
3. Generates clarification questions
4. Builds a final image generation prompt
5. Generates the image
6. Supports editing existing images

---

# Branches

## 1. main Branch

The `main` branch implements a fixed-field analysis approach.

The analyzer checks five predefined image description fields:
* Subject
* Action
* Location
* Style
* Composition

If any field is missing, the model generates a clarification question.

## Flow

```
User Input
    |
    v
/analyze endpoint
    |
    v
Check fixed fields:
(subject, action, location, style, composition)
    |
    v
Generate missing-field questions
    |
    v
User answers questions
    |
    v
/generate endpoint
    |
    v
Prompt Builder
    |
    v
Image Generation Model
```

---

# Dynamic Analyze Branch

Branch: 

```
feature/dynamic-analyze
```
This branch improves the analysis process by removing fixed fields.

Instead of always fields.

```
subject
action
location
style
composition
```

the model dynamically decides which information is important depanding on the image request.

---

## Dynamic Analysis Flow

```
User Input
(order_details + user_prompt)

        |
        v

AI Analyzer

        |
        v

Generate dynamic checklist
(maximum 5 important fields)

        |
        v

Check each field:

complete / missing

        |
        v

Generate questions
for missing information

        |
        v

User answers questions

        |
        v

Prompt Builder

        |
        v

Image Generation
```

---

# API Endpoints

## Analyze

### Endpoint

```
POST /analyze
```

Analyzes the user request and returns required clarification questions.

---

## Request

```json
{
  "order_details": {
    "product_type": "Wall_Art",
    "medium_style": "Oil_Painting",
    "color_palette": "Tuscan_Warm",
    "dimensions": {
      "width_cm": 50,
      "height_cm": 70,
      "aspect_ratio": "5:7"
    },
    "reference_image": {
      "file_url": null,
      "mime_type": null
    }
  },
  "user_prompt": "A beautiful landscape from Caspian sea at sunset."
}
```

---

## Response Example

When all information exists:

```json
{
  "checklist": [
    {
      "name": "Subject",
      "status": "complete"
    },
    {
      "name": "Setting",
      "status": "complete"
    }
  ],
  "questions": []
}
```

When information is missing:

```json
{
  "checklist": [
    {
      "name": "Environment details",
      "status": "missing"
    },
    {
      "name": "Time of day",
      "status": "missing"
    }
  ],
  "questions": [
    {
      "field": "Environment details",
      "question": "What specific features should the mountain village or surrounding landscape include?"
    },
    {
      "field": "Time of day",
      "question": "What time of day should the painting depict?"
    }
  ]
}
```

---

# Generate Endpoint

### Endpoint

```
POST /generate
```

Generates the final image.

The endpoint receives:

* Product information
* User prompt
* Answers to clarification questions

---

## Request Example

```json
{
  "order_details": {
    "product_type": "Wall_Art",
    "medium_style": "Oil_Painting",
    "color_palette": "Warm",
    "dimensions": {
      "width_cm": 60,
      "height_cm": 90,
      "aspect_ratio": "2:3"
    }
  },
  "user_prompt": "A painting of a mountain village.",
  "answers": [
    {
      "field": "Environment details",
      "answer": "A village surrounded by pine trees and mountains."
    },
    {
      "field": "Time of day",
      "answer": "Golden hour before sunset."
    }
  ]
}
```

---

# Prompt Building

The prompt builder combines:

* Product information
* User request
* Clarification answers
* Product concept description

into a final generation prompt.

Example:

```
Product Type:
Wall Art

Style:
Oil Painting

Dimensions:
60x90 cm

User Request:
A painting of a mountain village.

Additional Details:

Environment:
A village surrounded by pine trees and mountains.

Time:
Golden hour before sunset.
```

---

# Edit Endpoint

### Endpoint

```
POST /edit
```

Edits an existing image based on user instructions.

Input:

* Image file
* Edit prompt

Example:

```
image:
mountain.png

prompt:
Change sunset sky into cloudy weather.
```

The system sends the image and instruction to the image editing model.

---

# Project Structure

```
.
├── analysis
│   ├── analyzer.py
│   └── analysis_prompt.py
│
├── builder
│   ├── prompt_builder.py
│   ├── templates.py
│   └── concepts.py
│
├── editor
│   └── edit_promt_builder.py
│
├── models
│   ├── request_models.py
│   ├── conversation_models.py
│   └── analysis_models.py
│
├── services
│   ├── analyzer_service.py
│   ├── image_edit_service.py
│   ├── openrouter_client.py
│   └── openrouter.py
│
└── app.py
```

---

# Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=
MODEL_NAME=
ANALYZER_MODEL=
AVALAI_API_KEY=
GEMINI_API_KEY=
```

---

# Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Run Project

Start FastAPI server:

```bash
uvicorn app:app --reload
```

API documentation:

```
http://127.0.0.1:8000/docs
```

---

# Technologies

* Python
* FastAPI
* Pydantic
* OpenAI SDK
* OpenRouter API
* Gemini Models
* Image Generation Models

