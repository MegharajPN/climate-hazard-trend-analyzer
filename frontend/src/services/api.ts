import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api'; // Adjust the base URL as needed

export const getHeatwaveData = async (region: string, startDate: string, endDate: string) => {
    try {
        const response = await axios.get(`${API_BASE_URL}/heatwaves`, {
            params: { region, startDate, endDate }
        });
        return response.data;
    } catch (error) {
        console.error('Error fetching heatwave data:', error);
        throw error;
    }
};

export const getTrendAnalysis = async (region: string) => {
    try {
        const response = await axios.get(`${API_BASE_URL}/trends`, {
            params: { region }
        });
        return response.data;
    } catch (error) {
        console.error('Error fetching trend analysis:', error);
        throw error;
    }
};