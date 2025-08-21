SmartBin Management System

The SmartBin Management System is a Python-based simulation that monitors the fill levels of biodegradable and non-biodegradable waste bins. The system updates bin statuses in real-time and generates alerts when any compartment is almost full.

🚀 Features

Monitors multiple bins (default: 5).

Tracks both biodegradable and non-biodegradable compartments.

Generates alerts when capacity exceeds 80%.

Updates automatically at fixed intervals (default: 10 seconds).

▶️ Usage

Run the script with:

python smartbin.py


Example Output:

Updating bin statuses...
Bin ID: 1, Biodegradable Fill Level: 45%, Non-Biodegradable Fill Level: 90%
Bin ID: 2, Biodegradable Fill Level: 20%, Non-Biodegradable Fill Level: 65%

*** Alerts ***
Alert: Bin ID: 1, Non-Biodegradable compartment is almost full!

⚙️ Customization

Number of bins → Change in BinManagementSystem:

self.bins = [SmartBin(i) for i in range(1, 11)]  # Example with 10 bins


Alert threshold → Default is 80%, can be modified in check_bins().

Update interval → Change time.sleep(10) to adjust refresh rate.

📌 Future Enhancements

Real-time data from IoT sensors instead of random values.

Database integration for storing and analyzing bin data.

Dashboard/web app for live monitoring.

SMS/Email notifications when bins are full.
