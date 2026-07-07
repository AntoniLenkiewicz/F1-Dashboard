import { useState, useEffect } from 'react'

function NextEvent({ className, nextEvent, loading }) {
    const [timeLeft, setTimeLeft] = useState("");

    useEffect(() => {
        if (loading || !nextEvent) {
            return ;
        }
    const targetDate = new Date(nextEvent.eventTime).getTime();
    const timer = setInterval(() => {
    const difference= targetDate - Date.now();

    const days = Math.floor(difference / (1000 * 60 * 60 * 24));
    const hours = Math.floor((difference  / (1000 * 60 * 60)) % 24);
    const minutes = Math.floor((difference  / (1000 * 60)) % 60);
    const seconds = Math.floor((difference  / 1000) % 60);

    setTimeLeft(`${days}d ${hours}h ${minutes}m ${seconds}s`);
    }, 1000);
    return () => clearInterval(timer);
    }, [nextEvent.eventTime, loading]);

    if (loading) {
        return (
        <div className = {`next-event next-event-skeleton ${className}`}>
        </div>
        );
    };
    return (
    <div className = {`next-event ${className}`}>
        <h1>Round: {nextEvent.eventRoundNumber}</h1>
        <h1>{nextEvent.eventName} {nextEvent.eventType}</h1>
        <p>{timeLeft}</p>
    </div>
    );
}

export default NextEvent;