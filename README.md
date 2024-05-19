# Reproduction of "The Impact of Process Complexity on Process Performance: A Study Using Event Log Data”
Reproduction of the research results of the paper "The Impact of Process Complexity on Process Performance: A Study Using Event Log Data” as part of a group project in Advanced Process Mining from University of Mannheim

Paper:
Vidgof, M., Wurm, B., Mendling, J. (2023). The Impact of Process Complexity on Process Performance: A Study Using Event Log Data. In: Di Francescomarino, C., Burattin, A., Janiesch, C., Sadiq, S. (eds) Business Process Management. BPM 2023. Lecture Notes in Computer Science, vol 14159. Springer, Cham. https://doi.org/10.1007/978-3-031-41620-0_24


## TODOs

Repository: Your repository (provide a link in your slide set) should contain the following:

• Necessary code for the replication and any download links for code/libraries/data.

• Raw results (only if relevant, e.g., more detailed results than shown in the slides, not yet aggregated
results, …).

## Project slides


## Step-by-step Instructions on how to replicate the experiment
Note: The following code for replication consists on a .ipynb file that was run in a Google Colab session with CPU. That is, resources are all provided by Google Services. In fact, to facilitate execution we strongly recommend to run this in the same environment.

Be aware that in our Github repository we have three main .ipynb notebooks:

•	“Regression_PROVIDED_Authors_Data.ipynb”

•	“Regression_Evaluation_Data.ipynb”

•	““Regression_COMPUTED_Authors_Data.ipynb”

These all three notebooks execute the same procedure but each one of them is defined for different input .csv data. That is, for the first notebook the procedure is done to the available data provided publicly by the authors in their paper. Then, the second notebook receives as input a .csv file that consists of ; finally, the third notebook receives as input the .csv file referring to . 

To begin with, we first need to upload to the notebook’s environment the needed files. 
In case you might want to run this code locally, you should erase the code that mounts the content of your Google Drive storage and adapt the file path of the .csv file to your machine, otherwise the file should be in your Google Drive storage and also the file path should be modified accordingly.
Once the code and the file is adapted to your environment, in case you also run the code locally, you should verify that all the imports are on your local machine.
If all previous steps are done correctly, the code’s execution is straightforward and no more interventions are needed. 

The code consists of several processes that can be summed up into two main sections:

•	A preprocessing part of the .csv file to prepare the data to be passed to the regression analysis.

•	A regression analysis consisting on the creation of full, significant and minimal models with and without the dummy variable of Industry.
