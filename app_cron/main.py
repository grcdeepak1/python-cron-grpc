# app/main.py
import datetime
import time
import os

def run_job():
    """
    The main logic for your cron job.
    Replace this with your actual task.
    """
    now = datetime.datetime.now(datetime.timezone.utc)
    job_id = os.getenv('JOB_ID', 'unknown') # Example: Reading an env variable

    print(f"[{now.isoformat()}] Python CronJob ({job_id}) started.")

    # --- Your Cron Job Logic Goes Here ---
    # Example: Simulate some work
    print("Performing scheduled task...")
    time.sleep(10) # Simulate work for 10 seconds
    # --- End of Your Logic ---

    now_finished = datetime.datetime.now(datetime.timezone.utc)
    print(f"[{now_finished.isoformat()}] Python CronJob ({job_id}) finished.")


if __name__ == "__main__":
    # Kubernetes Jobs typically run the container command once and expect it to exit.
    # If your script needs to run continuously until a condition, manage that here.
    # For a simple 'do work and exit' cron job, just call the main function.
    run_job()
