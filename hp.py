import xml.etree.ElementTree as ET
import pandas as pd

# Load the XML file
tree = ET.parse("book.xml")
root = tree.getroot()

# Create empty lists to store book information
categories = []
titles = []
authors_list = []
years = []
prices = []
borrowers = []  # New field
issued_dates = []  # New field
return_dates = []  # New field

# Iterate through each <book> element
for book in root.findall(".//book"):
    category = book.get("category")
    title = book.find("title").text
    authors = ", ".join([author.text for author in book.findall("author")])
    year = book.find("year").text
    price = book.find("price").text

    # New fields for borrower, issued date, and return date
    borrower = input(f"Enter borrower for '{title}': ")
    issued_date = input(f"Enter issued date for '{title}' (YYYY-MM-DD): ")
    return_date = input(f"Enter return date for '{title}' (YYYY-MM-DD): ")

    # Append book information to the lists
    categories.append(category)
    titles.append(title)
    authors_list.append(authors)
    years.append(year)
    prices.append(price)
    borrowers.append(borrower)
    issued_dates.append(issued_date)
    return_dates.append(return_date)

# Create a DataFrame from the collected information
data = {
    "Category": categories,
    "Title": titles,
    "Authors": authors_list,
    "Year": years,
    "Price": prices,
    "Borrower": borrowers,
    "IssuedDate": issued_dates,
    "ReturnDate": return_dates,
}

df = pd.DataFrame(data)

# Print the DataFrame in table format
print(df)

# Update the XML file with the new information
for book, row in zip(root.findall(".//book"), df.iterrows()):
    # Check if the elements exist before setting their values
    borrower_element = book.find("borrower")
    issued_date_element = book.find("issuedDate")
    return_date_element = book.find("returnDate")
    
    if borrower_element is not None:
        borrower_element.text = row[1]["Borrower"]
    
    if issued_date_element is not None:
        issued_date_element.text = row[1]["IssuedDate"]
    
    if return_date_element is not None:
        return_date_element.text = row[1]["ReturnDate"]

# Save the updated XML tree to a new file
tree.write("updated_book.xml")
