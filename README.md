# bill-search

This is a Python script that I wrote for a coding interview.

I don't have the full prompt here but the general idea is two scripts:
* `billsearch.py`
* `billsearch-withbolding.py`

Both scripts search the zip file `billstatus_xml.zip`. This zip contains XML
files with Senate Bill information. The script allows the user to search the
bill summary for a regex and returns all bills (bill type/bill name) that match
the regex.

```bash
python3 billsearch.py search "American \w+ Bureau"

Found the following bills:
SRES 39
```

`billsearch-withbolding.py` goes a step further to to not only return the bill
type and name but the summary as well with the regex that matched bolded.

```bash
python3 billsearch-with-bolding.py search "American \w+ Bureau"

Found the following bills:
SRES 39: This resolution commemorates the 100th anniversary of the **American Farm Bureau** Federation and recognizes its efforts to promote and advocate for U.S. farm and ranch interests.
```

## Requirements

The only requirements for this project should be vagrant and the vagrant
prerequisites (VirtualBox). This script can be run on the Vagrant image with
should come with Python/Pip/Django provisioned during the Vagrant up process.

The use of the Vagrant box is that whenever I installed Python 3 on my local
machine I must've messed it up, because it simply refused to work, so this
decouples my local machine from the development tasks.

### Usage

#### billsearch.py

The command utility works as such:

```bash
python3 billsearch.py search "[PUT REGEX HERE]"

# for example
python3 billsearch.py search "American \w+ Bureau"
```

This can be test via vagrant provisioner by the following:

```bash
vagrant provision --provision-with run-billsearch
```

#### billsearch-withbolding.py

The command utility works as such:

```bash
python3 billsearch-with-bolding.py search "[PUT REGEX HERE]"
# for example
python3 billsearch-with-bolding.py search "American \w+ Bureau"
```

This can be test via vagrant provisioner by the following:

```bash
vagrant provision --provision-with run-billsearch-withbold
```

### Unit Tests

The unit tests are configured and return results to `unit.xml`.

The command utility works as such:

```bash
python3 manage.py test
```

This can be test via vagrant provisioner by the following:

```bash
vagrant provision --provision-with test
```
