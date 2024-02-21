import datetime
import pandas as pd

# Function to filter column by dates less than current date and specific email address
def filter_excel(file_path, email_address):
    
    # Load the workbook
    df = pd.read_excel(file_path)
    
    # Get the current date
    current_date = datetime.datetime.today()
    
    # Convert string date text in dataframe to date format
    df['date'] = pd.to_datetime(df['date'], format="%m/%d/%Y")
    
    # Filter data frame to show all dates less than or equal to today
    filtered_df = df[df['date'] <= current_date]
    
    # Filter dates by email_address variable
    filtered_emails = filtered_df.loc[(filtered_df['email'] == email_address)]

    email_body = filtered_emails.to_html()
    
    return email_body
    

if __name__ == "__main__":

    file_path = ""  # Replace with your file path
    email_address = ""  # Replace with the email address to filter by

    filter_excel(file_path, email_address)
