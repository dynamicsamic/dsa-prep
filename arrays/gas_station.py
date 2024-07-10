def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    """
    Leetcode. 134. Gas station.
    https://leetcode.com/problems/gas-station/description

    -----------------------------Description-----------------------------------
    There are n gas stations along a circular route, where the amount of gas at
    the ith station is gas[i]. You have a car with an unlimited gas tank and it
    costs cost[i] of gas to travel from the ith station to its next (i + 1)th
    station. You begin the journey with an empty tank at one of the gas stations.
    Given two integer arrays gas and cost, return the starting gas station's
    index if you can travel around the circuit once in the clockwise direction,
    otherwise return -1. If there exists a solution, it is guaranteed
    to be unique

    -----------------------------Constraints-----------------------------------
    : n == gas.length == cost.length
    : 1 <= n <= 10**5
    : 0 <= gas[i], cost[i] <= 10**4

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
    Output: 3
    Explanation:
    Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
    Travel to station 4. Your tank = 4 - 1 + 5 = 8
    Travel to station 0. Your tank = 8 - 2 + 1 = 7
    Travel to station 1. Your tank = 7 - 3 + 2 = 6
    Travel to station 2. Your tank = 6 - 4 + 3 = 5
    Travel to station 3. The cost is 5. Your gas is just enough to travel 
    back to station 3.
    Therefore, return 3 as the starting index.

    Example 2:
    Input: gas = [2,3,4], cost = [3,4,3]
    Output: -1
    Explanation:
    You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
    Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
    Travel to station 0. Your tank = 4 - 3 + 2 = 3
    Travel to station 1. Your tank = 3 - 3 + 3 = 3
    You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
    Therefore, you can't travel around the circuit once no matter where you start.


    ------------------------------Algorithm------------------------------------
    This algorithm is divided in two parts. At first we iterate over two arrays
    and find their sums. We compare two sums, and if cost sum is higher than
    gas sum, then obvioulsy we can't comlete a circuit.
    After the succefful comparison we know that somewhere in the arrays exists
    a point at which the tank sum never goes beyond zero. So we iterate over
    two arrays again and if we find a point at which our tank goes beyond zero,
    that means that this is not the station we are looking for. So we say,
    our station is the next coming station. At last we will find one.
    """

    length = len(gas)
    total_gas = sum(gas)
    total_cost = sum(cost)

    if total_gas < total_cost:
        return -1

    station_idx = 0
    tank = 0

    for j in range(length):
        tank += gas[j] - cost[j]
        if tank < 0:
            tank = 0
            station_idx = j + 1

    return station_idx


assert can_complete_circuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]) == 4
assert can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
assert can_complete_circuit([2, 3, 4], [3, 4, 3]) == -1
assert can_complete_circuit([3, 1, 1], [1, 2, 2]) == 0
assert can_complete_circuit([2], [2]) == 0

print("\nAll tests passed\n")
