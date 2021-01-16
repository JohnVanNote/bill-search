import sys
import zipfile
import re
from xml.dom import minidom

def main(argv):

    search_str = argv[2]

    bill_status_files = zipfile.ZipFile('billstatus_xml.zip', 'r')

    bills = list()
    for bill_status_file in bill_status_files.namelist():
                
        ## To ignore the __MACOSX files locally
        if bill_status_file.startswith("__"): 
            continue

        # Read the summaries and search
        data = bill_status_files.read(bill_status_file).decode("utf-8")
        doc = minidom.parseString(data)
        summaries_elem = doc.getElementsByTagName("summaries")
        for summary_elem in summaries_elem:
            text_elem = summary_elem.getElementsByTagName("text")
            if len(text_elem) > 0:
                text = text_elem[0].firstChild.data
                contains = re.search(search_str, text)
                if bool(contains):
                    bill_number = doc.getElementsByTagName("billNumber")[0]
                    bill_type = doc.getElementsByTagName("billType")[0]
                    bill_details = bill_type.firstChild.data + " " + bill_number.firstChild.data
                    bills.append(bill_details)

    if not bills:
        print("No results!")
    else:
        print("Found the following bills:")
        for bill in bills:
            print(bill)

if __name__ == "__main__":
    main(sys.argv)
