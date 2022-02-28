"""Calculate serveral custering measures according to: https://zhuanlan.zhihu.com/p/343667804"""

from scipy.special import comb

def __cal_distribution(nodes, target):
    """Calculate real label distibution in a set of nodes"""
    dis = {}
    for node in nodes:
        temp = target.label[node]
        dis[target.label[node]] = dis.get(target.label[node], 0) + 1
    return dis, len(nodes)

def cal_purity(partition, target):
    """Calculate purity measurement."""
    correct_count = 0
    false_count = 0
    total_count = 0

    for part, nodes in partition.items():
        temp_dis, size = __cal_distribution(nodes, target)

        max_count = 0

        for cls, count in temp_dis.items():
            if count > max_count:
                max_count = count
        correct_count += max_count
        false_count += size - correct_count
        total_count += size

        print("size=%d, local_purity=%f" %(size, max_count/(size+0.)))

    print('labeled nodes: %d, percentage: %f' % (total_count, total_count/(len(target)+0.)))

    return correct_count/total_count


def cal_f_score(partition, target, beta=1.):
    """Calculate F-Score measurement."""

    TP = 0
    FP = 0
    # TN = 0
    FN = 0

    print("\nEvaluating F-Score.")

    acc_real_dis = {}

    for part, nodes in partition.items():
        temp_dis, size = __cal_distribution(nodes, target)

        temp_TP = 0
        for label, count in temp_dis.items():
            temp_TP += comb(count, 2) if count > 1 else 0

            if label not in acc_real_dis:
                acc_real_dis[label] = count
            else:
                acc_real_dis[label] += count
        
        TP += temp_TP
        FP += comb(size, 2) - temp_TP

    for label, count in acc_real_dis.items():
        FN += comb(count, 2)
    FN = FN - TP

    print("TP=%d, FP=%d, FN=%d" %(TP, FP, FN))

    # TN = comb(len(target), 2) - TP - FP - FN

    precision = TP/(TP+FP+0.)
    recall = TP/(TP+FN+0.)

    print("precision=%f, recall=%f" % (precision, recall))

    return (1+beta**2)*(precision*recall)/(beta**2*precision+recall)