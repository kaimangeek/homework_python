def f(list, format, count, object):
    if format == "center":
        format = "^"
    elif format == "left":
        format = "<"
    elif format == "right":
        format = ">"
    try:
        for i in list:
            print(("{0:" + object + format + "%s" % count + "s}").format(i))
    except:
        print("Error, come on first")


f(["x", "y", "z"], "center", 50, "-")
