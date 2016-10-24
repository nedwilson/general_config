#!/usr/bin/python

import nuke
import os
import sys

g_show_root = None
g_show_code = None
b_ih_pipeline = False
try:
    g_show_root = os.environ['IH_SHOW_ROOT']
    g_show_code = os.environ['IH_SHOW_CODE']
    if os.path.exists(g_show_root):
        b_ih_pipeline = True
        print "INFO: Show %s initialized at path %s."%(g_show_code, g_show_root)
except KeyError:
    pass
    
# separate working directory for development code
g_global_dev_pipeline = "/Volumes/raid_vol01/work/SHARED/src/nuke_hub"

if os.environ.get('NUKE_DEVEL'):
    print "INFO: DEV Mode Active."
    print "INFO: Adding plugin path: %s"%g_global_dev_pipeline
    nuke.pluginAddPath(g_global_dev_pipeline)
    
else:
    # are we running inside the in-house pipeline?
    if b_ih_pipeline:    
        g_global_root = os.path.dirname(g_show_root)
        g_global_nuke_pipeline = os.path.join(g_global_root, "SHARED", "lib", "nuke", "nuke_pipeline")
        print "INFO: Adding plugin path: %s"%g_global_nuke_pipeline
        nuke.pluginAddPath(g_global_nuke_pipeline)

# add the global gizmos directory
if b_ih_pipeline:
    g_global_gizmos = os.path.join(g_global_root, "SHARED", "lib", "nuke", "gizmos")
    print "INFO: Adding plugin path: %s"%g_global_gizmos
    nuke.pluginAddPath(g_global_gizmos)
    
# add show-specific pipeline and gizmo directories
if b_ih_pipeline:
    g_show_nuke_pipeline = os.path.join(g_show_root, "SHARED", "lib", "nuke", "nuke_pipeline")
    if os.path.exists(g_show_nuke_pipeline):
        print "INFO: Adding plugin path: %s"%g_show_nuke_pipeline
        nuke.pluginAddPath(g_show_nuke_pipeline)
    g_show_gizmos = os.path.join(g_show_root, "SHARED", "lib", "nuke", "gizmos")
    if os.path.exists(g_show_gizmos):
        print "INFO: Adding plugin path: %s"%g_show_gizmos
        nuke.pluginAddPath(g_show_gizmos)
        

# Ned Personal Customizations
nuke.knobDefault("Read.mov.decoder", "mov64")
nuke.knobDefault("Read.mov.mov64_decode_video_levels", "Video Range")
nuke.knobDefault("Viewer.frame_increment", "16")
nuke.knobDefault("RotoPaint.toolbox", "clone {{brush ltt 0} {clone ltt 0}}")  
