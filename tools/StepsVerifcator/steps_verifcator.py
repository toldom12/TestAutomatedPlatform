from typing import Optional


class StepsVerifcatorNotResponsibleLength(Exception):
    pass   



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

    def is_any_fail(self) -> bool:
        count_expected = self.expected_results.count(True)
        count_received = self.received_results.count(True)

        return count_received != count_expected

    def cleanup(self):
        if len(sel.received_results) != len(self.expected_results):
            for index, value_expected_results in enumerate(self.expected_results):
                if value_expected_results == self.received_results[index]:
                    self.expected_results.pop(index)
                    self.received_results.pop(index)
                else: 
                    pass
        else:
            raise StepsVerifcatorNotResponsibleLength(f'not correctly length,received {self.received_results}, expected: {self.expected_results}')
    

if __name__ == '__main__':
    a = TesStepsVerifcator()
    a.add_test(condition=True,
               fail_msg='XYZ')

    a.add_test(condition=True,
               fail_msg='XYZ1')

    a.add_test(condition=True,
               fail_msg='XYZ1')
    
    a.add_test(condition=True,
               fail_msg='XYZ1')

    a.cleanup()

    pass 

    info = a.is_last_result_failed()
    info2_  = a.is_any_fail()
    print(info2_)

    pass



