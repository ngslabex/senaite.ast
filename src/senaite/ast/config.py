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
# Copyright 2020 by it's authors.
# Some rights reserved, see README and LICENSE.

from senaite.ast import messageFactory as _

# Analysis Category name AST Services will be added into
SERVICE_CATEGORY = "Antibiotic Sensitivity Testing (AST)"

# Keyword of the Analysis Service to be used as the template for the creation
# of zone size (mm) results. This service is automatically created on install
# and is not editable
ZONE_SIZE_KEY = "senaite_ast_zone"

# Keyword of the Analysis Service to be used as the template for the creation
# of AST analyses. This Service is automatically created on install and is not
# editable
RESISTANCE_KEY = "senaite_ast_resistance"

# Keyword of the Analysis Service to be used as the template for the creation
# of analyses that will be used to tell whether the AST result has to be
# reported in results report or not
REPORT_KEY = "senaite_ast_report"

# Keyword of the Analysis Service for the identification of microorganisms
# This analysis service is used for the automatic selection of microorganisms
# to include in an AST testing when an AST Panel is selected. If this service
# is not present, the system assign all microorganisms from the panel
IDENTIFICATION_KEY = "senaite_ast_identification"

# Title for the AST calculation object. This calculation allows AST machinery
# to assign a final result by its own, without prompting the user
AST_CALCULATION_TITLE = "senaite_ast_autogenerated"

# Settings for analyses creation
SERVICES_SETTINGS = {

    RESISTANCE_KEY: {
        "title": "{} - Resistance",
        "choices": "0:|1:R|2:S|3:+|4:-",
    },

    ZONE_SIZE_KEY: {
        "title": "{} - Zone size (mm)",
        "size": "1",
    },

    REPORT_KEY: {
        "title": "{} - Report",
        "choices": "0:|1:Y|2:N",
        # XXX types for interims are not yet supported by senaite.app.listing
        "type": "boolean",
    },

    IDENTIFICATION_KEY: {
        "title": _("Microorganism identification"),
    }

}
