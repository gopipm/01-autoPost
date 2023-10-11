# Import necessary libraries
from datetime import datetime

# Define the message
message = f"Today's date is {datetime.now().strftime('%Y-%m-%d')}... Stay tuned, launching soon."

# Write the message to the file
with open('daily_message.txt', 'w') as file:
    file.write(message)