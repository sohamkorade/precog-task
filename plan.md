[x] visualize state and district data in a map
- state codes are consistent across years (manually verified)
- district codes are only available for 2010
- so we got unique state codes and district codes
- write a script to extract the codes and save them in a file

# judges data

## cleanup
- `female_judge` column has only 1 value missing, so we drop that row
- there are 3735 unclear values in `female_judge` column, so we drop those rows
- `end_date` values are missing for 18158 rows, all other columns are complete

## visualization
- male vs female plots:
	- count
	- tenure
- district plot:
	- tried to match district names with census 2011 district names with python script


## subsampling
- wrote a bash script to subsample the data
- subsampled the data to 100000 rows

[ ] check how cases are distributed across years in different states and districts
- check date of filing of cases:
	- many of the values are `year-01-01` which means that the date was just filled for the sake of filling it

[ ] date of filing of cases vs date of judgement
- check if there is a pattern in the data
- how the judging period varies across states and districts
- how the judging period varies across years

[ ] check how many cases are filed in a year

[ ] cross-gender petitioner-defendant pairs increases over the years
0.342
0.308
0.269
0.221
0.249
0.212
0.348
0.472
0.465

[ ] calendar plot the dates of filing and judgement
- check if there is a pattern in the data
- scraped holidays data from https://www1.nseindia.com/global/content/market_timings_holidays/market_timings_holidays.htm
- there is less activity on holidays and Sundays as expected
- there are less cases filed in May and June, and more in October and November

[ ] check if there is a pattern in the data


# classification

- out of 62714 types of cases (year-case pairs), 11499 are unique values
- most of them are not that frequent, i.e. the type count is skewed too much

## pendency
- there are many cases where the date of filing is 'after' the date of decision! (>1000)