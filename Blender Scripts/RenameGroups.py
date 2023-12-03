import bpy

skyrimGroups = 1

name_list = [
# old name - new name
('NPC Calf [Clf].L','NPC L Calf [LClf]'),
('NPC Calf [Clf].R','NPC R Calf [RClf]'),
('NPC Clavicle [Clv].L', 'NPC L Clavicle [LClv]'),
('NPC Clavicle [Clv].R', 'NPC R Clavicle [RClv]'),
('NPC Finger00 [F00].L', 'NPC L Finger00 [LF00]'),
('NPC Finger00 [F00].R', 'NPC R Finger00 [RF00]'),
('NPC Finger01 [F01].L', 'NPC L Finger01 [LF01]'),
('NPC Finger01 [F01].R', 'NPC R Finger01 [RF01]'),
('NPC Finger02 [F02].L', 'NPC L Finger02 [LF02]'),
('NPC Finger02 [F02].R', 'NPC R Finger02 [RF02]'),
('NPC Finger10 [F10].L', 'NPC L Finger10 [LF10]'),
('NPC Finger10 [F10].R', 'NPC R Finger10 [RF10]'),
('NPC Finger11 [F11].L', 'NPC L Finger11 [LF11]'),
('NPC Finger11 [F11].R', 'NPC R Finger11 [RF11]'),
('NPC Finger12 [F12].L', 'NPC L Finger12 [LF12]'),
('NPC Finger12 [F12].R', 'NPC R Finger12 [RF12]'),
('NPC Finger20 [F20].L', 'NPC L Finger20 [LF20]'),
('NPC Finger20 [F20].R', 'NPC R Finger20 [RF20]'),
('NPC Finger21 [F21].L', 'NPC L Finger21 [LF21]'),
('NPC Finger21 [F21].R', 'NPC R Finger21 [RF21]'),
('NPC Finger22 [F22].L', 'NPC L Finger22 [LF22]'),
('NPC Finger22 [F22].R', 'NPC R Finger22 [RF22]'),
('NPC Finger30 [F30].L', 'NPC L Finger30 [LF30]'),
('NPC Finger30 [F30].R', 'NPC R Finger30 [RF30]'),
('NPC Finger31 [F31].L', 'NPC L Finger31 [LF31]'),
('NPC Finger31 [F31].R', 'NPC R Finger31 [RF31]'),
('NPC Finger32 [F32].L', 'NPC L Finger32 [LF32]'),
('NPC Finger32 [F32].R', 'NPC R Finger32 [RF32]'),
('NPC Finger40 [F40].L', 'NPC L Finger40 [LF40]'),
('NPC Finger40 [F40].R', 'NPC R Finger40 [RF40]'),
('NPC Finger41 [F41].L', 'NPC L Finger41 [LF41]'),
('NPC Finger41 [F41].R', 'NPC R Finger41 [RF41]'),
('NPC Finger42 [F42].L', 'NPC L Finger42 [LF42]'),
('NPC Finger42 [F42].R', 'NPC R Finger42 [RF42]'),
('NPC Foot [ft ].L','NPC L Foot [Lft ]'),
('NPC Foot [ft ].R','NPC R Foot [Rft ]'),
('NPC Forearm [Lar].R', 'NPC R Forearm [RLar]'),
('NPC Forearm [Lar].L', 'NPC L Forearm [LLar]'),
('NPC ForearmTwist1 [Lt1].L', 'NPC L ForearmTwist1 [LLt1]'),
('NPC ForearmTwist1 [Lt1].R', 'NPC R ForearmTwist1 [RLt1]'),
('NPC ForearmTwist2 [Lt2].L', 'NPC L ForearmTwist2 [LLt2]'),
('NPC ForearmTwist2 [Lt2].R', 'NPC R ForearmTwist2 [RLt2]'),
('NPC Hand [Hnd].L', 'NPC L Hand [LHnd]'),
('NPC Hand [Hnd].R', 'NPC R Hand [RHnd]'),
('NPC Thigh [Thg].L', 'NPC L Thigh [LThg]'),
('NPC Thigh [Thg].R', 'NPC R Thigh [RThg]'),
('NPC Toe0 [Toe].L','NPC L Toe0 [LToe]'),
('NPC Toe0 [Toe].R','NPC R Toe0 [RToe]'),
('NPC UpperArm [Uar].L', 'NPC L UpperArm [LUar]'),
('NPC UpperArm [Uar].R', 'NPC R UpperArm [RUar]'),
('NPC UpperarmTwist1 [Ut1].L', 'NPC L UpperarmTwist1 [LUt1]'),
('NPC UpperarmTwist1 [Ut1].R', 'NPC R UpperarmTwist1 [RUt1]'),
('NPC UpperarmTwist2 [Ut2].L', 'NPC L UpperarmTwist2 [LUt2]'),
('NPC UpperarmTwist2 [Ut2].R', 'NPC R UpperarmTwist2 [RUt2]')
]

v_groups = bpy.context.active_object.vertex_groups
for old_name, new_name in name_list:
    if old_name in v_groups:
        v_groups[old_name].name = new_name
    elif new_name in v_groups:
        v_groups[new_name].name = old_name
print('done')