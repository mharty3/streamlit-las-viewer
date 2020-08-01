# Streamlit LAS Viewer for Denver Datas Drivers
An example streamlit app for visualizing log curves in las files. This repo is for a discussion for the Denver Data Drivers on July 28, 2020. The app is hosted on Heroku, and is running [here](https://streamlit-las-viewer.herokuapp.com/).

## Python environment set up
If you want to follow along with the demonstration, you will need to set up a Python development environment with the required packages. The best way to do that is to use the conda package. If you don't have it, download and install miniconda from [here](https://docs.conda.io/en/latest/miniconda.html).

Open the Anaconda Prompt and enter in the following commands to create an isolated environment, activate it, and use pip to install the necessary packages.

```
conda create -n ddd-streamlit-demo python=3.8
conda activate ddd-streamlit-demo
pip install streamlit lasio plotly_express
```

## Run the app
All you need to follow along with the tutorial is an environment you just set up. If you would like to clone this repository and run the app as is, you can run the app with the following command:

`streamlit run app/app.py`
