import os
import datetime


def generate_sample_logs(log_directory):
    """
    在指定目录中生成示例日志文件。

    Args:
        log_directory (str): 日志文件存放的目录
    """
    # 确保目录存在
    os.makedirs(log_directory, exist_ok=True)

    # 示例日志内容
    sample_logs = [
        ("app_20250417.log", [
            "2025-04-17 10:00:00 INFO Application started",
            "2025-04-17 10:01:00 ERROR Failed to connect to database",
            "2025-04-17 10:02:00 INFO Retry successful"
        ]),
        ("server_20250417.log", [
            "2025-04-17 09:00:00 INFO Server initialized",
            "2025-04-17 09:05:00 WARNING High CPU usage detected",
            "2025-04-17 09:10:00 INFO Server shutdown"
        ]),
        ("debug_20250417.log", [
            "2025-04-17 08:00:00 DEBUG Starting debug session",
            "2025-04-17 08:01:00 DEBUG Variable x = 42",
            "2025-04-17 08:02:00 DEBUG Session ended"
        ])
    ]

    # 生成日志文件
    for log_filename, log_content in sample_logs:
        log_filepath = os.path.join(log_directory, log_filename)
        try:
            with open(log_filepath, "w", encoding="utf-8") as f:
                f.write("\n".join(log_content))
            print(f"生成日志文件: {log_filepath}")
        except Exception as e:
            print(f"生成日志文件 {log_filename} 时出错: {e}")


if __name__ == "__main__":
    # 指定日志目录
    log_directory = "D:/study/Pycharm/自动化/logs"
    generate_sample_logs(log_directory)
