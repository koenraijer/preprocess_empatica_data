import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

def trim_time_series(dataframe, st=0, et=0, sr=1):
    return dataframe.iloc[(st * sr):(et * sr),:]

def process_data():
    try:
        file = folder_name.get()
        start = int(start_time.get() or "0")
        period = 900
        end = start + period

        df_HR = pd.read_csv("%s/HR.csv"%file) # Load data in dataframe
        df_HR.rename(columns = {df_HR.columns[0] : "HR"}, inplace=True) # Rename column titles
        sampling_rate = int(df_HR.iloc[0,:].tolist()[0])
        df_HR = df_HR.iloc[1:]

        df_EDA = pd.read_csv("%s/EDA.csv"%file) # Load data in dataframe
        sampling_rate = int(df_EDA.iloc[0,:].tolist()[0])

        df_EDA.rename(columns = {df_EDA.columns[0] : "EDA"}, inplace=True) # Rename column titles

        df_EDA_trimmed = trim_time_series(df_EDA.iloc[2:,:], start, end, sampling_rate)

        name = "EDA_" + file.split("/")[-1] + "_15mins"
        output_file_path = f"{file}/{name}.txt"
        df_EDA_trimmed.to_csv(output_file_path, sep='\t', index=False, header=False)

        messagebox.showinfo("Success", f"Data processed successfully.\nSaved as: {output_file_path}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while processing the data: {str(e)}")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    folder_name.set(folder_selected)

root = tk.Tk()
root.title("Preprocess Empatica EDA")

folder_name = tk.StringVar()
start_time = tk.StringVar()

tk.Label(root, text="Select Folder:").grid(row=0, column=0)
tk.Entry(root, textvariable=folder_name).grid(row=0, column=1)
tk.Button(root, text="Browse", command=browse_folder).grid(row=0, column=2)

tk.Label(root, text="Enter Start Time (seconds):").grid(row=1, column=0)
tk.Entry(root, textvariable=start_time).grid(row=1, column=1)

tk.Button(root, text="Process Data", command=process_data).grid(row=2, column=1)

root.mainloop()
