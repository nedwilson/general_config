#!/usr/bin/python

import nuke
import os
import sys
import timeit

g_show_root = None
g_show_code = None
g_global_root = None
g_global_nuke_pipeline = None
g_global_gizmos = None
b_ih_pipeline = False
try:
    g_show_root = os.environ['IH_SHOW_ROOT']
    g_show_code = os.environ['IH_SHOW_CODE']
    if os.path.exists(g_show_root):
        b_ih_pipeline = True
        print "INFO: Show %s initialized at path %s."%(g_show_code, g_show_root)
except KeyError:
    pass

if b_ih_pipeline:
    g_global_root = os.path.dirname(g_show_root)
    g_global_nuke_pipeline = os.path.join(g_global_root, "SHARED", "lib", "nuke", "pipeline")
    g_global_gizmos = os.path.join(g_global_root, "SHARED", "lib", "nuke", "gizmos")
    g_show_nuke_pipeline = os.path.join(g_show_root, "SHARED", "lib", "nuke", "pipeline")
    g_show_gizmos = os.path.join(g_show_root, "SHARED", "lib", "nuke", "gizmos")
else:
    print "WARNING: Nuke is not operating inside an In-House Pipeline. Most likely this is due to environment variables not being configured."
    for envkey in sorted(os.environ.keys()):
        print "%s : %s"%(envkey, os.environ[envkey])

def load_global_np():
    nuke.pluginAddPath(g_global_nuke_pipeline)
def load_global_gizmos():
    nuke.pluginAddPath(g_global_gizmos)
def load_show_np():
    nuke.pluginAddPath(g_show_nuke_pipeline)
def load_show_gizmos():
    nuke.pluginAddPath(g_show_gizmos)


# separate working directory for development code
g_global_dev_pipeline = "/Volumes/raid_vol01/shows/SHARED/src/nuke_hub"

if os.environ.get('NUKE_DEVEL'):
    print "INFO: DEV Mode Active."
    print "INFO: Adding plugin path: %s"%g_global_dev_pipeline
    nuke.pluginAddPath(g_global_dev_pipeline)
    
else:
    # are we running inside the in-house pipeline?
    if b_ih_pipeline:    
        print "INFO: Adding plugin path: %s"%g_global_nuke_pipeline
        rval = timeit.timeit(load_global_np, number=100)
        print rval

# add the global gizmos directory
if b_ih_pipeline:
    print "INFO: Adding plugin path: %s"%g_global_gizmos
    rval = timeit.timeit(load_global_gizmos, number=100)
    print rval

# add show-specific pipeline and gizmo directories
if b_ih_pipeline:
    if os.path.exists(g_show_nuke_pipeline):
        print "INFO: Adding plugin path: %s"%g_show_nuke_pipeline
        rval = timeit.timeit(load_show_np, number=100)
        print rval
    if os.path.exists(g_show_gizmos):
        print "INFO: Adding plugin path: %s"%g_show_gizmos
        rval = timeit.timeit(load_show_gizmos, number=100)
        print rval 

# Ned Personal Customizations
nuke.knobDefault("Read.mov.decoder", "mov64")
nuke.knobDefault("Read.mov.mov64_decode_video_levels", "Video Range")
