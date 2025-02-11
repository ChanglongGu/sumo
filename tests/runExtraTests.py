#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2008-2019 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    runExtraTests.py
# @author  Michael Behrisch
# @date    2012-03-29
# @version $Id$


import optparse
import os
import subprocess
import sys
try:
    import texttestlib  # noqa
    haveTextTestLib = True
except ImportError:
    haveTextTestLib = False


def run(suffix, args, out=sys.stdout, guiTests=False, console=False, chrouter=True):
    if type(args) is list:
        args = " ".join(args)
    if os.name != "posix":
        suffix += ".exe"
    env = os.environ
    root = os.path.abspath(os.path.dirname(__file__))
    env["TEXTTEST_HOME"] = root
    env["ACTIVITYGEN_BINARY"] = os.path.join(
        root, "..", "bin", "activitygen" + suffix)
    env["DFROUTER_BINARY"] = os.path.join(
        root, "..", "bin", "dfrouter" + suffix)
    env["DUAROUTER_BINARY"] = os.path.join(
        root, "..", "bin", "duarouter" + suffix)
    env["JTRROUTER_BINARY"] = os.path.join(
        root, "..", "bin", "jtrrouter" + suffix)
    env["NETCONVERT_BINARY"] = os.path.join(
        root, "..", "bin", "netconvert" + suffix)
    env["NETEDIT_BINARY"] = os.path.join(
        root, "..", "bin", "netedit" + suffix)
    env["NETGENERATE_BINARY"] = os.path.join(
        root, "..", "bin", "netgenerate" + suffix)
    env["OD2TRIPS_BINARY"] = os.path.join(
        root, "..", "bin", "od2trips" + suffix)
    env["SUMO_BINARY"] = os.path.join(root, "..", "bin", "sumo" + suffix)
    env["POLYCONVERT_BINARY"] = os.path.join(
        root, "..", "bin", "polyconvert" + suffix)
    env["GUISIM_BINARY"] = os.path.join(root, "..", "bin", "sumo-gui" + suffix)
    env["MAROUTER_BINARY"] = os.path.join(
        root, "..", "bin", "marouter" + suffix)
    apps = "sumo.meso,sumo.ballistic,sumo.idm,sumo.sublanes,sumo.astar,sumo.parallel,netconvert.gdal,polyconvert.gdal"
    apps += ",complex.meso,duarouter.astar"
    if chrouter:
        apps += ",duarouter.chrouter"
    ttBin = 'texttest.py'
    if os.name == "posix":
        if subprocess.call(['which', 'texttest']) == 0:
            ttBin = 'texttest'
    elif haveTextTestLib:
        if console:
            ttBin = 'texttestc.py'
        else:
            ttBin += "w"
    if os.name == "nt" and subprocess.call(['where.exe', 'texttest.exe']) == 0:
        ttBin = 'texttest.exe'
    try:
        subprocess.call(['python3', '-V'])
        apps += ',complex.python3,tools.python3,complex.libsumo.python3'
    except Exception:
        pass
    if guiTests:
        apps += ",sumo.meso.gui"
    subprocess.call("%s %s -a %s" % (ttBin, args, apps), env=os.environ,
                    stdout=out, stderr=out, shell=True)


if __name__ == "__main__":
    optParser = optparse.OptionParser()
    optParser.add_option("-s", "--suffix", default="",
                         help="suffix to the fileprefix")
    optParser.add_option("-g", "--gui", default=False,
                         action="store_true", help="run gui tests")
    optParser.add_option("-c", "--console", default=False,
                         action="store_true", help="run texttest console interface")
    (options, args) = optParser.parse_args()
    run(options.suffix, ["-" + a for a in args],
        guiTests=options.gui, console=options.console)
