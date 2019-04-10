
import sys


_msg = '''

--------------------------------------------------------------------------------
    WARNING: saga-python is deprecated!

    Your application will still work - but "saga-python" has been renamed to
    "radical.saga".  Please change your imports from

        import saga

    to

        import radical.saga as saga

    No other changes are needed.  This backward compatibility package will
    disappear in version 1.0, planned for end 2019.
--------------------------------------------------------------------------------

'''

sys.stderr.write(_msg)
sys.stderr.flush()


from radical.saga import *

