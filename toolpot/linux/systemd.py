"""
Control daemons with systemctl
"""


from subprocess import Popen, PIPE, STDOUT


def control(daemon, action, wait=True, sudo=True):
    """Control a daemon with systemctl"""
    command_line = []
    if sudo: command_line.append("sudo")
    command_line += ["systemctl", str(action), str(daemon)]

    process = Popen(command_line,
                    stdout=PIPE,
                    stderr=STDOUT,
                    universal_newlines=True)
    if wait:
        exit_code = process.wait()
        reply = process.stdout.read()
    else:
        exit_code = 0
        reply = ""
    if exit_code:
        error_description = "\n".join((
            "systemctl failed (exit code: %s)" % exit_code,
            "Standard output:",
            reply or "<empty>",
            ))
        raise RuntimeError(error_description)
    return exit_code, reply


def control_isrunning(daemon, sudo=True):
    """Check if a daemon is running"""
    REPLY_HEADER = "%s.service" % daemon
    REPLY_OK = "active (running)"

    try:
        exit_code, reply = control(daemon, "status", sudo=sudo)
    except RuntimeError as e:
        return False  # systemctl returns exit code 3 for stopped service
    if REPLY_HEADER in reply:
        return REPLY_OK in reply
    else:
        raise RuntimeError("unexpected systemctl output:\n%s" % reply)
