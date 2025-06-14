# Extraction and Transformation Pipeline

`Randy Misati Nyambane`: `670145`

## Abstract

The project uses WSL Ubuntu 24.04 OS with default configurations as the operating system environment. The Notebook loads data from the `.csv` file in two iterations.

The first iteration loads all the data in the CSV file into a pandas dataframe. The second iteration loads data from the CSV file into a pandas dataframe after a certain time point written in the `last_extraction.txt`. It then locates the very latest date available in the dataset and sets the last_extraction checkpoint to that.

Afterwards the data is transformed by:

- Dropping irrelevant columns
- Dropping duplicate rows
- Replacing missing values using imputation
- Converting values in the `0-10` range into their corresponding textual representations from 5 predefined groups

Finally, the data is saved into a suitable CSV file.

## Tools and Frameworks

A Jupyter Notebook is employed. Python 3.12 within a virtual environment is run as the kernel for the Jupyter Notebook instance. The modules employed are detailed in the `requirements.txt` file.

## Data Source

I sourced my data from Kaggle. The data is derived from the Music and Mental Health Survey Results analysing if music therapy can improve an individual's stress, mood, and overall mental health. MT is also recognized as an evidence-based practice, using music as a catalyst for "happy" hormones such as oxytocin.

However, MT employs a wide range of different genres, varying from one organization to the next.

The dataset aims to identify what, if any, correlations exist between an individual's music taste and their self-reported mental health. Ideally, these findings could contribute to a more informed application of MT or simply provide interesting sights about the mind.

## How to Run

1. Create the virtual environment and activate it.

```bash
python3 -m venv .venv
source .venv/bin/activate
which python 
```

2. Download the needed modules.

```bash
pip install -r requirements.txt
```

3. Open the Jupyter Notebook and select the virtual environment's Python version as the kernel from which the Jupyter Notebook will base its instance.

4. Run all the code blocks. This will offer output with which to understand the explanations offered.

## Screenshots

![Full Extraction](/full_extraction.png)

![Incremental Extraction](/incremental_extraction.png)



