from collections import namedtuple

NEXT_ACTIVITY = 'next_activity'
REMAINING_TIME = 'remaining_time'
ATTRIBUTE_NUMBER = 'attribute_number'
ATTRIBUTE_STRING = 'attribute_string'
NO_LABEL = 'no_label'
DURATION = 'duration'

THRESHOLD_MEAN = 'threshold_mean'
THRESHOLD_CUSTOM = 'threshold_custom'

CLASSIFICATION_LABELS = [NEXT_ACTIVITY, ATTRIBUTE_STRING, ATTRIBUTE_NUMBER, THRESHOLD_MEAN, THRESHOLD_CUSTOM]

REGRESSION_LABELS = [REMAINING_TIME, ATTRIBUTE_NUMBER]

TIME_SERIES_PREDICTION_LABELS = [NEXT_ACTIVITY]  # TODO: check for using NO_LABEL


class LabelContainer(namedtuple('LabelContainer', ['type', 'attribute_name', 'threshold_type', 'threshold',
                                                   'add_remaining_time', 'add_elapsed_time', 'add_executed_events',
                                                   'add_resources_used', 'add_new_traces'])):
    """Inner object describing labelling state.
    For no labelling use NO_LABEL

    This is a horrible hack and should be split into a label container and a container for encoding options, like
    what to add to the encoded log.
    """

    def __new__(cls, type: str = REMAINING_TIME, attribute_name: str = None, threshold_type: str = THRESHOLD_MEAN,
                threshold: int = 0, add_remaining_time: bool = False, add_elapsed_time: bool = False,
                add_executed_events: bool = False, add_resources_used: bool = False, add_new_traces: bool = False):
        # noinspection PyArgumentList
        return super(LabelContainer, cls).__new__(cls, type, attribute_name, threshold_type, threshold,
                                                  add_remaining_time, add_elapsed_time, add_executed_events,
                                                  add_resources_used, add_new_traces)