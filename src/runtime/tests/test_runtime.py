import os
import signal
import subprocess

from time import sleep

from django.test.testcases import TestCase

from src.jobs.models import JobTypes, Job
from src.jobs.tasks import prediction_task
from src.runtime.tasks import runtime_task, replay_task
from src.split.models import SplitTypes, SplitOrderingMethods
from src.utils.django_orm import duplicate_orm_row
from src.utils.tests_utils import create_test_job, create_test_split, create_test_log


class TestRuntime(TestCase):

    def test_replay(self):

        job = create_test_job()
        runtime_job = duplicate_orm_row(job)

        runtime_log = create_test_log(log_name='runtime_example.xes',
                                      log_path='cache/log_cache/test_logs/runtime_test.xes')
        runtime_job.split = create_test_split(split_type=SplitTypes.SPLIT_DOUBLE.value,
                                              split_ordering_method=SplitOrderingMethods.SPLIT_SEQUENTIAL.value,
                                              train_log=runtime_log,
                                              test_log=runtime_log)

        requests = replay_task(runtime_job, job)
        self.assertEqual(len(requests), 6)

    def test_runtime(self):
        job = create_test_job(create_models=True)
        runtime_log = create_test_log(log_name='runtime_example.xes',
                                      log_path='cache/log_cache/test_logs/runtime_test.xes')

        prediction_task(job.id)
        job.refresh_from_db()
        job.split = create_test_split(split_type=SplitTypes.SPLIT_DOUBLE.value,
                                      split_ordering_method=SplitOrderingMethods.SPLIT_SEQUENTIAL.value,
                                      train_log=runtime_log,
                                      test_log=runtime_log)

        runtime_task(job)