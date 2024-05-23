# Reproduction of "The Impact of Process Complexity on Process Performance: A Study Using Event Log Data”

Reproduction of the research results of the paper "The Impact of Process Complexity on Process Performance: A Study Using Event Log Data” as part of a group project in Advanced Process Mining from University of Mannheim

Paper:
Vidgof, M., Wurm, B., Mendling, J. (2023). The Impact of Process Complexity on Process Performance: A Study Using Event Log Data. In: Di Francescomarino, C., Burattin, A., Janiesch, C., Sadiq, S. (eds) Business Process Management. BPM 2023. Lecture Notes in Computer Science, vol 14159. Springer, Cham. https://doi.org/10.1007/978-3-031-41620-0_24

The following steps are necessary to replicate the results of the paper:
1. Calculation of the complexity metrics and the troughput time as the independent and dependent variables
2. Conduct the regression analysis with forward, backward and both method variable selection based on the AIC. 

## 1. Calculation of the complexity metrics

To recreate the CSV file saved in the [Complexity Data](https://github.com/MaxVidgof/complexity-data) repository by the authors follow the following steps.

### 1.1 Download Event Log files

Download all the original event log files used by the authors.

- [BPI Challenge 2015](https://data.4tu.nl/collections/_/5065424/1)
- [Real-life event logs - Hospital log](https://data.4tu.nl/articles/_/12716513/1)
- [BPI challenge 2017](https://data.4tu.nl/articles/_/12696884/1)
- [BPI challenge 2019](https://data.4tu.nl/articles/_/12715853/1)
- [BPI challenge 2020](https://data.4tu.nl/collections/_/5065541/1)
- [BPI challenge 2018](https://data.4tu.nl/articles/_/12688355/1)

After that, unzip them and find the XES files. For example, event log file for BPI challenge 2017 is located in `BPI Challenge 2017_1_all.zip/BPI Challenge 2017.xes.gz/BPIChallenge2017.xes`

### 1.2. Clone the repo for complexity calculation
Clone the following repo to get the scripts necessary for reproduction https://github.com/MaxVidgof/process-complexity

### 1.3 Make sure latest version of pm4py is installed

It is possible that installed pm4py version is not the recent one. For older version of pm4py, Python scripts in the project [process-complexity](https://github.com/MaxVidgof/process-complexity) (provided by Paper authors) will throw errors.

Execute `python -m pip freeze` to check the version of installed pm4py package. If the pm4py version is not latest uninstall the package and reinstall again.

`python -m pip uninstall pm4py`
`python -m pip install -Iv pm4py==2.7.11.4`

### 1.4 Run complexity script
- Now execute the **montlhy.py** script to generate metrics for a given event log file. To save the metrics as a file, use `--save-csv` option. i.e. execute `python .\monthly.py -f "D:\BPI Challenge 2017_1_all\BPI Challenge 2017.xes\BPIChallenge2017.xes" --save-csv`. This will create a file named BPIChallenge2017_metrics.csv. Generated csv file contains less number of columns than the original **merged.csv** file (in the project [Complexity Data](https://github.com/MaxVidgof/complexity-data)).
- Use **over_time.py** script to generate exactly similar csv files with more columns. Example command to execute - `python .\over-time.py -f "D:\BPI Challenge 2017_1_all\BPI Challenge 2017.xes\BPIChallenge2017.xes"`. Note that, *--save-csv* is not needed here.

### 1.5 Merging all CSV files

After generating all the CSV files using **over_time.py** script, we need to merge them in a single file. That file will be similar to the **merged.csv** file in the project [Complexity Data](https://github.com/MaxVidgof/complexity-data).

We registered that there are some minor floating differences between our calculations and the ones from the author.

## 2 Conduct the regression analysis
Note: The following code for replication consists on a .ipynb files that was run in a Google Colab session with CPU. To facilitate execution we strongly recommend to run this in the same environment.

Be aware that in our Github repository we have two main .ipynb notebooks:

- Regression_PROVIDED_Authors_Data.ipynb

- Only_industry_variable_as_predictor.ipynb

The Regression_PROVIDED_Authors_Data is the main notebook conducting the regression analysis in the same manner as the authors have done it in their project. We created 3 copys of the notebook. Each differ only in regard to the input csv-file. So to gain the same results as we did. You can either duplicate the provided notebook and change the input file or you just re-run the notebook and change the input file after every iteration. 

That first notebook shows the procedure with the available data provided publicly by the authors over their github. You find the other data input files in our data subfolders. 

- provided_data          - its the same file as the authors shared in their github
- replicated_data        - this file was replicated by us after following the instructions from the authors
- test_data              - this file was newly built by us on before unseen data and was used to test the external validity of the model

To begin with, we first need to upload to the notebook’s environment the needed files. 
In case you want to run this code yourself, you should adjust the section in the beginning where you specific the csv-file location to a local folder where you have control about.
If all previous steps are done correctly, the code’s execution is straightforward.

The notebooks build the models based on following, backward and both selection method for two different subsets: One with and one without industry encoded as a dummy variabe. In addition, the models are calculated for all variables, minimal models and only for significant variables.

The other notebook Only_industry_variable_as_predictor.ipynb was used to validate/falsify the hypothesis from the authors that the industry dummy variable alone accounts for 80% of the total variance. This notebook have a similiar preprocessing as the other one, but the building of the model is way easier with respect to having only one independent variable.
