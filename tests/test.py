from django_gpxpy.gpx_parse import parse_gpx
from django.test import TestCase

class DjangoGpxPyTests(TestCase):
    def test_admin_filter_RelatedFieldRadioFilter(self):
        """
        test if the admin page with RelatedFieldRadioFilter filters loads succesfully
        """
        with open("tests/test_data/test_track.gpx", "r") as f:
            multilinestring = parse_gpx(f)
        self.assertEquals(multilinestring.num_geom, 26)
