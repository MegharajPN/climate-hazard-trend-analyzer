# Climate Hazard Trend Analyzer

## Overview
The Climate Hazard Trend Analyzer is a web application designed to analyze and visualize climate hazard trends, specifically focusing on heatwaves. It provides users with insights into historical data, trends, and predictions related to climate hazards.

## Setup Instructions

### Backend Setup
1. Navigate to the `backend` directory.
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run the FastAPI application:
   ```
   uvicorn app.main:app --reload
   ```

### Frontend Setup
1. Navigate to the `frontend` directory.
2. Install the required dependencies:
   ```
   npm install
   ```
3. Start the React application:
   ```
   npm start
   ```

## Architecture Diagram
![Architecture Diagram](path/to/architecture-diagram.png)

## Data Source Information
The application utilizes publicly available climate data sources, including:
- National Oceanic and Atmospheric Administration (NOAA)
- European Centre for Medium-Range Weather Forecasts (ECMWF)

## Heatwave Definitions and Logic
A heatwave is defined as a prolonged period of excessively hot weather, which may be accompanied by high humidity. The application uses specific temperature thresholds and duration criteria to identify heatwaves.

## Trend Methods
The application employs statistical methods to analyze trends in heatwave occurrences, including:
- Mann-Kendall trend test
- Seasonal decomposition of time series

## Assumptions
- The data used is accurate and up-to-date.
- Users have a basic understanding of climate terminology.

## Security and Performance Measures
- The application implements authentication and authorization for sensitive endpoints.
- Rate limiting is applied to prevent abuse of the API.

## Limitations
- The analysis is limited to the available historical data.
- Predictions are based on statistical models and may not account for all variables.

## AI Tools Used and How
- Machine learning algorithms are used for predictive analytics, leveraging libraries such as scikit-learn for model training and evaluation.