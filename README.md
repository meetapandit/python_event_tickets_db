# Python Data pipeline for Events Ticket Database

The aim of this mini project was to create a data pipeline in python to load event tickets information to a database.
- The events data was shared as a csv file. The data sources were online sales of tickets and thrid-party data from resellers which was also shared as csv
- The data was read as a pandas dataframe and uploaded to third_party_sales table in event_Sales db in MySQL
- Created a SQLAlchemy engine to connect to MySQL database
- The event_sales is now available to deep dive into the event sales and generate meaningful insights to further boost sales and enhance customer experience

## Screenshot of the table created in MySQL to upload data through the data pipeline

<p align="center"> 
  <img width="1149" alt="Screenshot 2023-12-07 at 11 49 52 AM" src="https://github.com/meetapandit/python_event_tickets_db/assets/15186489/b25f30a7-748b-4b78-bc4c-25185e66c534">
</p>
