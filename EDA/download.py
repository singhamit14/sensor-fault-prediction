import requests

# URL of the CSV file
url = "https://raw.githubusercontent.com/avnyadav/sensor-fault-detection/main/aps_failure_training_set1.csv"

# Send a GET request to the URL
response = requests.get(url)

# Save the content to a file
with open("aps_failure_dataset.csv", "wb") as file:
    file.write(response.content)

print("File downloaded successfully.")