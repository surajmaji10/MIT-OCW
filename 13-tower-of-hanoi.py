# this is a sample code from MIT OCW 18.00

# a simple recursive implementation of a quite complext task
# hanoi ---> monk reside in a monastery with 64 disks and 3 towers

def hanoi(ndisks, source, destination, spare):
    if ndisks == 1:
        print("Move disk from {} => {}".format(source, destination))
        return
    hanoi(ndisks-1, source, spare, destination)
    hanoi(1, source, destination, spare)
    hanoi(ndisks-1, spare, destination, source)

n = int(input("Enter number of disks:"))
hanoi(ndisks=n, source="SRC", destination="DEST", spare="EXT")
