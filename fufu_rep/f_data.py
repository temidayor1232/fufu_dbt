from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker()

# Random functions for synthetic data generation
def random_gender():
    return random.choice(['Male', 'Female', 'Non-Binary'])

def random_loyalty_status():
    return random.choice(['Basic', 'Silver', 'Gold', 'Platinum'])

def random_item_category():
    return random.choice(['Starter', 'Main', 'Dessert', 'Drink', 'Side'])

def random_region():
    return random.choice(['North America', 'Europe', 'Asia', 'Africa', 'Oceania'])

def random_city():
    return random.choice(["New York", "Paris", "Tokyo", "Cape Town", "Sydney"])

international_dishes = [
    'Tacos', 'Sushi', 'Pizza', 'Biryani', 'Paella', 
    'Chow Mein', 'Baguette', 'Shawarma', 'Curry', 'Hamburger',
    'Falafel', 'Moussaka', 'Ramen', 'Kebab', 'Pasta',
    'Croissant', 'Doner Kebab', 'Pho', 'Crepe', 'Gelato'
]

def random_food_name():
    return random.choice(international_dishes)

def random_food_description():
    descriptions = [
        "A savory international delight", "Made with fresh ingredients", 
        "Authentic and flavorful", "Richly seasoned", "Perfect for sharing", 
        "A burst of exotic flavors", "Served with love", "Traditional recipe with a modern twist"
    ]
    return random.choice(descriptions)

# Generate synthetic customer data
def generate_customers(num_records):
    customers = []
    for _ in range(num_records):
        customer = {
            'customer_id': fake.uuid4(),
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'phone_number': fake.phone_number(),
            'address': fake.address().replace("\n", ", "),
            'gender': random_gender(),
            'loyalty_status': random_loyalty_status()
        }
        customers.append(customer)
    return pd.DataFrame(customers)

# Generate synthetic menu data
def generate_menu_items(num_records):
    menu_items = []
    while len(menu_items) < num_records:
        menu_item = {
            'item_id': fake.uuid4(),
            'name': random_food_name(),
            'price': round(random.uniform(5, 100), 2),
            'item_category': random_item_category(),
            'food_description': random_food_description()
        }
        menu_items.append(menu_item)
    return pd.DataFrame(menu_items)

# Generate synthetic branch data
def generate_branches(num_records):
    branches = []
    while len(branches) < num_records:
        branch = {
            'branch_id': fake.uuid4(),
            'branch_name': fake.company(),
            'branch_location': fake.address().replace("\n", ", "),
            'city': random_city(),
            'region': random_region()
        }
        branches.append(branch)
    return pd.DataFrame(branches)

# Generate synthetic transaction data
def generate_transactions(num_records, customers, menu_items, branches):
    transactions = []
    for _ in range(num_records):
        transaction = {
            'transaction_id': fake.uuid4(),
            'customer_id': random.choice(customers['customer_id']),
            'branch_id': random.choice(branches['branch_id']),
            'item_id': random.choice(menu_items['item_id']),
            'amount': round(random.uniform(10, 200), 2),
            'payment_method': random.choice(['Cash', 'Credit Card', 'Mobile Payment']),
            'transaction_date': fake.date_this_year(),
            'dining_option': random.choice(['Dine-in', 'Take-out', 'Delivery']),
        }
        transactions.append(transaction)
    return pd.DataFrame(transactions)

# Generate and save the data
num_records = 1000

customers_df = generate_customers(num_records)
menu_items_df = generate_menu_items(50)
branches_df = generate_branches(10)
transactions_df = generate_transactions(num_records, customers_df, menu_items_df, branches_df)

# Save the data to CSV files
customers_df.to_csv('customers.csv', index=False)
menu_items_df.to_csv('menu_items.csv', index=False)
branches_df.to_csv('branches.csv', index=False)
transactions_df.to_csv('transactions.csv', index=False)

print("New synthetic data generated and saved as CSV files!")