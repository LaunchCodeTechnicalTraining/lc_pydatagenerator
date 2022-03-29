from generate_random import generate_random_user_data
from generate_random import generate_random_sensitive_user_data
from generate_random import generate_random_ip_data
from generate_random import generate_random_transaction_data

# Todo, Tests and mutations

if __name__ == "__main__":

    generate_random_user_data("dummy-user-data.csv", 25000)

    generate_random_ip_data("dummy-ip-data.csv", 25000)

    generate_random_sensitive_user_data("dummy-sensitive-user-data.csv", 25000)

    generate_random_transaction_data("dummy-transaction-data.csv", 25000)
