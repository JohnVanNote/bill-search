# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import subprocess
from django.test import SimpleTestCase


def get_search_result(search_str, with_bolding = False):
    process = subprocess.Popen(
        ["python3", "billsearch-with-bolding.py" if with_bolding else "billsearch.py", "search", search_str],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    out, err = process.communicate()
    if err:
        raise Exception(err if isinstance(err, str) else err.decode("utf-8"))
    
    out = out.replace(b"Found the following bills:", b"").split(b"\n")
    return set(filter(None, out))


class BillSearchTestCase(SimpleTestCase):
    def test_billsearch1(self):
        self.assertEqual(set([b"SRES 39"]), get_search_result("American \w+ Bureau"))

    def test_billsearch2(self):
        self.assertEqual(set([b"No results!"]), get_search_result("this search does not return any result"))

    def test_billsearch3(self):
        expected_output = [b"SRES 125", b"SRES 130", b"SRES 114", b"SRES 105", b"SRES 70", b"SRES 93", b"SRES 91", b"SRES 116", b"SRES 117", b"SRES 113", b"SRES 145", b"SRES 88", b"SRES 76", b"SRES 124"]
        self.assertEqual(set(expected_output), get_search_result("March"))

    def test_billsearch4(self):
        expected_output = [b"SRES 432", b"SRES 433", b"SRES 158", b"SRES 251", b"SRES 330", b"SRES 242", b"SRES 359", b"SRES 258", b"SRES 180", b"SRES 430", b"SRES 162", b"SRES 36", b"SRES 194", b"SRES 166", b"SRES 117", b"SRES 336", b"SRES 401", b"SRES 238", b"SRES 325", b"SRES 92", b"SRES 118", b"SRES 266", b"SRES 245", b"SRES 77", b"SRES 114", b"SRES 313", b"SRES 131", b"SRES 191", b"SRES 231", b"SRES 26", b"SRES 8", b"SRES 285", b"SRES 17", b"SRES 70", b"SRES 374", b"SRES 168", b"SRES 113", b"SRES 102", b"SRES 223", b"SRES 167", b"SRES 267", b"SRES 83", b"SRES 76", b"SRES 79", b"SRES 88", b"SRES 22", b"SRES 249", b"SRES 89", b"SRES 160", b"SRES 200", b"SRES 93", b"SRES 246", b"SRES 352", b"SRES 105", b"SRES 154", b"SRES 186", b"SRES 217", b"SRES 37", b"SRES 351", b"SRES 346", b"SRES 130", b"SRES 241", b"SRES 377", b"SRES 367", b"SRES 324", b"SRES 283", b"SRES 32", b"SRES 7", b"SRES 390", b"SRES 44", b"SRES 145", b"SRES 174", b"SRES 209", b"SRES 28", b"SRES 157", b"SRES 124", b"SRES 16", b"SRES 15", b"SRES 331", b"SRES 163", b"SRES 149", b"SRES 190", b"SRES 271", b"SRES 116", b"SRES 213", b"SRES 347", b"SRES 125", b"SRES 295", b"SRES 239", b"SRES 226", b"SRES 235", b"SRES 18", b"SRES 358", b"SRES 348", b"SRES 68", b"SRES 159", b"SRES 177", b"SRES 304", b"SRES 38", b"SRES 253", b"SRES 193", b"SRES 23", b"SRES 265", b"SRES 144", b"SRES 399", b"SRES 164", b"SRES 91", b"SRES 25", b"SRES 335", b"SRES 294"]
        self.assertEqual(set(expected_output), get_search_result("(20[0-9][0-9])"))

    def test_billsearch5(self):
        expected_output = [b"SRES 367"]
        self.assertEqual(set(expected_output), get_search_result("Ohio"))

    def test_billsearch_with_bolding(self):
        expected_output = [b"SRES 39: This resolution commemorates the 100th anniversary of the \x1b[1mAmerican Farm Bureau\x1b[0m Federation and recognizes its efforts to promote and advocate for U.S. farm and ranch interests."]
        self.assertEqual(set(expected_output), get_search_result("American \w+ Bureau", with_bolding=True))

