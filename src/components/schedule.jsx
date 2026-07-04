import { useState, useEffect } from 'react';

function Schedule({ className='', schedule = []} ) {
    return(
    <div className = {`schedule ${className}}`}>
      {schedule.map((event) => (
        <>
            <p>{event.eventName}</p>
            <p>{event.eventStart}</p>
            <p>{event.eventEnd}</p>
        </>
      ))}
    </div>
    );
}

export default Schedule;