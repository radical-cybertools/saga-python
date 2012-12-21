# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

__author__    = "Ole Christian Weidner"
__copyright__ = "Copyright 2012, The SAGA Project"
__license__   = "MIT"

""" Unit test mock adaptor for saga.engine.engine.py
"""

from saga.utils.singleton import Singleton
import saga.cpi.base
import saga.cpi.job

_adaptor_info   = {
    'name'          : 'saga.adaptor.mock',
    'cpis'          : [
        { 
        'type'      : 'saga.job.Job',
        'class'     : 'MockJob',
        'schemas'   : ['mock']
        }
    ]
}

class Adaptor (saga.cpi.base.AdaptorBase):
    __metaclass__ = Singleton

    def __init__ (self) :

        saga.cpi.base.AdaptorBase.__init__ (self, _adaptor_info['name'], {}) 

    def register (self) :
        """ Adaptor registration function. The engine calls this during startup. 
    
            We usually do sanity checks here and throw and exception if we think
            the adaptor won't work in a given environment. In that case, the
            engine won't add it to it's internal list of adaptors. If everything
            is ok, we return the adaptor info.
        """
    
        raise Exception("CRAP! Well, actually this is supposed to happen... ;-)")


class MockJob(saga.cpi.job.Job):
    def __init__ (self, api, adaptor) :
        saga.cpi.Base.__init__ (self, api, adaptor, 'MockJob')


