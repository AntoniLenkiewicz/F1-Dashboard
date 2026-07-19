import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import TransformDate from '../helpers/transformDate';

function Schedule({ year, className='', schedule = [], loading}) {
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
      <nav>
      {schedule.map((event) => (
            <Link to = {`/pastresults/${year}/${event.eventName}`}>
            <hr/>
            <h2>{event.eventName}</h2>
            <p>{TransformDate(event.eventStartDate)}-{TransformDate(event.eventEndDate)}</p>
            </Link>
      ))}
      </nav>
    </div>
    );
}


export default Schedule;