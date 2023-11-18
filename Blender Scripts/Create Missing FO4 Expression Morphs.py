""" Create FO4 expression morph shape keys """

import bpy
import niflytools

obj = bpy.context.object
for e in niflytools.fo4Expressions:
    if not e in obj.data.shape_keys.key_blocks:
        obj.shape_key_add(name=e)
