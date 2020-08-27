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

## Why are some statistics missing from the early data?
I began capturing additional data starting 8-21-20. Testing days before this date will lack certain metrics such as
'Isolated' etc.

## Get current statistics
https://bu-covid19-api.herokuapp.com/current
`GET /current`
```json
{
  "8-25-20": {
    "Cumulative": {
      "Invalid": 180, 
      "Negative": 18089, 
      "Positive": 32, 
      "Processing Time": 23.6, 
      "Total": 18301
    }, 
    "Daily": {
      "Date": "8-25-20", 
      "Date_TS": 1598328000.0, 
      "Date_Verbose": "August 25, 2020", 
      "Invalid": 11, 
      "Isolated": 26, 
      "Negative": 1891, 
      "Non-Contagious": 1, 
      "Positive": 4, 
      "Processing Time": 25.9, 
      "Recovered": 5, 
      "Total": 1906
    }
  }
}
```

## Get all testing data
https://bu-covid19-api.herokuapp.com/all
`GET /historical`

```json
{
  "data": [
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
      }
    }, 
    {
      "8-16-20": {
        "Daily": {
          "Date": "8-16-20", 
          "Date_TS": 1597550400.0, 
          "Invalid": 0, 
          "Negative": 285, 
          "Positive": 1, 
          "Total": 286
        }
      }
    }, 
    {
      "8-17-20": {
        "Daily": {
          "Date": "8-17-20", 
          "Date_TS": 1597636800.0, 
          "Invalid": 13, 
          "Negative": 1069, 
          "Positive": 4, 
          "Total": 1086
        }
      }
    }, 
    {
      "8-18-20": {
        "Daily": {
          "Date": "8-18-20", 
          "Date_TS": 1597723200.0, 
          "Invalid": 11, 
          "Negative": 950, 
          "Positive": 4, 
          "Total": 965
        }
      }
    }, 
    {
      "8-19-20": {
        "Daily": {
          "Date": "8-19-20", 
          "Date_TS": 1597809600.0, 
          "Invalid": 7, 
          "Negative": 1443, 
          "Positive": 0, 
          "Total": 1450
        }
      }
    }, 
    {
      "8-20-20": {
        "Daily": {
          "Date": "8-20-20", 
          "Date_TS": 1597896000.0, 
          "Invalid": 4, 
          "Negative": 1410, 
          "Positive": 0, 
          "Total": 1414
        }
      }
    }, 
    {
      "8-21-20": {
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
    }, 
    {
      "8-22-20": {
        "Daily": {
          "Date": "8-22-20", 
          "Date_TS": 1598054400.0, 
          "Date_Verbose": "August 22, 2020", 
          "Invalid": 9, 
          "Isolated": 21, 
          "Negative": 1925, 
          "Non-Contagious": 1, 
          "Positive": 6, 
          "Processing Time": 18.4, 
          "Recovered": 3, 
          "Total": 1940
        }
      }
    }, 
    {
      "8-23-20": {
        "Daily": {
          "Date": "8-23-20", 
          "Date_TS": 1598155200.0, 
          "Date_Verbose": "August 23, 2020", 
          "Invalid": 8, 
          "Isolated": 19, 
          "Negative": 1270, 
          "Non-Contagious": 1, 
          "Positive": 0, 
          "Processing Time": 15.7, 
          "Recovered": 5, 
          "Total": 1278
        }
      }
    }, 
    {
      "8-24-20": {
        "Daily": {
          "Date": "8-24-20", 
          "Date_TS": 1598241600.0, 
          "Date_Verbose": "August 24, 2020", 
          "Invalid": 8, 
          "Negative": 1270, 
          "Positive": 0, 
          "Total": 1278
        }
      }
    }, 
    {
      "8-25-20": {
        "Cumulative": {
          "Invalid": 180, 
          "Negative": 18089, 
          "Positive": 32, 
          "Processing Time": 23.6, 
          "Total": 18301
        }, 
        "Daily": {
          "Date": "8-25-20", 
          "Date_TS": 1598328000.0, 
          "Date_Verbose": "August 25, 2020", 
          "Invalid": 11, 
          "Isolated": 26, 
          "Negative": 1891, 
          "Non-Contagious": 1, 
          "Positive": 4, 
          "Processing Time": 25.9, 
          "Recovered": 5, 
          "Total": 1906
        }
      }
    }
  ]
}
```

## Files 
### data_fetcher.py

1) Selenium + Headless Chromedriver scrapes data from PowerBI visualization available here: https://www.bu.edu/healthway/community-dashboard/
2) Checks to see if new data has been added
3) If everything up to date, do nothing, otherwise update the data.json file

### app.py 

Flask API/web server
runs update_data() from data_fetcher.py every 15 minutes in the background 
