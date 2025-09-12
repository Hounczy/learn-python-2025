# Checklist for Exercise 01 (bootIT)

Exercise 01 is all about setting up a cozy coding environment on your machine. Brief checklist:

1. Install the sublime text editor
2. Install VS Codium
3. Install an Anaconda distribution
4. Launch & use Jupyter notebook
5. **(only for Windows users)** Install a WSL (Windows Subsystem for Linux) 

Each step is explained in detail below.

## Step 1: Install the sublime text editor

Install the [sublime text editor](https://www.sublimetext.com).

## Step 2: Install VS Codium

Install [VS Codium](https://vscodium.com). Or, alternatively, install [Visual Studio Code](https://code.visualstudio.com).

## Step 3: Install Anaconda

Install an [Anaconda distribution](https://docs.anaconda.com/free/anaconda/install/), follow the installation instructions for your OS (operating system). Then, [verify](https://docs.anaconda.com/free/anaconda/install/verify-install/) that Anaconda has been installed correctly.  

## Step 4: Launch & use Jupyter notebook

### Step 4a: Open up the jupyter notebook application - three ways!
We will work with jupyter notebooks (`.ipynb`) in this class. The jupyter notebook application is part of the Anaconda distrubution you installed in the previous step. There are 3 ways of opening up the jupyter notebook application. Make sure you try out all three steps:
1. Through Anaconda Navigator, in your browser: go to the Anaconda Navigator, search for jupyter notebook, and click `Launch`
2. Through Anaconda Navigator, in VS Codium: go to the Anaconda Navigator, search for VS Codium, and `Launch` (more details [here](https://www.anaconda.com/docs/tools/anaconda-navigator/main); alternatively, you can also launch VS Codium directly and use the file browsing system to open up or create a jupyter notebook)
3. Through the command line interface (CLI): open your CLI (see below), type `jupyter notebook` and press Enter. The notebook should then open in a browser window.

#### Note: How do I open up the CLI? 
* macOS & linux users: search for "Terminal" in your Applications
* Windows users: !! search for "Anaconda Prompt" in your Applications. (Do NOT use the preinstalled "Windows Terminal" application)

**Screenshot of the Jupyter Notebook app in a web browser**

<p style="text-align:left;">
    <img src="../images/scs-nbapp.png" alt="Screenshot of the jupyter notebook app in a web browser" width=500px>
</p>

### Step 4b: Open and run a downloaded jupyter notebook
1. Download the jupyter notebook [`exercise01_testIT.ipynb`](./exercise01_testIT.ipynb) to your machine, to the folder of your choice
2. Open up the jupyter notebook application with the method of your choice (step 4a)
3. Navigate to the folder where the jupyter notebook is stored, and open the notebook file
4. Run all cells in the notebook by clicking on `Cell > Run All`
5. If all worked well, you should receive a friendly greeting in the notebook.

#### Note: Make the notebook "trusted"
If in your browser, make sure that the notebook is "trusted" (the top right button should say "Trusted"; if it says "Not Trusted", click and confirm to make the notebook trusted) - see screenshot below.

**Screenshot of the testIT jupyter notebook**

<p style="text-align:left;">
    <img src="../images/scs-testitnb.png" alt="Screenshot of the testIT jupyter notebook in a web browser" width=500px>
</p>

## Step 5 (only for windows users): Install WSL

If you are a macOS/Linux user: you're done for today! **If you are a Windows user**, your last task is to [install a WSL (Windows Subsystem for Linux) on your machine](./WSL.md). 
