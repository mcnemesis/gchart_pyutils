from math import floor

def simple_encode(values,max_value=None):
    max_value = max(values) if max_value is None else max_value
    simple_encoding = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    chart_data = ['s:']
    for i in range(len(values)):
        current_value = values[i]
        if (isinstance(current_value,int) or isinstance(current_value,float)) and current_value >= 0:
            chart_data.append(simple_encoding[int(round((len(simple_encoding)-1) * current_value / max_value))])
        else:
            chart_data.append('_')
    return ''.join(chart_data)

def extended_encode(values, max_value=None):
    max_value = max(values) if max_value is None else max_value
    #Same as simple encoding, but for extended encoding.
    EXTENDED_MAP= 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-.'
    EXTENDED_MAP_LENGTH = len(EXTENDED_MAP)
    chart_data = 'e:'
    for i in range(len(values)):
        #In case the array vals were translated to strings.
        numeric_val = float(values[i])
        #Scale the value to max_value.
        scaled_value = floor(EXTENDED_MAP_LENGTH * EXTENDED_MAP_LENGTH * numeric_val / max_value)

        if(scaled_value > (EXTENDED_MAP_LENGTH * EXTENDED_MAP_LENGTH) - 1):
          chart_data += ".."
        elif (scaled_value < 0):
          chart_data += '__'
        else:
          #Calculate first and second digits and add them to the output.
          quotient = floor(scaled_value / EXTENDED_MAP_LENGTH)
          remainder = int(scaled_value - EXTENDED_MAP_LENGTH * quotient)
          chart_data += EXTENDED_MAP[int(quotient)] + EXTENDED_MAP[remainder]

    return chart_data

def text_encode(values):
    return "t:%s" % ",".join(map(str,values))

