import pytest
import unittest
import argparse
from mypkg.scc import SiteChecker, Factory

class ParserTest(unittest.TestCase):
    def setUp(self):
        self.parser = Factory().create_parser()

    # def test_case1(self):
    #     # args.host_name = "www.zidong.us"
    #     args = self.parser.parse_args(["-hn", "www.zidong.us"])
    #
    #     res = "200 OK"
    #     assert(res != SiteChecker(args).scc())

    def test_case2(self):
        args = self.parser.parse_args(["-hn", "www.google.com"])

        res = "200 OK"
        assert(res == SiteChecker(args).scc())
    
    def test_case3(self):
        args = self.parser.parse_args(["-hn", "www.youtube.com"])

        res = "200 OK"
        assert(res == SiteChecker(args).scc())
