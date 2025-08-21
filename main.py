import random
import time

class SmartBin:
    def __init__(self, bin_id):
        self.bin_id = bin_id
        self.bio_fill_level = 0  # Biodegradable fill level (percentage from 0 to 100)
        self.non_bio_fill_level = 0  # Non-biodegradable fill level (percentage from 0 to 100)

    def update_fill_levels(self):
        # Simulate changes in fill levels
        self.bio_fill_level = random.randint(0, 100)
        self.non_bio_fill_level = random.randint(0, 100)

    def get_status(self):
        return (
            f"Bin ID: {self.bin_id}, "
            f"Biodegradable Fill Level: {self.bio_fill_level}%, "
            f"Non-Biodegradable Fill Level: {self.non_bio_fill_level}%"
        )

class BinManagementSystem:
    def __init__(self):
        self.bins = [SmartBin(i) for i in range(1, 6)]  # Example with 5 bins

    def update_all_bins(self):
        for bin in self.bins:
            bin.update_fill_levels()

    def check_bins(self):
        alerts = []
        for bin in self.bins:
            status = bin.get_status()
            print(status)
            if bin.bio_fill_level > 80:
                alerts.append(f"Alert: {status} - Biodegradable compartment is almost full!")
            if bin.non_bio_fill_level > 80:
                alerts.append(f"Alert: {status} - Non-Biodegradable compartment is almost full!")
        return alerts

    def display_alerts(self, alerts):
        if alerts:
            print("\n*** Alerts ***")
            for alert in alerts:
                print(alert)
        else:
            print("All compartments are within safe limits.")

    def run(self):
        while True:
            print("\nUpdating bin statuses...")
            self.update_all_bins()
            alerts = self.check_bins()
            self.display_alerts(alerts)
            time.sleep(10)  # Wait for 10 seconds before the next update

if __name__ == "__main__":
    system = BinManagementSystem()
    system.run()

