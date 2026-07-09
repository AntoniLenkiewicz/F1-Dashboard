import { useEffect, useState } from 'react';

function useGetResults({year, gp, session=''}) {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        setLoading(true);
        fetch(`api/getgpresults?year=${year}&gp=${gp}&session=${session}`)
        .then(res => res.json())
        .then(data => {
            setData(data);
            setLoading(false);
        });
    }, [year, gp, session]);
    return {data, loading}; 
};

export default useGetResults;