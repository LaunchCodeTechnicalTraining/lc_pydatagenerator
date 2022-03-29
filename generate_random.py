from faker import Faker
import random

def user_data(filename="example-user-data.csv", num_of_records=1000):
    """Write a new file with first_name, last_name, email, and company.

    Keyword arguments:
    filename -- name of file you are writing to or overwriting (default "example-user-data.csv)
    num_of_records -- Number of dummy records you would like the function to create (default 1000)
    """

    fake = Faker()

    with open(filename, 'w') as the_file:
        for i in range(num_of_records):
            the_file.write("{},{},{},{}\n".format(fake.first_name(), fake.last_name(), fake.email(), fake.company()))

def sensitive_user_data(filename="example-sensitive-user-data.csv", num_of_records=1000):
    """Writes a new file with a user_name, password, and email.

    Keyword arguments:
    filename -- name of file you are writing to or overwriting (default "example-sensitive-user-data.csv)
    num_of_records -- Number of dummy records you would like the function to create (default 1000)
    """

    fake = Faker()

    with open(filename, 'w') as the_file:
        for i in range(num_of_records):
            password_choices = [fake.password(), "password","admin","123456","batman","hunter2","matlock"]
            password_choices_weights = [10,1,1,1,1,1,1]
            password_list = random.choices(password_choices, password_choices_weights)
            password = password_list[0]
            the_file.write("{},{},{}\n".format(fake.user_name(), password, fake.email()))

def ip_data(filename="example-ip-data.csv", num_of_records=1000):
    """Writes a new file with ipv4 address, user_agent, and past datetime.

    Keyword arguments:
    filename -- name of file you are writing to or overwriting (default "example-ip-data.csv)
    num_of_records -- Number of dummy records you would like the function to create (default 1000)
    """

    fake = Faker()

    with open(filename, 'w') as the_file:
        for i in range(num_of_records):
            the_file.write("{},{},{}\n".format(fake.ipv4(), fake.user_agent(), fake.past_datetime()))


def transaction_data(filename="example-bank-account-data.csv", num_of_records=1000):
    """Writes a new file with a name, company, city, and random dollar amount.

    Keyword arguments:
    filename -- name of file you are writing to or overwriting (default "example-transaction-data.csv)
    num_of_records -- Number of dummy records you would like the function to create (default 1000)
    """

    fake = Faker()

    with open(filename, 'w') as the_file:
        for i in range(num_of_records):
            multiplication_amounts = [1000, 1500, 2000, 3000, 10000, 100000, 9999999]
            multiplication_weights = [15, 12, 8, 6, 3, 2, 1]
            multiplication_amount = random.choices(multiplication_amounts, multiplication_weights)[0]
            bank_account_amount = random.random() * multiplication_amount
            the_file.write("{},{},{},${:.2f}\n".format(fake.name(), fake.company(), fake.city(), bank_account_amount))