# 5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

def towerofhanoi(disk , from_rod, to_rod, aux_rod):
    if disk == 0:
        return
    towerofhanoi(disk-1 , from_rod, aux_rod, to_rod)
    print("Move disk", disk , "from rod", from_rod, "to rod", to_rod)
    towerofhanoi(disk-1 , aux_rod, to_rod, from_rod)
 
 
disk = int(input("Enter no. of disks :"))
from_rod = input("Enter name of first rod :")
to_rod = input("Enter name of second rod :")
aux_rod = input("Enter name of third rod :")
towerofhanoi(disk, from_rod , to_rod , aux_rod)