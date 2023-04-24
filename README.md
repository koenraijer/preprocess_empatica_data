# Preprocess Empatica EDA
Simple tool for preprocessing Empatica EDA data, for use in Matlab's Ledalab. The repo contains a Python script that can be compiled into an executable file using PyInstaller.

## Usage
### Creating the executable
- Install Python 3.6 or higher.
- Run `pip install requirements.txt` to install the required packages.
- Run `pyinstaller --onefile --noconsole script.py` to create the executable file.
- Run the executable file, wait until a window pops up.

### Using the executable
- Run the executable script, wait until a window pops up.
- Click "Browse" to select a folder with raw Empatica data.
- Enter a desired start time in seconds.
- Click "Process data". The processed data will be saved as a text file named `EDA_<original_file_name>_15mins.txt` in the same folder as the raw data.

### Adapting the script
- Run `pip install requirements.txt` to install the required packages.
- Edit `script.py` to your liking.
- Run `pyinstaller --onefile --noconsole script.py` to create the executable file.
- The new executable file will be in the `dist` folder.