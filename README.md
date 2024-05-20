# Reproduction of "The Impact of Process Complexity on Process Performance: A Study Using Event Log Data”

Reproduction of the research results of the paper "The Impact of Process Complexity on Process Performance: A Study Using Event Log Data” as part of a group project in Advanced Process Mining from University of Mannheim

Paper:
Vidgof, M., Wurm, B., Mendling, J. (2023). The Impact of Process Complexity on Process Performance: A Study Using Event Log Data. In: Di Francescomarino, C., Burattin, A., Janiesch, C., Sadiq, S. (eds) Business Process Management. BPM 2023. Lecture Notes in Computer Science, vol 14159. Springer, Cham. https://doi.org/10.1007/978-3-031-41620-0_24


## Steps to recreate the CSV files

To recreate the CSV files saved in the [Complexity Data](https://github.com/MaxVidgof/complexity-data) repository by the authors follow the following steps.

### 1 Download Event Log files

Download all the original event log files used by the authors.

- [BPI Challenge 2015](https://data.4tu.nl/collections/_/5065424/1)
- [Real-life event logs - Hospital log](https://data.4tu.nl/articles/_/12716513/1)
- [BPI challenge 2017](https://data.4tu.nl/articles/_/12696884/1)
- [BPI challenge 2019](https://data.4tu.nl/articles/_/12715853/1)
- [BPI challenge 2020](https://data.4tu.nl/collections/_/5065541/1)
- [BPI challenge 2018](https://data.4tu.nl/articles/_/12688355/1)

After that, unzip them and find the XES files. For example, event log file for BPI challenge 2017 is located in `BPI Challenge 2017_1_all.zip/BPI Challenge 2017.xes.gz/BPIChallenge2017.xes`

### 2 Make sure latest version of pm4py is installed

It is possible that installed pm4py version is not the recent one. For older version of pm4py, Python scripts in the project [process-complexity](https://github.com/MaxVidgof/process-complexity) (provided by Paper authors) will throw errors.

Execute `python -m pip freeze` to check the version of installed pm4py package. If the pm4py version is not latest uninstall the package and reinstall again.

`python -m pip uninstall pm4py`
`python -m pip install -Iv pm4py==2.7.11.4`

### 3 Prepare the metrices (CSV files)

To preprae the metrices for the dowloaded event log files, we need to execute the Python scripts from the [process-complexity](https://github.com/MaxVidgof/process-complexity) project. Following are the steps for metrices preparation.

- Clone the project from Github.
- After cloning, open the command promt and set working director to the cloned directory. i.e. execute `cd D:\Python\APMProject\process-complexity`
- Now execute the **montlhy.py** script to generate metrics for a given event log file. To save the metrics as a file, use `--save-csv` option. i.e. execute `python .\monthly.py -f "D:\BPI Challenge 2017_1_all\BPI Challenge 2017.xes\BPIChallenge2017.xes" --save-csv`. This will create a file named BPIChallenge2017_metrics.csv. Generated csv file contains less number of columns than the original **merged.csv** file (in the project [Complexity Data](https://github.com/MaxVidgof/complexity-data)).
- Use **over_time.py** script to generate exactly similar csv files with more columns. Example command to execute - `python .\over-time.py -f "D:\BPI Challenge 2017_1_all\BPI Challenge 2017.xes\BPIChallenge2017.xes"`. Note that, *--save-csv* is not needed here.

### 4 Merging all CSV files

After generating all the CSV files using **over_time.py** script, we need to merge them in a single file. That file will be similar to the **merged.csv** file in the project [Complexity Data](https://github.com/MaxVidgof/complexity-data).

We registered that there are some minor floating differences between our calculations and the ones from the author.

## Step-by-step Instructions on how to replicate the experiment
Note: The following code for replication consists on a .ipynb file that was run in a Google Colab session with CPU. That is, resources are all provided by Google Services. In fact, to facilitate execution we strongly recommend to run this in the same environment.

Be aware that in our Github repository we have three main .ipynb notebooks:

•	“Regression_PROVIDED_Authors_Data.ipynb”

•	“Regression_Evaluation_Data.ipynb”

•	“Regression_COMPUTED_Authors_Data.ipynb”

These all three notebooks execute the same procedure but each one of them is defined for different input .csv data. That is, for the first notebook the procedure is done to the available data provided publicly by the authors in their paper. Then, the second notebook receives as input a .csv file that consists of ; finally, the third notebook receives as input the .csv file referring to . 

To begin with, we first need to upload to the notebook’s environment the needed files. 
In case you might want to run this code locally, you should erase the code that mounts the content of your Google Drive storage and adapt the file path of the .csv file to your machine, otherwise the file should be in your Google Drive storage and also the file path should be modified accordingly.
Once the code and the file is adapted to your environment, in case you also run the code locally, you should verify that all the imports are on your local machine.
If all previous steps are done correctly, the code’s execution is straightforward and no more interventions are needed. 

The code consists of several processes that can be summed up into two main sections:

•	A preprocessing part of the .csv file to prepare the data to be passed to the regression analysis.

•	A regression analysis consisting on the creation of full, significant and minimal models with and without the dummy variable of Industry.
