def get_crossed_wires():
    crossed_wires = ['z05', 'hdt', 'z09', 'gbf', 'mht', 'jgt', 'z30', 'nbf']
    return crossed_wires


if __name__ == '__main__':
    crossed_wires = get_crossed_wires()
    sorted_crossed_wires = sorted(crossed_wires)
    output = ','.join(sorted_crossed_wires)
    print(output)

