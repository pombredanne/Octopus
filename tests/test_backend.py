# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 Bitergia
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# Authors:
#     Santiago Dueñas <sduenas@bitergia.com>
#

import sys
import unittest

if not '..' in sys.path:
    sys.path.insert(0, '..')

from octopus.backends import Backend, ProjectsIterator, ReleasesIterator


# Backends for unit tests
class FakeBackend(Backend):

    def __init__(self):
        super(FakeBackend, self).__init__('FakeBackend')


class UnnamedBackend(Backend):

    def __init__(self):
        super(UnnamedBackend, self).__init__()


class TestBackend(unittest.TestCase):

    def test_backend(self):
        backend = FakeBackend()
        self.assertEqual('FakeBackend', backend.name)

    def test_unnamed_backend(self):
        self.assertRaises(TypeError, UnnamedBackend)

    def test_readonly_properties(self):
        backend = FakeBackend()
        self.assertRaises(AttributeError, setattr, backend, 'name', 'ErrorName')
        self.assertEqual('FakeBackend', backend.name)


class TestProjectsIterator(unittest.TestCase):

    def test_is_iterable(self):
        import collections
        iterator = ProjectsIterator()
        self.assertIsInstance(iterator, collections.Iterable)


class TestReleasesIterator(unittest.TestCase):

    def test_is_iterable(self):
        import collections
        iterator = ReleasesIterator()
        self.assertIsInstance(iterator, collections.Iterable)


if __name__ == "__main__":
    unittest.main()
