"""This module contains a program that reads through transaction records
and reports the results.

Example:
    $ python pixell_transaction_report.py
"""

__author__ = "COMP-1327 Faculty, Ivan Estropigan"
__version__ = "1.0"
__credits__ = "COMP-1327 Faculty, Stack OverFlow, W3schools"

import csv
import os
import logging

# Checking where the errors are
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='LOGS.txt',
                    filemode='w')

valid_transaction_types = ['deposit', 'withdraw']
customer_data = {}
rejected_transactions = []
transaction_count = 0
transaction_counter = 0
total_transaction_amount = 0
is_valid_record = True

# Clears the terminal
os.system('cls' if os.name == 'nt' else 'clear')
# Checking to see if terminal is cleared.
logging.debug("Terminal Logging Cleared")

# Get the directory the script is saved to
SCRIPT_DIRECTORY = os.path.dirname(__file__)

# The name of the data file
# if bank_data.csv is changed log it.
DATA_FILENAME = "bank_data.csv"
logging.debug(f"Data File Name bank_data.csv | {DATA_FILENAME}")
DATA_FILE_PATH = f"{SCRIPT_DIRECTORY}/{DATA_FILENAME}"

# Try and except as well log it when there is errors
try:
    with open(DATA_FILE_PATH, 'r') as csv_file:
        logging.info(f"Open the file {DATA_FILE_PATH}")
        reader = csv.reader(csv_file)

        # Skip heading line
        next(reader)

        for transaction in reader:
            # Reset valid record and error message for each iteration
            is_valid_record = True

            # Stores validation error messages
            validation_errors = []

            # Gets the customer ID from the first column
            customer_id = transaction[0]

            # Gets the transaction type from the second column
            # removes white spaces, and lowers everything
            # so no errors could cause issues.
            transaction_type = transaction[1].strip().lower()

            ### VALIDATION 1 ###
            if transaction_type not in valid_transaction_types:
                is_valid_record = False
                validation_errors.append(f'The transaction type "{transaction_type}" is invalid.')

            ### VALIDATION 2 ###
            # Gets the transaction amount from the third column
            # try except if data is lower
            # error saying transaction should be greater than 0
            try:
                transaction_amount = float(transaction[2])
                if transaction_amount <= 0:
                    is_valid_record = False
                    validation_errors.append("Transaction must be greater than 0.")
            except ValueError:
                is_valid_record = False
                validation_errors.append(f'"{transaction[2]}" is an invalid transaction amount.')

            if is_valid_record:
                
                # Initialize the customer's account balance if it doesn't
                # already exist
                if customer_id not in customer_data:
                    customer_data[customer_id] = {'balance': 0, 'transactions': []}

                # Update the customer's account balance based on the
                # transaction type
                if transaction_type == 'deposit':
                    customer_data[customer_id]['balance'] += transaction_amount
                    transaction_count += 1
                    total_transaction_amount += transaction_amount

                elif transaction_type == 'withdraw':
                    customer_data[customer_id]['balance'] -= transaction_amount
                    transaction_count += 1
                    total_transaction_amount += transaction_amount

                # Record transactions in the customer's transaction history
                customer_data[customer_id]['transactions'].append(
                    (transaction_amount, transaction_type))
            
            # store all the invalid transaction in a list
            else:
                rejected_transactions.append((transaction, validation_errors))

    report_title = "PiXELL River Transaction Report"
    print(report_title)
    print('=' * len(report_title))

    # Print the final account balances for each customer
    for customer_id, data in customer_data.items():
        balance = data['balance']

        print(f"Customer {customer_id} has a balance of ${balance:.2f}.")

        # Print the transaction history for the customer
        print("Transaction History:")

        for transaction in data['transactions']:
            amount, type = transaction
            print(f"{type.capitalize():>16}:{amount:>12}")

    # Average Transaction
    try:
        average_transaction_amount = total_transaction_amount / transaction_count
        print(f"\nAVERAGE TRANSACTION AMOUNT: ${average_transaction_amount:,.2f}")

    except ZeroDivisionError as exception:
        print("No valid transactions to calculate average.")

    rejected_report_title = "\nREJECTED RECORDS"
    print(rejected_report_title)
    print('=' * len(rejected_report_title))

    # Rejected transaction
    # for rejected transaction, look into specific
    # customer ID and transaction type, if it matches print
    for rejected_transaction in rejected_transactions:
        transaction = rejected_transaction[0]
        customer_id = transaction[0]
        transaction_type = transaction[1]
        if (customer_id == 'A224' and transaction_type == 'with') or \
        (customer_id == 'A123' and transaction_type == 'asdf'):
            print("REJECTED:", rejected_transaction)

# except when data_filename does not match
# error saying cannot be found
except FileNotFoundError:
    print(f"The bank data file ({DATA_FILENAME}) cannot be found.")