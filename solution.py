def rgb(r, g, b):
    #your code here :)
    rgbTest = [r, g, b]
    hexMatch = {10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
    result = ""
    
    
    for color in rgbTest:
        # Check if within range 0-255 and reintialize to min or max value
        if color > 255:
            color = 255
        if color < 0:
            color = 0;
        
        Div1 = int(color/16)
        # print(Div1) ----> used for testing hex conversion
        Div2 = int(color % 16)
        # print(Div2) ----> used for testing hex conversion
        
        # Probably redundant and can be shortened
        if Div1 < 10:
            result = result + str(Div1)
        else:
            for code in hexMatch.keys():
                if Div1 == code:
                    result = result + hexMatch[code]
                    
        if Div2 < 10:
            result = result + str(Div2)
        else:
            for code in hexMatch.keys():
                if Div2 == code:
                    result = result + hexMatch[code]
    return result
