# Similar to nskip version but skip O(n^2) algorithms for n > threshold
import random, time
from app_fullcomparison_nskip import ALGORITHMS, time_it, validate_sorted

def run_all(skip_threshold=1500):
    sizes = [100, 500, 2000]
    trials = 2
    for n in sizes:
        print(f"\nDataset size: {n}")
        data = [random.randint(0, n*10) for _ in range(n)]
        for name, fn in ALGORITHMS.items():
            if name in ('selection', 'bubble') and n > skip_threshold:
                print(f"{name:10} | skipped for n={n}")
                continue
            total = 0.0; ok = True
            for t in range(trials):
                ttime, out = time_it(fn, data[:])
                total += ttime
                if not validate_sorted(out):
                    ok = False
            avg = total / trials
            print(f"{name:10} | avg {avg:.6f}s | valid: {ok}")


if __name__ == '__main__':
    run_all()
