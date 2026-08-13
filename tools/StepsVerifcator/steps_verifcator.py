from typing import Optional


class TesStepsVerifcator:
    def __init__(self,
                 expected_results=None,
                 received_results=None):

        if expected_results is None:
            expected_results = []
        if received_results is None:
            received_results = []

        self.expected_results = expected_results
        self.received_results = received_results

    def add_test(self,
                 condition: bool,
                 fail_msg: Optional[str]):

        if fail_msg is not None:
            self.received_results.append(condition if condition else fail_msg)
        else:
            self.received_results.append(condition)

        self.expected_results.append(True)

    def is_last_result_failed(self) -> bool :
        if isinstance(self.received_results[-1], str) or  not self.received_results[-1]:
            return True
        else:
            return False

    def is_any_fail(self):
        count_expected = self.expected_results.count(True)
        count_received = self.received_results.count(True)

        return count_received != count_expected

if __name__ == '__main__':
    a = TesStepsVerifcator()
    a.add_test(condition=False,
               fail_msg='XYZ')

    a.add_test(condition=True,
               fail_msg='XYZ1')

    info = a.is_last_result_failed()
    info2_  = a.is_any_fail()

    pass



