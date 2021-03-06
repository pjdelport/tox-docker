import os
import unittest
import urllib2


class ToxDockerIntegrationTest(unittest.TestCase):
    # TODO: These tests depend too heavily on what's in tox.ini,
    # but they're better than nothing

    def test_it_sets_specific_env_vars(self):
        self.assertEqual("env-var-value", os.environ["ENV_VAR"])

    def test_it_sets_automatic_env_vars(self):
        # the nginx image we use exposes port 80
        self.assertIn("NGINX_80_TCP", os.environ)

    def test_it_exposes_the_port(self):
        # the nginx image we use exposes port 80
        url = "http://127.0.0.1:{port}/".format(port=os.environ["NGINX_80_TCP"])
        response = urllib2.urlopen(url)
        self.assertEqual(200, response.getcode())
        self.assertIn("Thank you for using nginx.", response.read())
