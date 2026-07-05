# F1 Dashboard

## React + Vite + Flask + TailwindCSS

Project Status: ongoing

## Overview

A web app created for Formula one to view live telemtry and race statistics, past race data and current season standings.

## Application Architecture:

The application is split into two parts, a backend flask server and a react frontend

## Flask backend

The flask backend fetches data primarily through the FastF1 python library which gathers data from three seperate APIs.

The flask server acts as an API server providing the data to the front end through API requests in the form of JSON arrays or JSON objects.

## React Frontend

The React Frontend requests data necessary, manages routing and after recieving the data displays it to the user. The frontend is styled using TailwindCSS allowing for a responsive design which scales to display components correctly for a variety of different devices.
