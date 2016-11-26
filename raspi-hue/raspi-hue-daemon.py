#!/usr/bin/env python

import sys
import os
import time
import argparse
import logging
import daemon
from daemon import pidfile

DAEMON_NAME = 'raspi-hue'

debug_p = True

def get_logger(logger_name=DAEMON_NAME):

    logger = logging.getLogger(DAEMON_NAME)
    logger.setLevel(logging.DEBUG)

    fh = logging.StreamHandler(sys.stdout)
    fh.setLevel(logging.DEBUG)

    formatstr = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(formatstr)

    fh.setFormatter(formatter)

    logger.addHandler(fh)

    return logger

def do_something():
    ### This does the "work" of the daemon

    logger = get_logger()

    while True:
        logger.debug("this is a DEBUG message")
        logger.info("this is an INFO message")
        logger.error("this is an ERROR message")
        time.sleep(5)


def start_daemon(pidf):
    ### This launches the daemon in its context

    global debug_p

    if debug_p:
        print("eg_daemon: entered run()")
        print("eg_daemon: pidf = {}".format(pidf))
        print("eg_daemon: about to start daemonization")

    try:
        with daemon.DaemonContext(
            working_directory='/var/lib/' + DAEMON_NAME,
            stdout=sys.stdout,
            stderr=sys.stderr,
            umask=0o002,
            pidfile=pidfile.TimeoutPIDLockFile(pidf),
            ) as context:
            do_something()
    except Exception as e:
        print e



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Example daemon in Python")
    parser.add_argument('-p', '--pid-file', default='/var/run/eg_daemon.pid')

    args = parser.parse_args()

    start_daemon(pidf=args.pid_file)
