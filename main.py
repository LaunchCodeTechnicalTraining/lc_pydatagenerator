from generate_random import user_data, ip_data, sensitive_user_data, transaction_data

if __name__ == "__main__":

    user_data("dummy-user-data.csv", 25000)

    ip_data("dummy-ip-data.csv", 25000)

    sensitive_user_data("dummy-sensitive-user-data.csv", 25000)

    transaction_data("dummy-transaction-data.csv", 25000)