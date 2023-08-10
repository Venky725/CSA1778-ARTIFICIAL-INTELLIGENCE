def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    hanoi(n-1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n-1, auxiliary, source, destination)
if __name__ == "__main__":
    num_disks = 3
    source_peg = "A"
    auxiliary_peg = "B"
    destination_peg = "C"

    hanoi(num_disks, source_peg, auxiliary_peg, destination_peg)
