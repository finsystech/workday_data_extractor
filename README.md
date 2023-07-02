# Workday Data Extractor

Website: http://financialsystems.tech

GitHub: https://github.com/finsystech/workday_data_extractor.git



## Description ##

This application allows you to extract and download information from the Workday ERP by creating a report, enabling it as a web service in CSV format and downloading it with this script.

For step-by-step process, visit this website: https://financialsystems.tech/articles-by-category/extracting-information-from-workday-financials-via-api/

If you have questions, send a message in Twitter @FinSysTech. We will do our best to help.

## Installation Instructions ##

**Optional**: We recommend that you create a virtual environment for this application, but you can install everything directly in your computer (not recommended)

```
    # if you don't have virtualenv installed
    $ pip install virtualenv

    # once installed, create a virtual environment
    $ install python -m virtualenv venv

    # activate it with Windows. Locate in the folder that contains the 'venv' folder
    $ venv\Scripts\activate
```

You should see the (env) suffix in your prompt, indicating you activated successfully the virtual enviornment. Now, install the Python libraries (dependencies) needed for the app to run:

```
    # ensure to be located in the folder that contains 'requirements.txt'
    $ pip install -r requirements.txt
```

Create an '.env' file in the same folder as the application. This .env file contains all of the secret/sensitive information specific for your Workday tenant. The file structure should be as shown below. Replace the values specific to your report and tenants as needed. Remember NOT to use quotes or single quotes for the strings and NOT to leave spaces before or after the equal sign.

```
    ISU=my_isu
    PASSWORD=<whatever password you selected>
    TENANT=<Workay tenant for your company>
    REPORT_OWNER=<user id of whoever created the report>
    REPORT=my_suppliers_report
    WD_URL=wd3-impl-services1.workday.com
    SUPPLIER_WID=<workday ID of the supplier you want to use four our test report>
```

Once you have created this .env folder, and you have activated the virual environment (or installed the libraries direclty in your computer if you did not go with the recommended virutal environment), you are ready to run the app.