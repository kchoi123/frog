#!/usr/bin/env python3

import os
import sys
import argparse
import subprocess

class jfrog(object):

    """
    CLI for jfrog technical evaluation
    """

    def __init__(self):
        parser = argparse.ArgumentParser(
            description  = 'main script for python',
            usage = '''python3 jfrog.py [<cmd>]
            \nAvailable Comands:
                build           Build docker images and create temp image in Jfrog Artifactory
                clean           Clean your docker environment for clean install
                deploy          Docker-compose Jfrog technical evaluation
                destroy         Destroy docker-compose ['down']
            ''')

        parser.add_argument('command')

        # print("print", sys.argv[1:2])
        # output is: print ['clean']

        args = parser.parse_args(sys.argv[1:2])
        # print(args)
        # output is: Namespace(command='clean')

        # Invalid command clause
        if not hasattr(self, args.command):
            print('Unauthorized command')
            parser.print_help()
            exit(1)

        # move to function build, clean, ...
        getattr(self, args.command)()

    def build(self):
        print("Always run this python script indside scripts directory, please!")

        buildBashCommand = "bash ./build.sh"

        # testing the relative path
        # process = subprocess.Popen(["ls"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        with open ('../tmp/build_stdout.txt', 'w') as f: # This can be output for splunk, nr logging, etc
            process = subprocess.Popen(buildBashCommand.split(), stdout=f, stderr=subprocess.DEVNULL) # We can change DEVNULL to PIPE for errors
            result = process.communicate()

            print("BUILD is finished. stderr is: ", result)

    def clean(self):
        print("Always run this python script indside scripts directory, please!")

        cleanBashCommand = "bash ./clean_start.sh"

        # testing the relative path
        # process = subprocess.Popen(["ls"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        with open ('../tmp/clean_stdout.txt', 'w') as f: # This can be output for splunk, nr logging, etc
            process = subprocess.Popen(cleanBashCommand.split(), stdout=f, stderr=subprocess.DEVNULL) # We can change DEVNULL to PIPE for errors
            result = process.communicate()

            print("CLEAN is finished. stderr is: ", result)

    def deploy(self):
        print("This is going to deploy using docker-compose")

        deployBashCommand = "docker-compose -f ../docker-compose.yml up -d"

        with open ('../tmp/deploy_stdout.txt', 'w') as f: # This can be output for splunk, nr logging, etc
            process = subprocess.Popen(deployBashCommand.split(), stdout=f, stderr=subprocess.DEVNULL) # We can change DEVNULL to PIPE for errors
            result = process.communicate()

            print("DEPLOY is finished. stderr is: ", result)

    def destroy(self):
        print("This is going to bring down docker-compose")

        destroyBashCommand = "docker-compose -f ../docker-compose.yml down"

        with open ('../tmp/destroy_stdout.txt', 'w') as f: # This can be output for splunk, nr logging, etc
            process = subprocess.Popen(destroyBashCommand.split(), stdout=f, stderr=subprocess.DEVNULL) # We can change DEVNULL to PIPE for errors
            result = process.communicate()

            print("DESTROY is finished. stderr is: ", result)



if __name__ == '__main__':
    jfrog()