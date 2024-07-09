import csv
import random
import string
from faker import Faker

# Define a function to generate a random IP address
def generate_ip():
  return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

# Create a pool of IP addresses (modify pool_size for desired number of shared IPs)
pool_size = 10
ip_pool = [generate_ip() for _ in range(pool_size)]

# Use Faker library for random names and profile pictures
fake = Faker()

# Open the CSV file for writing
with open('users.csv', 'w', newline='') as csvfile:
  # Create a CSV writer object
  writer = csv.writer(csvfile)
  
  # Write header row
  writer.writerow(['Username', "First Name" ,'Last Name', 'Post Count', 'Profile Picture', 'IP Address'])

  # Generate 10000 users
  for _ in range(10000):
    username = fake.user_name()
    first_name = fake.first_name()
    last_name = fake.last_name()
    post_count = random.randint(0, 1000)
    profile_picture = fake.image_url()
    # Randomly choose an IP address from the pool
    ip_address = random.choice(ip_pool)
    
    # Write user data to CSV
    writer.writerow([username, first_name, last_name, post_count, profile_picture, ip_address])

print("User data generated and exported to users.csv")
