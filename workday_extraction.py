from requests import Session
from requests.auth import HTTPBasicAuth
import requests
import os
from dotenv import load_dotenv

class WorkdayExtraction():
    """ Description: This class allows you to download Workday reports as CSV files.
        Additional details: go to https://financialsystems.tech/articles-by-category/extracting-information-from-workday-financials-via-api/
    """

    def __init__(self) -> None:
        # loads environment variables from .env file
        load_dotenv()

        # Environment variables
        self.TENANT = os.getenv("TENANT","tenant")
        self.REPORT_OWNER = os.getenv("REPORT_OWNER", "report_owner")
        self.REPORT = os.getenv("REPORT", "report")
        self.ISU = os.getenv("ISU","isu")
        self.PASSWORD = os.getenv("PASSWORD","password")
        self.WD_URL = os.getenv("WD_URL","wd_url")

    def download_report(self, report, rep_params):
        """ Downloads a Workday report in CSV format. It requires a Integration System User (ISU) to be created and to have
            privileges for the Integration System Security Group (ISSG) required to access the information of the report. Also, the
            report should be enabled as web service and the report should be shared with the ISU.
        """

        # Workday Report WebService URL
        url = f"https://{self.WD_URL}/ccx/service/customreport2/{self.TENANT}/{self.REPORT_OWNER}/{report}?{rep_params}"

        session = Session()

        # authentication object
        session.auth = HTTPBasicAuth(username= self.ISU, password= self.PASSWORD)

        # opens a connection to the Workday webservice for the purchased items
        r = requests.get(url, auth=session.auth)
        print(r.text)

        #returns the report in CSV format
        return r.text
    
    def download_my_suppliers_report(self):
        """ Downloads the 'my_suppliers_report' created in the example.
        """

        report = "my_suppliers_report"

        # Workday ID of the supplier we pick for our test
        # Note: you can find this ID by searching for your supplier using 'Find Suppliers' command. Once you find your supplier
        # click on the related actions / Integration IDs / View IDs and you'll see a screen that shows the Workday ID string
        supplier_wid = os.getenv("SUPPLIER_WID","supplier_wid")

        # these are the parameters that come after the question mark (?) in your Workday webservice report URL
        rep_params = f"Supplier%21WID={supplier_wid}&format=csv"

        # calls Workday webservice to get the CSV version of the report
        self.download_report(report, rep_params)

if __name__ == "__main__":
    we = WorkdayExtraction()
    we.download_my_suppliers_report()



