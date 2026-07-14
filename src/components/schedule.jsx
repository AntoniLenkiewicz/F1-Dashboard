import { useState, useEffect } from 'react';
import TransformDate from '../helpers/transformDate';

function Schedule({ className='', schedule = [], loading}) {
  if (loading) {
    return(
    <div className = {`schedule schedule-skeleton ${className}`}> 
      <h1>Schedule</h1>
    </div>
    );
  }
    return(
    <div className = {`schedule ${className}`}> 
      <h1>Schedule</h1>  
      {schedule.map((event) => (
        <>
            <hr/>
            <h2>{event.eventName}</h2>
            <p>{TransformDate(event.eventStartDate)}-{TransformDate(event.eventEndDate)}</p>
        </>
      ))}
    </div>
    );
}


export default Schedule;