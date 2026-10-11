import React, { useEffect, useState } from 'react';
import { fetchHeatwaveData } from '../services/api';

const Dashboard: React.FC = () => {
    const [data, setData] = useState<any[]>([]);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const getData = async () => {
            try {
                const result = await fetchHeatwaveData();
                setData(result);
            } catch (err) {
                setError('Failed to fetch data');
            } finally {
                setLoading(false);
            }
        };

        getData();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>{error}</div>;
    }

    return (
        <div>
            <h1>Climate Hazard Trend Analyzer</h1>
            <h2>Heatwave Data</h2>
            <ul>
                {data.map((item, index) => (
                    <li key={index}>
                        <strong>Region:</strong> {item.region} <br />
                        <strong>Heatwave Days:</strong> {item.heatwaveDays} <br />
                        <strong>Year:</strong> {item.year}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Dashboard;