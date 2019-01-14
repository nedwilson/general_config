import hiero.core
import hiero.ui
import os
import sys

g_show_root = None
g_show_code = None
g_global_root = None
g_global_hiero_pipeline = None
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
    # g_global_root = os.path.dirname(g_show_root)
    g_global_hiero_pipeline = os.path.join(g_show_root, "SHARED", "lib", "nuke", "hiero")
    print "INFO: Adding plugin path: %s"%g_global_hiero_pipeline
    hiero.core.addPluginPath(g_global_hiero_pipeline)

