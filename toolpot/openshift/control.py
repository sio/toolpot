"""
Control Openshift2 cartridges
"""


from subprocess import Popen, PIPE, STDOUT


def control(action, wait=True):
    """Control Openshift instance (primary cartridge)"""
    command_line = ["control", str(action)]
    process = Popen(command_line)
    if wait: process.wait()
    exit_code = process.returncode
    if exit_code:
        raise RuntimeError("control returned exit code %s" % exit_code)


def control_isrunning():
    """Check if OpenShift primary cartridge is running"""
    REPLY_HEADER = "CLIENT_RESULT:"
    REPLY_OK = "Application is running"

    command_line = ["control", "status"]
    check = Popen(command_line,
                  stdout=PIPE,
                  stderr=STDOUT,
                  universal_newlines=True)
    exit_code = check.wait()
    reply = check.stdout.read()
    if exit_code:
        error_description = "\n".join((
            "status check failed (exit code: %s)" % exit_code,
            "Control output:",
            reply or "<empty>",
            ))
        raise RuntimeError(error_description)
    elif REPLY_HEADER in reply:
        return REPLY_OK in reply
    else:
        raise RuntimeError("unexpected control output:\n%s" % reply)
