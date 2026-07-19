import {useState, useEffect} from 'react';


function useGetSeasonInfo(year) {
    const [data, setData] = useState([])
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        setLoading(true);
        fetch(`/api/getseasoninfo?year=${year}`)
        .then(res => res.json())
        .then(data => {
            setData(data);
            setLoading(false);
        });
    }, [year]);
    return {data, loading};
};
export default useGetSeasonInfo;