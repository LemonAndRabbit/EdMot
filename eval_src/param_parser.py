"""Parameter parsing from the command line."""

import argparse

def parameter_parser():
    """
    A method to parse up command line parameters. By default it trains on the Cora dataset.
    The default hyperparameters give a good quality representation without grid search.
    """
    parser = argparse.ArgumentParser(description="Run EdMot Eval.")


    parser.add_argument("--eval-method",
                        nargs="?",
                        default="F-score",
                    help="Method to eval partition result.")

    parser.add_argument("--target-path",
                        nargs="?",
                        default="./input/cora_target.csv",
	                help="Target community CSV.")

    parser.add_argument("--membership-path",
                        nargs="?",
                        default="./output/cora_membership1.json",
	                help="Cluster memberhip json.")
    
    return parser.parse_args()
