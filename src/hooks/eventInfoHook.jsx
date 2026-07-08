import { useEffect, useState } from "react";

function useGetEventInfo({ year, gp}) {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        setLoading(true);
        fetch(`/api/getgpinfo?year=${year}&gp=${gp}`)
        .then(res => res.json())
        .then(data => {
            setData(data);
            setLoading(false);
        });
    }, [year, gp]);

    return {data, loading};
};

export default useGetEventInfo;