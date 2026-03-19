from random import random

class Imitator:
    def __init__(self, *args, request_count=7):
        if len(args) == 1 and isinstance(args[0], (list, tuple)):
            self.t1_min, self.t1_max, self.t2_min, self.t2_max = args[0]
        elif len(args) == 4:
            self.t1_min, self.t1_max, self.t2_min, self.t2_max = args
        self.request_count = request_count

    def check_loads(
            self,
            request_times: list[float]=None,
            processed_times: list[float]=None,
            draw: bool = False
    ) -> float:
        if not request_times:
            request_times = self.get_request_times()
        if not processed_times:
            processed_times = self.get_processed_times()
        failed_count = 0
        delay = 0
        print('T1', request_times)
        print('t2', processed_times)

        for i in range(self.request_count):
            if i not in (0, self.request_count):
                current_request_time = request_times[i]

                if delay != 0:
                    print(f'Запрос №{i} в {current_request_time} не обработан из-за задержки')
                    print('-' * 40)
                    failed_count += 1
                    continue

                delay = self._get_delay(
                    current_request_time=current_request_time,
                    next_request_time=request_times[i+1],
                    processed_time=processed_times[i],
                    delay=delay
                )
                status_string = self._get_load_status_string(delay)
                print(f'Запрос №{i} в {current_request_time} {status_string}')
                print('-' * 40)
        process_probability = ((self.request_count-1) - failed_count) / (self.request_count-1)
        print(f'Вероятность обработки: {process_probability}')
        if failed_count != 0:
            print(f'Не обработано запросов: {failed_count}')
        else:
            print('Все запросы обработаны!')
        return process_probability

    @staticmethod
    def _get_load_status_string(delay: float):
        return 'обработан вовремя' if delay == 0 else f'обработан с задержкой {delay} сек.'

    @staticmethod
    def _get_delay(current_request_time: float, next_request_time: float, processed_time: float, delay: float) -> float:
        process_end_time = current_request_time + processed_time + delay
        print(f'Приход в {current_request_time}. Уход в {process_end_time}')
        if process_end_time > next_request_time:
            return process_end_time - next_request_time
        return 0

    def T1(self, i) -> float:
        if i == 0:
            return 0
        return self.T1(i - 1) + (self.t1_max - self.t1_min) * random() + self.t1_min

    def t2(self) -> float:
        return (self.t2_max - self.t2_min) * random() + self.t2_min

    def get_request_times(self) -> list[float]:
        return [self.T1(i) for i in range(self.request_count+1)]

    def get_processed_times(self) -> list[float]:
        return [0] + [self.t2() for i in range(self.request_count)]

#

im = Imitator(1, 4, 1, 4)
im.check_loads(
    # request_times=[0, 0.151, 3.021, 4.868, 6.324, 8.307, 10.046, 11.242],
    # processed_times=[0, 1.457, 1.098, 1.094, 1.931, 1.895, 1.227, 1.441]
    # processed_times=[0, 1.334, 1.158, 1.153, 1.054, 1.426, 1.077, 1.041],
)
