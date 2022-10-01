import pyperf
from PathFactory import PathFactory as pf
import metrics_extractor as me
import bm_time_data as btd

def do_bench(alg, gr, bench_data):
    runner = pyperf.Runner()
    path_finder = pf.build(alg)
    runner.bench_func(alg, path_finder, bench_data)