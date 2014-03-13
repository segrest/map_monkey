""" This is used for label expressions inside ArcGIS. 
The varibles within [brackets] should be replaced with whatever is in your data set. 
[LOCATION_DESC] can be very long. This is meant to keep your labels from being miles long.
I have the [LOCATION_DESC] set to wrap after 16 characters."""

import textwrap
def FindLabel ( [FIELD_LAB_NAME], [LOCALE_NAME], [LOCATION_DESC] ):
  return [FIELD_LAB_NAME] +  "\n"  +  [LOCALE_NAME] +  "\n"  + '\n'.join(textwrap.wrap( [LOCATION_DESC], 16))
