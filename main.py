from generate_random import user_data
from generate_random import sensitive_user_data
from generate_random import ip_data
from generate_random import transaction_data

# Todo, Tests and mutations

if __name__ == "__main__":

    user_data("dummy-user-data.csv", 25000)

    ip_data("dummy-ip-data.csv", 25000)

    sensitive_user_data("dummy-sensitive-user-data.csv", 25000)

    transaction_data("dummy-transaction-data.csv", 25000)
