

# Get thresholds for beginner mode
def get_thresholds_beginner():

    # _ANGLE_HIP_KNEE_VERT = {
    #                         'NORMAL' : (0,  32),
    #                         'TRANS'  : (35, 65),
    #                         'PASS'   : (70, 95)
    #                        }    

        
    thresholds = {
                    'HIP_KNEE_VERT': [160,190],

                    'HIP_THRESH'   : [160,190],
                    'ANKLE_THRESH' : [80,100],
                    'KNEE_THRESH'  : [50, 70, 95],

                    'OFFSET_THRESH'    : 35.0,
                    'INACTIVE_THRESH'  : 15.0,

                    'CNT_FRAME_THRESH' : 50
                            
                }

    return thresholds



# Get thresholds for beginner mode
def get_thresholds_pro():

    # _ANGLE_HIP_KNEE_VERT = {
    #                         'NORMAL' : (0,  32),
    #                         'TRANS'  : (35, 65),
    #                         'PASS'   : (80, 95)
    #                        }    

        
    thresholds = {
                    'HIP_KNEE_VERT':[170,185],

                    'HIP_THRESH'   : [170,185],
                    'ANKLE_THRESH' : 90,
                    'KNEE_THRESH'  : [50, 80, 95],

                    'OFFSET_THRESH'    : 35.0,
                    'INACTIVE_THRESH'  : 15.0,

                    'CNT_FRAME_THRESH' : 50
                            
                 }
                 
    return thresholds