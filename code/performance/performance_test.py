import multiprocessing
import os
import time


def test(num_instances):
    start = time.time()

    procs = multiprocessing.Pool(num_instances)
    r = procs.map_async(os.system,
                        [f"venv\\Scripts\\python .\\code\\performance\\ingestor_with_metrics.py" for _ in
                         range(num_instances)])

    p = multiprocessing.Process(target=os.system, args=("venv\\Scripts\\python .\\code\\sensor.py 100",))
    p.start()
    p.join()
    r.wait()

    end = time.time()
    duration = end - start
    throughput = 100 * num_instances / duration

    with open("logs/ingestor.log", "r") as f:
        ingestor_logs = f.readlines()
        ingestor_logs = [x.strip() for x in ingestor_logs]
        ingestor_logs = [x for x in ingestor_logs if x]

    with open("logs/ingestor.log", "w") as f:
        f.write("")

    avg_response_times = [float(x) for x in ingestor_logs]
    avg_response_time = sum(avg_response_times) / len(avg_response_times)

    with open("logs/performance_1.log", "a") as f:
        f.write(f"{num_instances},{duration},{throughput},{avg_response_time}\n")


if __name__ == "__main__":
    for _ in range(4):
        for i in [1, 2, 3, 5, 7, 10, 15, 20, 30]:
            test(i)
            time.sleep(5)
