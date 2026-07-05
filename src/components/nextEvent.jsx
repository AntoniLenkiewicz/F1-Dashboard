import { useState, useEffect } from 'react'

function NextEvent({ className, nextEvent }) {
    const [timeLeft, setTimeLeft] = useState("");

    useEffect(() => {
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
}, [nextEvent.eventTime]);

    return (
        <div className = {`next-event ${className}`}>
            <h1>Round: {nextEvent.eventRoundNumber}</h1>
            <h1>{nextEvent.eventName} {nextEvent.eventType}</h1>
            <p>{timeLeft}</p>
        </div>
    );
}

export default NextEvent;