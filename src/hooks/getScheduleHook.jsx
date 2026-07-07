import { useEffect, useState } from "react";

function useGetSchedule(){
    const [data, setData] = useState([])
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        setLoading(true);
        fetch('/api/getschedule')
        .then(res => res.json())
        .then(data => {
            setData(data);
            setLoading(false);
        });
    }, []);
    return {data, loading};
};

export default useGetSchedule;