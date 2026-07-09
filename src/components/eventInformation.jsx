import { useState, useEffect } from 'react'
import TransformDate from '../helpers/transformDate';

function EventInformation({ className, eventInfo, loading }) {
    if (loading) {
        return (
        <div className = {`event-info event-info-skeleton ${className}`}>
        </div>
        );
    };
    return (
    <div className = {`event-info ${className}`}>
        <h1>Round: {eventInfo.eventRoundNumber}</h1>
        <h1>{eventInfo.eventName}</h1>
        <p>{TransformDate(eventInfo.eventStart)} - {TransformDate(eventInfo.eventEnd)} {eventInfo.eventStart.substring(0,4)}</p>
    </div>
    );
}

export default EventInformation;