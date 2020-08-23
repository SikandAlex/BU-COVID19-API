<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/en/thumb/1/15/Boston_University_Terriers_logo.svg/1200px-Boston_University_Terriers_logo.svg.png" width="300" />
</p>

<p align="center">
  <a href="#">
    <img src="https://img.shields.io/badge/made%20with-love-E760A4.svg" alt="Made with love">
  </a>
</p>

Created by Alex Sikand, MS in Artificial Intelligence Candidate 

## Base API 
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

## Get all testing data
`GET /historical`

```json
{
  "8-15-20": {
    "Daily": {
      "Date": "8-15-20", 
      "Date_TS": 1597464000.0, 
      "Invalid": 17, 
      "Negative": 1000, 
      "Positive": 2, 
      "Total": 1019
    }
  }, 
  "8-16-20": {
    "Daily": {
      "Date": "8/16/20", 
      "Date_TS": 1597550400.0, 
      "Invalid": 0, 
      "Negative": 285, 
      "Positive": 1, 
      "Total": 286
    }
  }, 
  "8-17-20": {
    "Daily": {
      "Date": "8/17/20", 
      "Date_TS": 1597636800.0, 
      "Invalid": 13, 
      "Negative": 1069, 
      "Positive": 4, 
      "Total": 1086
    }
  }, 
  "8-18-20": {
    "Daily": {
      "Date": "8/18/20", 
      "Date_TS": 1597723200.0, 
      "Invalid": 11, 
      "Negative": 950, 
      "Positive": 4, 
      "Total": 965
    }
  }, 
  "8-19-20": {
    "Daily": {
      "Date": "8/19/20", 
      "Date_TS": 1597809600.0, 
      "Invalid": 7, 
      "Negative": 1443, 
      "Positive": 0, 
      "Total": 1450
    }
  }, 
  "8-20-20": {
    "Daily": {
      "Date": "8-20-20", 
      "Date_TS": 1597896000.0, 
      "Invalid": 4, 
      "Negative": 1410, 
      "Positive": 0, 
      "Total": 1414
    }
  }, 
  "8-21-20": {
    "Cumulative": {
      "Invalid": 143, 
      "Negative": 11585, 
      "Positive": 19, 
      "Processing Time": 25.4, 
      "Total": 11747
    }, 
    "Daily": {
      "Date": "8-21-20", 
      "Date_TS": 1597968000.0, 
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

## Files 
### data_fetcher

1) Selenium + Headless Chromedriver scrapes data from PowerBI visualization available here: https://www.bu.edu/healthway/community-dashboard/
2) Uploads to Firebase Realtime Database 

### app.py 

Flask API/web server
runs data_fetcher.py every 30 minutes in the background 
