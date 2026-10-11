# Climate Hazard Trend Analyzer Backend Documentation

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/climate-hazard-trend-analyzer.git
   cd climate-hazard-trend-analyzer/backend
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   uvicorn app.main:app --reload
   ```
   The application will be accessible at `http://127.0.0.1:8000`.

## Usage

- The API provides endpoints for retrieving climate hazard data, including heatwave trends and analysis.
- You can access the API documentation at `http://127.0.0.1:8000/docs` after starting the server.

## API Endpoints

- **GET /health**: Check the health status of the API.
- **GET /heatwaves**: Retrieve heatwave data based on specified parameters.

## Additional Information

For more details on the data models, services, and utilities used in the backend, please refer to the respective files in the `app` directory.