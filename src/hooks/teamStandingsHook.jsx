import { useEffect, useState } from 'react';

function useTeamStandings(year) {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        setLoading(true);

        fetch(`/api/teamstandings?year=${year}`)
        .then(res => res.json())
        .then(data => {
            setData(data);
            setLoading(false);
        });
    }, [year]);

    return {data, loading};
};

export default useTeamStandings;