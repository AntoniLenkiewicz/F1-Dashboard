import { useState, useEffect } from 'react'

function NextEvent({ className, nextEvent }) {
    return (
        <div className = {`next-event ${className}`}>
            <h1>Next Event</h1>
            <p>{nextEvent.eventName}</p>
            <p>{nextEvent.eventType}</p>
            <p>{nextEvent.eventRoundNumber}</p>
        </div>
    );
}

export default NextEvent;