# Transport Fare Calculation
distance_in_km = float(input("Enter the Distance in km: "))
fare_per_km = float(input("Enter the Fare per km: "))
total_fare = distance_in_km * fare_per_km

print(f"Distance in km: {distance_in_km:.2f}km\nFare per km: #{fare_per_km:.2f}\nTotal Fare: #{total_fare:.2f}")