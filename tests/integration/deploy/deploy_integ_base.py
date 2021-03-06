import os
import uuid
import json
import time
from pathlib import Path
from unittest import TestCase

import boto3


class DeployIntegBase(TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        super(DeployIntegBase, self).setUp()

    def tearDown(self):
        super(DeployIntegBase, self).tearDown()

    def base_command(self):
        command = "sam"
        if os.getenv("SAM_CLI_DEV"):
            command = "samdev"

        return command

    def get_deploy_command_list(
        self,
        s3_bucket=None,
        stack_name=None,
        template=None,
        template_file=None,
        s3_prefix=None,
        capabilities=None,
        force_upload=False,
        notification_arns=None,
        fail_on_empty_changeset=None,
        confirm_changeset=False,
        no_execute_changeset=False,
        parameter_overrides=None,
        role_arn=None,
        kms_key_id=None,
        tags=None,
        profile=None,
        region=None,
        guided=False,
    ):
        command_list = [self.base_command(), "deploy"]

        if guided:
            command_list = command_list + ["--guided"]
        if s3_bucket:
            command_list = command_list + ["--s3-bucket", str(s3_bucket)]
        if capabilities:
            command_list = command_list + ["--capabilities", str(capabilities)]
        if parameter_overrides:
            command_list = command_list + ["--parameter-overrides", str(parameter_overrides)]
        if role_arn:
            command_list = command_list + ["--role-arn", str(role_arn)]
        if notification_arns:
            command_list = command_list + ["--notification-arns", str(notification_arns)]
        if stack_name:
            command_list = command_list + ["--stack-name", str(stack_name)]
        if template:
            command_list = command_list + ["--template", str(template)]
        if template_file:
            command_list = command_list + ["--template-file", str(template_file)]
        if s3_prefix:
            command_list = command_list + ["--s3-prefix", str(s3_prefix)]
        if kms_key_id:
            command_list = command_list + ["--kms-key-id", str(kms_key_id)]
        if no_execute_changeset:
            command_list = command_list + ["--no-execute-changeset"]
        if force_upload:
            command_list = command_list + ["--force-upload"]
        if fail_on_empty_changeset is None:
            pass
        elif fail_on_empty_changeset:
            command_list = command_list + ["--fail-on-empty-changeset"]
        else:
            command_list = command_list + ["--no-fail-on-empty-changeset"]
        if confirm_changeset:
            command_list = command_list + ["--confirm-changeset"]
        if tags:
            command_list = command_list + ["--tags", str(tags)]
        if region:
            command_list = command_list + ["--region", str(region)]
        if profile:
            command_list = command_list + ["--profile", str(profile)]

        return command_list
