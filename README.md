# Crypto And Stock Live Price Charts

The project involves using a combination of technologies, including Django, React, Celery, Celery Beat, and Redis, to create a website with live data visualization charts that are updated every 30/60 seconds. The data for the charts is fetched from Alphavantage API using Celery tasks, which are scheduled using Celery Beat and stored in Redis for fast retrieval. Redis is also used as a database to store updated data which are then passed through the Django REST Framework endpoint to the React frontend of the website. React takes care of the chart updates and also a Chart.js library is used for interactive charts. The website tracks prices of three stocks (Nvidia, Apple, Intel) and two cryptocurrencies (BTC, ETH).
<br /><br />
![charts](https://user-images.githubusercontent.com/91700001/227388255-52e5195a-7b09-4459-b811-297a83db620e.PNG)



https://user-images.githubusercontent.com/91700001/227389230-5db12ae5-4f26-40e9-aa3b-5d35582ae470.mp4

