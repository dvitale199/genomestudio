from multiprocessing import Pool
import subprocess
import argparse

parser = argparse.ArgumentParser(description='Arguments for Genotype Calling with Illumina CLI')
parser.add_argument('--idats', type=str, default='nope', help='Path to text file with different path to idat directories on each line')
parser.add_argument('--egt', type=str, default='nope', help='Path to Cluster File')
parser.add_argument('--bpm', type=str, default='nope', help='Path to Manifest')
parser.add_argument('--out', type=str, default='out', help='Prefix for output (including path)')

args = parser.parse_args()
idats = args.idats
egt = args.egt
bpm = args.bpm
out = args.out


with open(idats) as file:
    paths = file.readlines()

idat_paths = [x.strip() for x in paths] 


def genotype_call(idat, bpm=bpm, egt=egt, out=out):
    command = "./executables/iaap-cli-linux-x64-1.1.0-sha.80d7e5b3d9c1fdfc2e99b472a90652fd3848bbc7/iaap-cli/iaap-cli gencall {} {} {} -f {} -p".format(bpm, egt, out, idat)
    subprocess.run(command, shell=True)


pool = Pool()
pool.map(genotype_call, idat_paths)