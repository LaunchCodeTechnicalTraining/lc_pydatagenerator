# we need a tool that will generate the junk data we provide in the userspace application segment.

# Tool should generate:
# - CSV with random user data
# - first_name, last_name, address, company, title, salary
# - username, email, password_hash, account_type
# - CSV with random transaction data
# - business_name, amount, date, category
# - random IP log data (.log)
# - Webserver log output
# - Caddy
#   127.0.0.1 - - [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.1" 200 2326
# - NGINX
'''
    TLSv1.2 AES128-SHA 1.1.1.1 "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"
    TLSv1.2 ECDHE-RSA-AES128-GCM-SHA256 2.2.2.2 "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
    TLSv1.2 ECDHE-RSA-AES128-GCM-SHA256 3.3.3.3 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:58.0) Gecko/20100101 Firefox/58.0"
    TLSv1.2 ECDHE-RSA-AES128-GCM-SHA256 4.4.4.4 "Mozilla/5.0 (Android 4.4.2; Tablet; rv:65.0) Gecko/65.0 Firefox/65.0"
    TLSv1 AES128-SHA 5.5.5.5 "Mozilla/5.0 (Android 4.4.2; Tablet; rv:65.0) Gecko/65.0 Firefox/65.0"
    TLSv1.2 ECDHE-RSA-CHACHA20-POLY1305 6.6.6.6 "Mozilla/5.0 (Linux; U; Android 5.0.2; en-US; XT1068 Build/LXB22.46-28) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.2.1164 Mobile Safari/537.36"
'''
# - Apache
#   [Fri Sep 09 10:42:29.902022 2011] [core:error] [pid 35708:tid 4328636416] [client 72.15.99.187] File does not exist: /usr/local/apache2/htdocs/favicon.ico 
# - SSH?
'''
from cat /var/log/auth.log | grep "sshd"
    Mar 23 20:51:17 ubuntu-s-1vcpu-1gb-nyc1-01 sshd[1185887]: Accepted publickey for root from 71.11.136.98 port 48122 ssh2: RSA SHA256:ctJDIOCeFq4xG1/j1QFdvdOpJggwNM7YL0Uqqe9PeRo
    Mar 23 20:51:17 ubuntu-s-1vcpu-1gb-nyc1-01 sshd[1185887]: pam_unix(sshd:session): session opened for user root by (uid=0)
    Mar 23 20:52:03 ubuntu-s-1vcpu-1gb-nyc1-01 sshd[1185887]: Received disconnect from 71.11.136.98 port 48122:11: disconnected by user
    Mar 23 20:52:03 ubuntu-s-1vcpu-1gb-nyc1-01 sshd[1185887]: Disconnected from user root 71.11.136.98 port 48122
    Mar 23 20:52:03 ubuntu-s-1vcpu-1gb-nyc1-01 sshd[1185887]: pam_unix(sshd:session): session closed for user root
    Mar 23 20:52:27 ubuntu-s-1vcpu-1gb-nyc1-01 sshd[1186026]: Accepted publickey for root from 71.11.136.98 port 48124 ssh2: RSA SHA256:ctJDIOCeFq4xG1/j1QFdvdOpJggwNM7YL0Uqqe9PeRo
    Mar 23 20:52:27 ubuntu-s-1vcpu-1gb-nyc1-01 sshd[1186026]: pam_unix(sshd:session): session opened for user root by (uid=0)
    Mar 23 20:52:46 ubuntu-s-1vcpu-1gb-nyc1-01 sshd[1186113]: Invalid user intro from 13.71.46.226 port 1024
    Mar 23 20:52:46 ubuntu-s-1vcpu-1gb-nyc1-01 sshd[1186113]: Received disconnect from 13.71.46.226 port 1024:11: Bye Bye [preauth]
    Mar 23 20:52:46 ubuntu-s-1vcpu-1gb-nyc1-01 sshd[1186113]: Disconnected from invalid user intro 13.71.46.226 port 1024 [preauth]
    Mar 23 20:53:04 ubuntu-s-1vcpu-1gb-nyc1-01 sshd[1186117]: Connection closed by authenticating user root 69.222.176.76 port 55498 [preauth]  
'''

''' major things we need to accomplish
  - generate random data in various formats
    - [x] how do we generate any random data? POC --> Faker
    - [x] how do we generate specific random data? POC
  - write out to a file
    - [x] how do we write data to a file
        - io
'''
from faker import Faker
from random import randint

# Writes a new file with first_name, last_name, email, and company

def generate_random_user_data(faker_object, filename="example-user-data.csv", num_of_records=1000):
    with open(filename, 'w') as the_file:
        for i in range(num_of_records):
            the_file.write("{},{},{},{}\n".format(fake.first_name(), fake.last_name(), fake.email(), fake.company()))

# Writes a new file with timestamps, method, path, ip address

def generate_random_ip_data(faker_object, filename="example-ip-data.csv", num_of_records=1000):
    with open(filename, 'w') as the_file:
        for i in range(num_of_records):
            the_file.write("{},{},{}\n".format(fake.ipv4(), fake.user_agent(), fake.past_datetime()))

# def generate_random_log_data(faker_object, filename="example-log-data.csv", num_of_records=1000):
#     with open(filename, 'w') as the_file:
#         for i in range(num_of_records):
#             the_file.write("{},{},{},{}\n".format(fake.first_name(), fake.last_name(), fake.email(), fake.company()))

# Writes a new file with username, password, email address

def generate_sensitive_user_data(faker_object, filename="example-sensitive-user-data.csv", num_of_records=1000):
    with open(filename, 'w') as the_file:
        for i in range(num_of_records):
            the_file.write("{},{},{}\n".format(fake.user_name, fake.password(), fake.email()))

# Writes a new file with bank account #, account holder, money held, bank name

def generate_random_bank_account_data(faker_object, filename="example-bank-account-data.csv", num_of_records=1000):
    with open(filename, 'w') as the_file:
        for i in range(num_of_records):
            the_file.write("{},{},{},{}\n".format(fake.name(), fake.company(), fake.city(), randint(10000000, 999999999)))

# Writes a file with for example: Mozilla/5.0 (iPad; CPU iPad OS 14_2 like Mac OS X) AppleWebKit/533.1 (KHTML, like Gecko) FxiOS/16.1d3721.0 Mobile/94R243 Safari/533.1

# def generate_random_user_agent(faker_object, filename="example-user-agent.csv", num_of_records=1000):
#     with open(filename, 'w') as the_file:
#         for i in range(num_of_records):
#             the_file.write("{},{},{},{}\n".format(fake.user_agent()))



if __name__ == "__main__":

    fake = Faker()

    generate_random_user_data(fake, "dummy-user-data2.csv", 25000)

    generate_random_ip_data(fake, "dummy-ip-data.csv", 25000)

    generate_sensitive_user_data(fake, "dummy-sensitive-user-data.csv", 25000)

    generate_random_bank_account_data(fake, "dummy-bank-account-data.csv", 25000)



    

    # print("state: {}".format(fake.state()))
    # print("first_name: {}".format(fake.first_name()))
    # print("last_name: {}".format(fake.last_name()))
    # print("Mac address: {}".format(fake.mac_address()))
    # print("Secondary Address: {}".format(fake.secondary_address()))
    # print("Street Address: {}".format(fake.street_address()))
    # print("Ascii Company Email: {}".format(fake.ascii_company_email()))
    # print("Email: {}".format(fake.ascii_email()))
    # print("Company: {}".format(fake.company()))
    # print("Company_Email: {}".format(fake.company_email()))
    # print("Company_Suffix: {}".format(fake.company_suffix()))
    # print("Job: {}".format(fake.job()))
    # print("User Agent: {}".format(fake.user_agent()))
    # print("User Name: {}".format(fake.user_name()))
    # print("Phone Number: {}".format(fake.phone_number()))
    # print("Zipcode: {}".format(fake.zipcode()))
    # print("Linux Processor: {}".format(fake.linux_processor()))
    # print("Postcode: {}".format(fake.postcode()))
    # print("Sha256: {}".format(fake.sha256()))
    # print("SSN: {}".format(fake.ssn()))
    # print("Paragraph: {}".format(fake.paragraph()))
    # print("Paragraphs: {}".format(fake.paragraphs()))
    # print("Mine Type: {}".format(fake.mime_type()))
    # print("Port Number: {}".format(fake.port_number()))
    # print("Datetime: {}".format(fake.past_datetime()))
    # print("Past Date: {}".format(fake.past_date()))
    # print("Random Letter: {}".format(fake.random_letter()))
    # print("Country: {}".format(fake.country()))
    # print("CC Number: {}".format(fake.credit_card_number()))
    # print("CC Provider: {}".format(fake.credit_card_provider()))
    # print("Safe Domain Name: {}".format(fake.safe_domain_name()))
    # print("Coordinate: {}".format(fake.coordinate()))
    # print("Password: {}".format(fake.password()))
    # print("Currency: {}".format(fake.currency()))
    # print("Currency Code: {}".format(fake.currency_code()))
    # print("CSV: {}".format(fake.csv()))
    # print("TSV: {}".format(fake.tsv()))
    # print("City: {}".format(fake.city()))
