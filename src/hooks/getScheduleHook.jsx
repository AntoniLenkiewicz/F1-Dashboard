import { useEffect, useState } from "react";

function useGetSchedule(year){
    const [data, setData] = useState([])
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        setLoading(true);
        fetch(`/api/getschedule?year=${year}`)
        .then(res => res.json())
        .then(data => {
            setData(data);
            setLoading(false);
        });
    }, []);
    return {data, loading};
};

export default useGetSchedule;