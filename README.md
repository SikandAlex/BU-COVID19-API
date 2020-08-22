# Boston University COVID-19 API
https://bu-covid19-api.herokuapp.com

## Get current statistics
`GET /current`
```json
{
  "Cumulative": {
    "Invalid": 143, 
    "Negative": 11585, 
    "Positive": 19, 
    "Processing Time": 25.4, 
    "Total": 11747
  }, 
  "Daily": {
    "Date": "8-21-20", 
    "Date_TS": 1597982400.0, 
    "Date_Verbose": "August 21, 2020", 
    "Invalid": 10, 
    "Isolated": 16, 
    "Negative": 1443, 
    "Non-Contagious": 1, 
    "Positive": 3, 
    "Processing Time": 23.1, 
    "Recovered": 2, 
    "Total": 1456
  }
}
```

## Get data for a specific day
`GET /date/:day`

Date format example: 8-20-20
`GET /date/:8-20-20`

```json
{
  "Daily": {
    "Date": "8-20-20", 
    "Date_TS": 1597896000.0, 
    "Invalid": 4, 
    "Negative": 1410, 
    "Positive": 0
  }
}
```

## Files 
### data_fetcher

1) Selenium + Headless Chromedriver scrapes data from PowerBI visualization available here: https://www.bu.edu/healthway/community-dashboard/
2) Uploads to Firebase Realtime Database 

### app.py 

Flask API/web server
runs data_fetcher.py every 30 minutes in the background 
