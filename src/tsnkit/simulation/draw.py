import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from typing import List, Tuple


def calc_delay_jitter(
    log: List[List[List[int]]],
) -> Tuple[List[List[int]], List[List[int]]]:
    ## [[frame1, frame2, ...], [frame1, frame2, ...], ...]
    flow_delays: List[List[int]] = []
    flow_jitters: List[List[int]] = []

    for flow_log in log:
        delays: List[int] = []
        jitters: List[int] = []

        release_time = flow_log[0]
        arrival_time = flow_log[1]

        for frame_id in range(0, len(release_time)):
            if frame_id < len(arrival_time):
                delays.append(arrival_time[frame_id] - release_time[frame_id])
                if frame_id > 0:
                    jitters.append(abs(delays[frame_id] - delays[frame_id - 1]))
            else:
                delays.append(0)
                jitters.append(0)

        flow_delays.append(delays)
        flow_jitters.append(jitters)

    return flow_delays, flow_jitters


def draw(log: List[List[List[int]]]) -> None:
    """
    Draw the delay and jitter of each stream in time-series.
    """

    flow_delays, flow_jitters = calc_delay_jitter(log)

    plt.figure(figsize=(12, 4))

    ## Draw delays
    # Flatten the list and create a DataFrame
    values = [item[0] for item in flow_delays]
    df = pd.DataFrame({'Index': range(len(values)), 'Value': values})

    plt.subplot(1, 2, 1)
    # Plot horizontal lines
    for i, value in enumerate(values):
        sns.lineplot(x=[0, len(values) - 1], y=[value, value], label=f'flow{i}')
    # for i in range(len(flow_delays)):
    #     sns.lineplot(x=range(len(flow_delays[i])), y=flow_delays[i][0], label=f"flow{i}")
    # Set x-axis labels
    plt.xticks(range(len(values)), [f'{i}' for i in range(len(values))])
    plt.title("Simulated delay")
    plt.xlabel("Pkt index")
    plt.ylabel("Delay (ns)")
    plt.legend()

    ## Draw jitters
    plt.subplot(1, 2, 2)
    for i in range(len(flow_jitters)):
        sns.lineplot(x=range(len(flow_jitters[i])), y=flow_jitters[i], label=f"flow{i}")
    plt.title("Simulated jitter")
    plt.xlabel("Pkt index")
    plt.ylabel("Jitter (ns)")
    plt.show()
