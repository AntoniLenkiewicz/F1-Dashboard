import { useState, useEffect } from 'react'


function DriverStandings({ driverStandings }){
    return (
    <div className='standings-table'>
        <table>
            <thead>
            <tr>
                <th>Pos</th>
                <th>Driver</th>
                <th>Points</th>
            </tr>
            </thead>
            <tbody>
            {Object.entries(driverStandings)
            .sort((a, b) => b[1] - a[1])
            .map(([driver, points], index) => (
                <tr key={driver}>
                <td>{index + 1}</td>
                <td>{driver}</td>
                <td>{points}</td>
                </tr>
            ))}
            </tbody>
        </table>
        </div>
    );
}

export default DriverStandings;