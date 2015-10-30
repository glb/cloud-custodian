import os
import sys


def identify(options, policy_collection):

    fh = sys.stdout

    for policy in policy_collection:
        manager = policy.resource_manager
        resources = manager.resources()
        print manager.format_json(resources, fh)

    
def run(options, policy_collection):
    for policy in policy_collection:
        policy()
        

