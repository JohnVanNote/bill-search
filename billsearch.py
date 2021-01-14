import sys
import zipfile
import re
from xml.dom import minidom

def main(argv):
    print(argv)
    search_str = argv[2]
    print(search_str)

    bill_status_files = zipfile.ZipFile('billstatus_xml.zip', 'r')

    bills = list()
    for bill_status_file in bill_status_files.namelist():
        data = bill_status_files.read(bill_status_file)
        data_str = str(data, 'utf-8', 'ignore')
        contains = re.search(search_str, data_str)
        if bool(contains):
            doc = minidom.parseString(data_str)
            bill_number = doc.getElementsByTagName("billNumber")[0]
            bill_type = doc.getElementsByTagName("billType")[0]
            bill_details = bill_type.firstChild.data + " " + bill_number.firstChild.data
            bills.append(bill_details)

    if not bills:
        print("No results!")
    else:
        print("Found the following bills:")
        for bill in bills:
            print(bill);

if __name__ == "__main__":
    main(sys.argv)
