import { useState, useEffect } from 'react'

function NextEvent({ className, nextEvent }) {
    return (
        <div className = {`next-event ${className}`}>
            <h1>Round: {nextEvent.eventRoundNumber}</h1>
            <h1>{nextEvent.eventName} {nextEvent.eventType}</h1>
            <p>(Implement Timer {nextEvent.eventTime})</p>
        </div>
    );
}

export default NextEvent;