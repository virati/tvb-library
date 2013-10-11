# -*- coding: utf-8 -*-
#
#
#  TheVirtualBrain-Scientific Package. This package holds all simulators, and 
# analysers necessary to run brain-simulations. You can use it stand alone or
# in conjunction with TheVirtualBrain-Framework Package. See content of the
# documentation-folder for more details. See also http://www.thevirtualbrain.org
#
# (c) 2012-2013, Baycrest Centre for Geriatric Care ("Baycrest")
#
# This program is free software; you can redistribute it and/or modify it under 
# the terms of the GNU General Public License version 2 as published by the Free
# Software Foundation. This program is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
# License for more details. You should have received a copy of the GNU General 
# Public License along with this program; if not, you can download it here
# http://www.gnu.org/licenses/old-licenses/gpl-2.0
#
#
#   CITATION:
# When using The Virtual Brain for scientific publications, please cite it as follows:
#
#   Paula Sanz Leon, Stuart A. Knock, M. Marmaduke Woodman, Lia Domide,
#   Jochen Mersmann, Anthony R. McIntosh, Viktor Jirsa (2013)
#       The Virtual Brain: a simulator of primate brain network dynamics.
#   Frontiers in Neuroinformatics (7:10. doi: 10.3389/fninf.2013.00010)
#
#

"""
The Mode Decomposition datatypes. This brings together the scientific and 
framework methods that are associated with the Mode Decomposition datatypes.

.. moduleauthor:: Stuart A. Knock <Stuart@tvb.invalid>
.. moduleauthor:: Paula Sanz Leon <paula.sanz-leon@univ-amu.fr>

"""

import tvb.datatypes.mode_decompositions_scientific as mode_decompositions_scientific
import tvb.datatypes.mode_decompositions_framework as mode_decompositions_framework
from tvb.basic.logger.builder import get_logger

LOG = get_logger(__name__)


class PrincipalComponents(mode_decompositions_scientific.PrincipalComponentsScientific,
                          mode_decompositions_framework.PrincipalComponentsFramework):
    """
    This class brings together the scientific and framework methods that are
    associated with the PrincipalComponents datatype.
    
    ::
        
                            PrincipalComponentsData
                                     |
                                    / \\
        PrincipalComponentsFramework   PrincipalComponentsScientific
                                    \ /
                                     |
                              PrincipalComponents
        
    
    """
    pass


class IndependentComponents(mode_decompositions_scientific.IndependentComponentsScientific,
                            mode_decompositions_framework.IndependentComponentsFramework):
    """
    This class brings together the scientific and framework methods that are
    associated with the IndependentComponents datatype.
    
    ::
        
                            IndependentComponentsData
                                       |
                                      / \\
        IndependentComponentsFramework   IndependentComponentsScientific
                                      \ /
                                       |
                              IndependentComponents
        
    
    """
    pass

