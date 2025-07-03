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
- Added: #Collect invalid record to store them.

- Modified: #validation two with try and except if transaction is less than 0
- Modified: transaction_type to remove white space and transactional lowercases to capture them in lowercases.
- Modified for rejected_transaction in rejected_transactions to only show two specific transaction output.

- Fixed: indentation for Average with the use of try and except ZeroDivisionError
- Fixed: elif transaction_type 'withdrawal' to 'withdraw' and the subtracting values from "Deposit".

