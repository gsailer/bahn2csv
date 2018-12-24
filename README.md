# bahn2csv

Small script to parse Deutsche Bahn online tickets to csv.
It splits tickets with multiple rides and saves the travel dates matched by the ticket_id:

    ticket_id;date
    ZD4H18;11.11.2018

## Prerequisites

    pip install PyPDF2

## Usage
Put all online tickets and the script in the same directory and run

    python bahn2csv.py

