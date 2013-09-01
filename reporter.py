from termcolor import cprint
def default(errors):
    for err in errors:
        if err[1]:
            cprint("---- " + "->".join(map(lambda x: str(x.message), err[0])) + " ----", "red")
            cprint("".join(err[1]), "grey")
        else:
            cprint("---- " + "->".join(map(lambda x: str(x.message), err[0])) + " ----")
            cprint("passed", "green")
        print("=========================================================")

def raw(errors):
    print(errors)
