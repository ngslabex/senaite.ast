# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.AST.
#
# SENAITE.AST is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright 2020-2025 by it's authors.
# Some rights reserved, see README and LICENSE.

import transaction
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.testing import zope
from senaite.core.tests.base import BaseTestCase
from senaite.core.tests.layers import BaseLayer


class SimpleTestLayer(BaseLayer):

    def setUpZope(self, app, configurationContext):
        super(SimpleTestLayer, self).setUpZope(app, configurationContext)

        # Load ZCML
        import senaite.abx
        import senaite.microorganism
        self.loadZCML(package=senaite.abx)
        self.loadZCML(package=senaite.microorganism)
        self.loadZCML(package=senaite.ast)

        # Install product and call its initialize() function
        zope.installProduct(app, "senaite.abx")
        zope.installProduct(app, "senaite.microorganism")
        zope.installProduct(app, "senaite.ast")

    def setUpPloneSite(self, portal):
        super(SimpleTestLayer, self).setUpPloneSite(portal)
        applyProfile(portal, "senaite.ast:default")
        transaction.commit()


SIMPLE_TEST_LAYER_FIXTURE = SimpleTestLayer()
SIMPLE_TESTING = FunctionalTesting(
    bases=(SIMPLE_TEST_LAYER_FIXTURE, ),
    name="senaite.ast:SimpleTesting"
)


class SimpleTestCase(BaseTestCase):
    """Use for test cases which do not rely on demo data
    """
    layer = SIMPLE_TESTING
