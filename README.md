### Program Name: _SHA-256 Hashing_ 
### Author: _Baronia, James Scott N. and Binalla, Carmela C._ 
### Date: _2024-09-25_ 
### Version: _1.0_ 
### Purpose: _Hash the user input to show SHA-256 hashing_.

## System Requirements

### Minimum Hardware Specifications:
- **Processor:** AMD Athlon 300G or Intel Pentium equivalent.
- **Memory (RAM):** 4 GB minimum.
- **Graphics:** Integrated Graphics (iGPU) or better.
- **Storage:** Minimum 100 MB of available disk space.

### Software Specifications:
- **Operating Systems:** Compatible with Windows, macOS, and Linux.
- **Supported Browsers:** Google Chrome, Microsoft Edge, Mozilla Firefox, or other modern web browsers.


**_Made with Python and Django library installed._**

## Functional Description:  
- **Input:** The user will be asked to input a string. It could be a number or a text. Which sent to the views.py in Django.
Where it will be processed.

- **Processing:** The user inputted string will be processed using python's built in hashing library (hashlib). Which will be hashed using the SHA-256 method in hexdigest which returns the encoded data in hexadecimal format. 

- **Output:** The hashed value is then printed out in the same page in hexadecimal form.

## Security Considerations  
- **Vulnerability Assessment:** There are risk in the code where there may be a possibility of access to unhashed password. Further actions
are needed to ensure security.

- **Mitigation Strategies:** To avoid the risk mentioned, in future updates developers should look to immediately discardment of data store
in the unhashed password to avoid potential breach.  

- **Testing:** Once the security is updated, dev options should be open in the browser while the browser is open to check if the unhashed password is still visible to the viewers of the page.  

## Usage Instructions
- **Installation:**  
  Developers need to install Python and the Django library.
  
- **Configuration:**  
  Developers need to choose their preferred IDE and ensure that Python and Django are compatible with their chosen software.
  
- **Execution:**
  To run the local server, use the following steps in the command-line interface (CLI):
  
  1. Go to the project directory (where `manage.py` is located).
  2. Run the following command to start the server:
     ```bash
     python manage.py runserver
     ```
  3. After that, copy the URL provided in the CLI.  
     Example: `127.0.0.1:8000`
  4. Paste the URL in your web browser to access the application.

## Error Handling
- **Error codes:**
  _**Pending or Unapplied Migrations**_
  Running the program may encounter the error that indicates 18 pending database schema changes that needed to be applied to ensure they function properly.

- **Recovery Procedures:**
  You may run 'python manage.py migrate' to apply them. However, if the application is still running as expected, you can choose to ignore this message for now and apply the migrations later.

## Maintenance Log
- **Date:**
- **Changes:**
- **Author:** Baronia, James Scott N., Binalla, Carmela C.






