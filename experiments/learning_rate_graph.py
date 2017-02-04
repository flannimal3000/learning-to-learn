import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main(argv):
    fn = 'polynomial-sgd-discrete-dqn.csv'
    df = pd.read_csv(fn)
    epoch = df["epoch"].as_matrix()
    iteration = df["iteration"].as_matrix()
    # loss_train
    # loss_val
    nl_lr = df["nl_lr"].as_matrix()
    lr = np.exp(-nl_lr)
    min_epoch = np.min(epoch, axis=None)
    max_epoch = np.max(epoch, axis=None)
    iters = np.max(iteration, axis=None)
    data = np.zeros((iters + 1, max_epoch - min_epoch + 1))
    for e in range(min_epoch, max_epoch + 1):
        d = lr[np.where(epoch == e)]
        data[:, e - min_epoch] = d
    avg = np.mean(data, axis=1)
    idx = np.arange(0, iters + 1)

    # Plot each trial
    fig = plt.figure()
    plt.plot(idx, data)
    plt.xlabel("Epoch")
    plt.ylabel("Learning Rate")
    plt.xlim(0, iters)
    fig.savefig("learning_rate.png")
    plt.close(fig)

    # Plot average
    fig = plt.figure()
    plt.plot(idx, avg)
    plt.xlabel("Epoch")
    plt.ylabel("Average Learning Rate")
    plt.xlim(0, iters)
    fig.savefig("learning_rate_avg.png")
    plt.close(fig)


if __name__ == "__main__":
    main(sys.argv[1:])