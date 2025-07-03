# [Assignment 4]

[Describe the tools and techniques you'll use to improve the quality of the PiXELL Transaction Report.]

For this assignment I will be using pylint and I will be reviewing pixell_transaction_report.py to ensure that we can address bugs early on.

## Author

Ivan Estropigan

## Code Modification 1

LOGGING UPDATES:

- Added: import logging, logging txt to output in LOGS.txt

- Added: error handling, to the data file for errors if file name is not similar to the actual file, if error file cannot be found.

- Added: #validation one to capture all transaction to check invalid transaction

- Added: #Collect invalid record to store the list of valid errors.

- Modified: #validation two with try and except if transaction is less than 0
- Modified: transaction_type to remove white space and transactional lowercases to capture them in lowercases.
- Modified for rejected_transaction in rejected_transactions to only show two specific transaction output.

- Fixed: indentation for Average with the use of try and except ZeroDivisionError
- Fixed: elif transaction_type 'withdrawal' to 'withdraw' and the subtracting values from "Deposit".

## Code Modification 2

Looking through troubleshooting, data is being successfully read to customer_id, transaction type and amount.

- Added: logging to see if it aligns with customer_id, transaction_type, and amount.
- Added: bank_data.copy.csv, and added an invalid to check to see if it outputs
- Removed: inside of rejected_transaction in rejected_transaction

```cs
for rejected_transaction in rejected_transactions:
    transaction = rejected_transaction[0]
        customer_id = transaction[0]
        transaction_type = transaction[1]
        if (customer_id == 'A224' and transaction_type == 'with') or \
        (customer_id == 'A123' and transaction_type == 'asdf'):
```

This only works for the specified accounts which is why it wasn't producing an expected error inside bank_data.csv when I added an incorrect format.

## Code Modification 3

Reviewing code, and commenting

- Added: inside README the "for rejected_transaction in rejected_transactions: to make it more sense.
- Added: Adding comments to the code

[EOF]