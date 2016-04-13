import os, sys
from datetime import datetime

BASE_DIR = 
ACTIVE_FILE = os.path.join(BASE_DIR, "active.tlog")
today = datetime.now()
LOG_FILE = os.path.join(BASE_DIR, "%d-%d-%d.tlog" % (today.month, today.day, today.year))

def addActivity(activity):
    """Adds the specified activity to the activity file"""
    with open(ACTIVE_FILE, "a") as f:
        f.write("%s\n" % activity)

def removeActivity(activity):
    """Removes the specified activity from activity file"""
    with open(ACTIVE_FILE, "r") as f:
        result = [line for line in f if activity not in line]

    with open(ACTIVE_FILE, "w") as f:
        for line in result:
            f.write(line)

def isIn(activity):
    """Checks to see if the activity is logged in or not"""
    try:
        with open(ACTIVE_FILE, "r") as f:
            for line in f:
                if activity in line:
                    return True
    except FileNotFoundError:
        print("Creating Activity file")

    return False

def log(in_out, activity):
    """Logs the clock in or clock out stage, and performs
    most of the logic"""
    with open(LOG_FILE, "a") as f:
        f.write("%s,%s,%s\n" %(in_out, str(today), activity))

def showList():
    """Prints a list of the active activities"""
    try:
        with open(ACTIVE_FILE, "r") as f:
            print(f.read())
    except FileNotFoundError:
        sys.exit("No activities currently logged in.")

if __name__ == "__main__":
    in_out = sys.argv[1]
    if in_out == "list":
        showList()
        sys.exit(0)
    elif in_out == "in" or in_out == "out":
        try:
            activity = sys.argv[2]
        except IndexError:
            sys.exit("No activity specified!")
    else:
        sys.exit("Use clock [in/out/list] [activity]")
    checked_in = isIn(activity)
    if in_out == "in":
        if checked_in:
            sys.exit("Can't login!  Already logged in!")
        else:
            addActivity(activity)
    elif in_out == "out":
        if not checked_in:
            sys.exit("Can't logout!  Not logged in to that activity")
        else:
            removeActivity(activity)
    log(in_out, activity)
    print("Clocked %s!" % in_out)
