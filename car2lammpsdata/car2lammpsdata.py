import argparse
from ase.data import atomic_numbers, atomic_masses
from collections import Counter


def readcar(carfile):
    crds = []
    symbols = []
    b = False
    with open(carfile) as f:
        for line in f:
            s = line.split()
            if s[0] == 'PBC':
                box = list(map(float, s[1:4]))
                b = True
            elif b and len(s) == 9:
                crds.append(list(map(float, s[1:4])))
                symbols.append(s[-2])
    return crds, symbols, box


def write(datafile, crds, symbols, box, symbollist=None):
    buff = ['by Jinzhe Zeng']
    buff.append(f'{len(symbols)} atoms')
    if symbollist is None:
        symbollist = list(Counter(symbols))
    buff.append(f'{len(symbollist)} atom types')
    buff.extend([f'0 {box[i]} {d}lo {d}hi' for i,
                 d in enumerate(['x', 'y', 'z'])])
    buff.extend(['Masses', ''])
    buff.extend([f'{i} {atomic_masses[atomic_numbers[s]]}' for i,
                 s in enumerate(symbollist, 1)])
    buff.extend(['Atoms', ''])
    symbolindex = dict(zip(symbollist, range(1, len(symbollist)+1)))
    buff.extend([f'{i} {symbolindex[s]} 0 {c[0]} {c[1]} {c[2]}' for i,
                 (c, s) in enumerate(zip(crds, symbols), 1)])
    with open(datafile, 'w') as f:
        f.write('\n'.join(buff))


def convert(carfile, datafile, symbollist):
    write(datafile, *readcar(carfile), symbollist)


def _commandline():
    parser = argparse.ArgumentParser(description='car to lammps-data')
    parser.add_argument('-i', '--carfile',  required=True)
    parser.add_argument('-o', '--datafile',  required=True)
    parser.add_argument('-a', '-s', '--symbol', nargs='*')
    args = parser.parse_args()
    convert(args.carfile, args.datafile, symbollist=args.symbol)


if __name__ == '__main__':
    _commandline()
