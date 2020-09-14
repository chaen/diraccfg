from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import re


def parseVersion(versionString):
  """Parse a DIRAC-style version sting
  """
  match = re.match(
      r"^v(?P<major>\d+)r(?P<minor>\d+)(?:p(?P<patch>\d+))?(?:-pre(?P<pre>\d+))?$",
      versionString,
  )
  if not match:
    raise ValueError("%s is not a valid version" % versionString)

  segments = match.groupdict()
  for k, v in segments.items():
    if k != "pre" and v is None:
      segments[k] = 0
    if v is not None:
      segments[k] = int(v)

  return (segments["major"], segments["minor"], segments["patch"], segments["pre"])
