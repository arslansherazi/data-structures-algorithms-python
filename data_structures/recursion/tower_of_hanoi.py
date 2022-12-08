def tower_of_hanoi(disk, source_rod, dest_rod, aux_rod):
    # termination condition / base criteria
    if disk == 0:
        return

    tower_of_hanoi(disk - 1, source_rod, aux_rod, dest_rod)
    print(f'Move {disk} from {source_rod} to {dest_rod}')
    tower_of_hanoi(disk - 1, aux_rod, dest_rod, source_rod)


if __name__ == '__main__':
    no_of_disks = 3
    tower_of_hanoi(no_of_disks, source_rod='A', dest_rod='C', aux_rod='B')

# No of steps = 2 ^ no of disks - 1
