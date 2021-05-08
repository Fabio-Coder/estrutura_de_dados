from time import perf_counter_ns, perf_counter


def cronometro_ns():
    return perf_counter_ns()


def cronometro():
    return perf_counter()
