"""Evaluating the partition result."""

from param_parser import parameter_parser
from utils import read_partition, Target
from eval_method import cal_f_score, cal_purity 

def main():
    args = parameter_parser()
    partition = read_partition(args.membership_path)
    target = Target(args.target_path)
    
    if args.eval_method == 'F-score':
        score = cal_f_score(partition, target)
    elif args.eval_method == 'purity':
        score = cal_purity(partition, target)
    else:
        raise NotImplementedError('Measurement %s has not been implemented yet.' 
                                    % args.eval_method)
    
    print("\nMeasurement = %s, Score = %f" % (args.eval_method, score))

if __name__ == '__main__':
    main()
