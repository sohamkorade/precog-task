# How to use

## Prepare the data

1. Download the data from [here](https://www.dropbox.com/sh/hkcde3z2l1h9mq1/AAB2U1dYf6pR7qij1tQ5y11Fa/csv?dl=0&subfolder_nav_tracking=1)

2. Extract such that the csv files are in the `csv` directory

		csv
		├── acts_sections.csv
		├── acts_sections.tar.gz
		├── cases
		│   ├── cases
		│   │   ├── cases_2010.csv
		│   │   ├── cases_2011.csv
		│   │   ├── cases_2012.csv
		│   │   ├── cases_2013.csv
		│   │   ├── cases_2014.csv
		│   │   ├── cases_2015.csv
		│   │   ├── cases_2016.csv
		│   │   ├── cases_2017.csv
		│   │   └── cases_2018.csv
		│   └── cases.tar.gz
		├── judges_clean.csv
		├── judges_clean.tar.gz
		└── keys
			├── keys
			│   ├── act_key.csv
			│   ├── cases_court_key.csv
			│   ├── cases_district_key.csv
			│   ├── cases_state_key.csv
			│   ├── disp_name_key.csv
			│   ├── judge_case_merge_key.csv
			│   ├── purpose_name_key.csv
			│   ├── section_key.csv
			│   └── type_name_key.csv
			└── keys.tar.gz

3. Subsample the large csv files to smaller csv files

	This is done to reduce the size of the files and make them easier to work with. The files are subsampled using the `subsample.sh` script. The script takes in the path to the large csv file and the path to the output file. It outputs a csv file with the `N` rows. The script is run as follows:

	Tip: you can change the value of `N` in the script to change the number of rows to subsample.

	```bash
	$ chmod +x scripts/subsample.sh
	$ ./scripts/subsample.sh csv/cases/cases/*.csv
	```

