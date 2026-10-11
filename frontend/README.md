# Climate Hazard Trend Analyzer Frontend Documentation

## Overview
The Climate Hazard Trend Analyzer frontend is built using React and TypeScript. It provides a user-friendly interface for visualizing climate hazard trends, specifically focusing on heatwaves and their impacts.

## Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/climate-hazard-trend-analyzer.git
   cd climate-hazard-trend-analyzer/frontend
   ```

2. **Install Dependencies**
   Ensure you have Node.js installed. Then, run:
   ```bash
   npm install
   ```

3. **Run the Application**
   Start the development server:
   ```bash
   npm start
   ```
   The application will be available at `http://localhost:3000`.

## Project Structure
- **public/**: Contains static files, including the main HTML file.
- **src/**: Contains the source code for the React application.
  - **components/**: Reusable components like Header.
  - **pages/**: Contains page components such as Dashboard.
  - **services/**: API service functions for backend communication.

## Usage
Once the application is running, you can navigate to the Dashboard to select regions and visualize climate hazard data. The application fetches data from the backend API and displays insights based on user selections.

## Development
- To add new features or components, create a new file in the appropriate directory within `src/`.
- Ensure to follow TypeScript conventions and maintain code quality.

## Testing
- To run tests, use:
  ```bash
  npm test
  ```

## Limitations
- The application relies on the backend API for data. Ensure the backend is running for full functionality.
- Performance may vary based on the amount of data being processed.

## Future Improvements
- Implement additional visualizations for other climate hazards.
- Enhance user experience with more interactive elements.

## Acknowledgments
This project utilizes various libraries and tools from the open-source community to provide a robust climate hazard analysis platform.