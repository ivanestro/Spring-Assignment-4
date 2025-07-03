# [Assignment 4]

[Describe the tools and techniques you'll use to improve the quality of the PiXELL Transaction Report.]

For this assignment I will be using pylint and I will be reviewing pixell_transaction_report.py to ensure that we can address bugs early on.

## Author

Ivan Estropigan

## Code Modification 1

LOGGING UPDATES:

- Added: import logging, logging txt to output in LOGS.txt
- Modified: transaction_type to remove white space and transactional lowercases to capture them in lowercases.
- Added: error handling, to the data file for errors if file name is not similar to the actual file.
- Added: validation one to capture all transaction to check invalid transaction
- Modified: validation two with try and except if transaction is less than 0
- Fixed: indentation for Average
- Fixed: elif transaction_type 'withdrawal' to 'withdraw' and the subtracting values from "Deposit".
