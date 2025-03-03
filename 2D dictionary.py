# Question 1

# Create the following using a 2D dictionary showing the sales each person has made in the different geographical
# regions:
#         | N    | S    | E    | W    |
#   John  | 3056 | 8463 | 8441 | 2694 |
#   Tom   | 4832 | 6783 | 4737 | 3612 |
#   Anne  | 5239 | 4802 | 5832 | 1859 |
#   Fiona | 3904 | 3645 | 8821 | 2451 |
  
# Ask the user for a name and a region. Display the relevant data. Ask the user for the name and region of data
# they want to change and allow them to make the alteration to the sales figure. Display the sales for all regions
# for the name they choose.


# 2D dictionary containing sales data
sales_data = {
    'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
    'Tom': {'N': 4832, 'S': 6783, 'E': 4737, 'W': 3612},
    'Anne': {'N': 5239, 'S': 4802, 'E': 5832, 'W': 1859},
    'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}
}

# Function to display sales for a given name and region
def display_sales(name, region):
    if name in sales_data and region in sales_data[name]:
        print(f"Sales for {name} in region {region}: {sales_data[name][region]}")
    else:
        print("Invalid name or region.")

# Function to update the sales data
def update_sales(name, region, new_sales):
    if name in sales_data and region in sales_data[name]:
        sales_data[name][region] = new_sales
        print(f"Sales data for {name} in region {region} has been updated to {new_sales}.")
    else:
        print("Invalid name or region.")

# Main program
if __name__ == "__main__":
    # Ask the user for a name and a region
    name = input("Enter the name of the person: ")
    region = input("Enter the region (N, S, E, W): ")
    
    # Display the relevant sales data
    display_sales(name, region)
    
    # Ask the user for a name and region to modify sales data
    modify_name = input("Enter the name of the person to modify sales data: ")
    modify_region = input("Enter the region (N, S, E, W) to modify sales data: ")
    new_sales = int(input(f"Enter the new sales figure for {modify_name} in region {modify_region}: "))
    
    # Update the sales data
    update_sales(modify_name, modify_region, new_sales)
    
    # Display the updated sales for all regions for the selected person
    print(f"Sales data for {modify_name}: {sales_data[modify_name]}")
