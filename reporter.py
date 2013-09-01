def default(errors):
    for err in errors:
        print "---- " + "->".join(map(lambda x: str(x.message), err[0])) + " ----"
        if err[1]:
            print "".join(err[1])
        else:
            print "passed"
        print "=========================================================\n"
