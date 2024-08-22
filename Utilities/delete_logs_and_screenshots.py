import os
import glob

def delete_files(directory, file_extension):
    # This function finds all files in the directory that match the pattern *{file_extension}.
    files = glob.glob(os.path.join(directory, f"*{file_extension}"))
    for file in files:
        try:
            os.remove(file)
            print(f"Deleted: {file}")
        except Exception as e:
            print(f"Error deleting file {file}: {e}")


def delete_logs_and_screenshots():
    # Define directories
    log_dir = "selenium_logs"  # Directory for log files
    screenshot_dir = "screenshots"  # Directory for screenshots

    # Delete log files
    delete_files(log_dir, ".log")

    # Delete screenshot files
    delete_files(screenshot_dir, ".png")
