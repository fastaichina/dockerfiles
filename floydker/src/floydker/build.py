#!/usr/bin/env python
# -*- coding:utf-8 -*-

from subprocess import check_call, check_output
import os
import logging
import click
import click_log
from .utils import assert_image_tag_from_dockerfile

logger = logging.getLogger(__name__)


@click.command()
@click.argument('dockerfile')
@click_log.simple_verbosity_option()
@click_log.init(__name__)
def build(dockerfile):
    image_tag = assert_image_tag_from_dockerfile(logger, dockerfile)
    dockerfile_dir = os.path.dirname(dockerfile)
    logger.info('--------------------------------------------')
    logger.info('[*] Building %s with tag %s...', dockerfile, image_tag)
    logger.info('--------------------------------------------')
    check_call('docker build -t %s -f %s %s' % (image_tag,
                                                dockerfile,
                                                dockerfile_dir),
               shell=True)
    logger.info(check_output(['docker', 'images']))
