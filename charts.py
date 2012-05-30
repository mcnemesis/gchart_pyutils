from gchart_pyutils.encoding import simple_encode,extended_encode,text_encode

def make_chart(labels,values,encoder=extended_encode,ctype="p3",l=100,w=100,extra=None):
    """ Spit a Google Chart (img) based on the passed in params 
    
    Params:
    labels - list of names for each field (expect str/unicode)
    values - list of values (expect numbers)
    encoder - the desired encoder (from gchart_pyutils.encoding), default is extended_encode
    ctype - the chart type
    l - length of chart
    w - width of the chart
    extra - Any extra params as a dictionary of the param name and it's value

    Returns:
    the Chart as an HTML img tag with the necessary Chart API payload
    """
    d = {
        'chs' : "%sx%s"%(l,w),
        'chd' : encoder(values),
        'cht' : ctype,
        'chdl' : "|".join(labels)
    }
    
    d.update(extra) if isinstance(extra,dict) else None

    params = "&".join(map(lambda i: "%s=%s"%(i[0],i[1]),d.iteritems()))
    return '''<img src="https://chart.googleapis.com/chart?%s" />''' % params
