# makefile
#

load-requirements :
	pip3 install --user -r requirements_app.txt

run-billsearch : load-requirements
	pip3 install --user -r requirements.txt; python3 billsearch.py search "American \w+ Bureau"

run-billsearch-withbold : load-requirements 
	pip3 install --user -r requirements.txt; python3 billsearch-with-bolding.py search "American \w+ Bureau"

test : load-requirements
	rm -rf unit.xml; pip3 install --user -r requirements.txt; python3 manage.py test
