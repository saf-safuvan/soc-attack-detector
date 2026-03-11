import re

log_file = input("Enter log file path: ")

failed_attempts = {}
threshold = 3

with open(log_file, "r") as file:
    logs = file.readlines()

for line in logs:

    if "failed password" in line.lower():

        ip_match = re.findall(r'\d+\.\d+\.\d+\.\d+', line)

        if ip_match:

            ip = ip_match[0]

            if ip not in failed_attempts:
                failed_attempts[ip] = 1
            else:
                failed_attempts[ip] += 1


print("\n=== SOC Attack Detection Report ===\n")

for ip, count in failed_attempts.items():

    if count >= threshold:

        print(f"ALERT: Possible brute force attack from {ip} ({count} failed attempts)")
