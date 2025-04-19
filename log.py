import os
import tarfile
import datetime
import argparse


def archive_logs(log_directory):
    """
    Archives logs from the given directory into a tar.gz file with a timestamp.

    Args:
        log_directory (str): The directory containing the logs to archive.
    """

    if not os.path.exists(log_directory):
        print(f"Error: Log directory '{log_directory}' does not exist.")
        return

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_filename = f"logs_archive_{timestamp}.tar.gz"

    try:
        with tarfile.open(archive_filename, "w:gz") as tar:
            tar.add(log_directory, arcname=os.path.basename(log_directory))
        print(f"Logs archived to '{archive_filename}'")
    except Exception as e:
        print(f"Error archiving logs: {e}")
        return

    # Log the archive creation time to a file
    log_file = "archive_log.txt"
    try:
        with open(log_file, "a") as f:
            f.write(
                f"Archive created: {timestamp}, File: {archive_filename}\n")
        print(f"Archive log written to '{log_file}'")
    except Exception as e:
        print(f"Error writing to archive log: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Archive logs from a directory.")
    parser.add_argument(
        "log_directory", help="The directory containing the logs to archive.")
    args = parser.parse_args()

    archive_logs(args.log_directory)
