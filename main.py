import datetime
import pandas as pd


# Function to filter column by dates less than current date and specific email address
def filter_excel(file_path: str, email_address: str) -> str:
        
    # Load the workbook
    df: str = pd.read_excel(file_path)
    
    # Get the current date
    current_date: datetime = datetime.datetime.today()
    
    # Convert string date text in dataframe to date format
    df["date"]: str = pd.to_datetime(df["date"], format="%m/%d/%Y")
    
    # Filter data frame to show all dates less than or equal to today
    filtered_df: datetime = df[df["date"] <= current_date]
    
    # Filter dates by email_address variable
    filtered_emails: str = filtered_df.loc[(filtered_df["email"] == email_address)]

    # Transform dataframe into HTML table
    email_body: str = filtered_emails.to_html()
    
    #return email_body
    print(email_body)

def main():
    
    file_path: str = "YOUR FILE PATH HERE"
    email_address: str = "YOUR EMAIL HERE"
    filter_excel(file_path, email_address)    

if __name__ == "__main__":
    main()
