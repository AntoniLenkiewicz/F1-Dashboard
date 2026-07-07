import { useEffect, useState } from "react";

function useGetNextEvent() {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        setLoading(true);
        fetch('/api/getnextevent')
        .then(res => res.json())
        .then(data => {
            setData(data);
            setLoading(false);
        });
    }, []);

    return {data, loading};
};

export default useGetNextEvent;