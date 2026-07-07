import { useState, useEffect } from 'react';

function Schedule({ className='', schedule = [], loading}) {
  if (loading) {
    return(
    <div className = {`schedule schedule-table-skeleton ${className}`}> 
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
            <p>{TransformDate(event.eventStart)}-{TransformDate(event.eventEnd)}</p>
        </>
      ))}
    </div>
    );
}
function TransformDate(date) {
  let d = new Date(date).toLocaleDateString("en-GB", {
    month: "long",
    day: "numeric",
  });
  return d;
}

export default Schedule;