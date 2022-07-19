import Play

def Solution():     #For TestTubes1_1
#    solution = [(0,3),(2,3),(2,3),(2,4),(0,2),(1,2),(1,2),(0,3),(0,1),(4,1)]
#    solution = [(0, 4), (1, 3), (1, 3), (2, 4), (2, 4), (2, 1), (2, 3), (0, 3), (0, 4), (0, 1)]
    solution = [(4, 6), (0, 6), (2, 5), (2, 6), (4, 2), (1, 4), (1, 4), (1, 5), (0, 1), (0, 1), (2, 0), (2, 0), (2, 6), (3, 0), (3, 5), (3, 1), (3, 5)]
    return solution

def main():
    printAll,tubes = Play.Config()
    solution = Solution()
    currentStatus = Play.MakeStatus(tubes)
    for move in solution:
        if printAll:
            print(currentStatus.Show())
        currentStatus.Move(move)
    print(currentStatus.Show())

if __name__ == "__main__":
    main()
