"""
Utilities for testing xblocks
"""
import os

from django.conf import settings

from xmodule.modulestore.tests.factories import CourseFactory, ItemFactory

TEST_DATA_DIR = settings.COMMON_ROOT / u'test/data'

def add_xml_block_from_file(block_type, filename, parent, metadata):
    with open(TEST_DATA_DIR / u'blocks' / filename) as datafile:
        return ItemFactory.create(
            parent=parent,
            category=block_type,
            data=datafile.read().decode('utf-8'),
            metadata=metadata,
            display_name=u'problem'
        )
