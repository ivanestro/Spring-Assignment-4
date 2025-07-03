"""This module contains a program that reads through transaction records
and reports the results.

Example:
    $ python pixell_transaction_report.py
"""

__author__ = "COMP-1327 Faculty, Ivan Estropigan"
__version__ = "1.0"
__credits__ = "COMP-1327 Faculty, Stack OverFlow, W3schools"

# importing csv, os [clear], and logging
import csv
import os
import logging

# Checking where the errors are
# logging helps to capture severity and write LOGS.txt
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='LOGS.txt',
                    filemode='w')

# variables
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
# log the file if it opened
# FileNotFoundError: capture the error if filename does not match
try:
    with open(DATA_FILE_PATH, 'r') as csv_file:
        logging.info(f"Open the file {DATA_FILE_PATH}")
        # each row is monitored by csv.reader turns to a list
        reader = csv.reader(csv_file)

        # Skip heading line
        next(reader)

        
        for transaction in reader:
            # Adding logging.debug to read the id,type, amount
            logging.debug(f"Transaction read: {transaction}")
            # Reset valid record and error message for each iteration
            is_valid_record = True

            # Stores validation error messages
            validation_errors = []


            # Gets the customer ID from the first column
            customer_id = transaction[0]

            # Gets the transaction type from the second column
            # removes white spaces, and lowers everything
            # so no errors could cause issues.
            # store inside transaction type [1]
            transaction_type = transaction[1].strip().lower()

            ### VALIDATION 1 ###
            # if transaction type is not in valid
            # clarify if it is not [deposit]/[withdraw]
            # put it in valid_error that it is invalid
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

            #if it is valid
            if is_valid_record:
                
                # Initialize the customer's account balance if it doesn't
                # already exist in the system
                if customer_id not in customer_data:
                    customer_data[customer_id] = {'balance': 0, 'transactions': []}

                # Update the customer's account balance based on the
                # transaction type
                if transaction_type == 'deposit':
                    customer_data[customer_id]['balance'] += transaction_amount
                    transaction_count += 1
                    total_transaction_amount += transaction_amount

                # subtract transaction to total amount
                elif transaction_type == 'withdraw':
                    customer_data[customer_id]['balance'] -= transaction_amount
                    transaction_count += 1
                    total_transaction_amount += transaction_amount

                # Record transactions in the customer's transaction history
                customer_data[customer_id]['transactions'].append(
                    (transaction_amount, transaction_type))
            
            # store all the invalid transaction in a list
            # for later use
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

        # loop through each transaction from bank_data
        # amount, type, capitalize Deposit in console
        # right align 16 characters
        # right align 12 characters wide spaces
        for transaction in data['transactions']:
            amount, type = transaction
            print(f"{type.capitalize():>16}:{amount:>12}")

    # Average Transaction
    # except zero division no need for 1/0
    try:
        average_transaction_amount = total_transaction_amount / transaction_count
        print(f"\nAVERAGE TRANSACTION AMOUNT: ${average_transaction_amount:,.2f}")

    except ZeroDivisionError as exception:
        print("No valid transactions to calculate average.")

    # *lenth of the rejected_report_title
    rejected_report_title = "\nREJECTED RECORDS"
    print(rejected_report_title)
    print('=' * len(rejected_report_title))

    # Rejected transaction
    # inside the whole list for rejected transaction
    # check the rejected_transaction if it is 
    # print("REJECTED: output")
    for rejected_transaction in rejected_transactions:
            print("REJECTED:", rejected_transaction)

# except when data_filename does not match
# error saying cannot be found
except FileNotFoundError:
    print(f"The bank data file ({DATA_FILENAME}) cannot be found.")