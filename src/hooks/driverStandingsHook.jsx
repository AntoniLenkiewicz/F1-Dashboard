import { useState, useEffect, use } from 'react';

function useDriverStandings(year) { 
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        setLoading(true);

        fetch(`/api/driverstandings?year=${year}`)
        .then(res => res.json())
        .then(data => {
            setData(data);
            setLoading(false);
        });
    }, [year]);

    return {data, loading};
}

export default useDriverStandings;