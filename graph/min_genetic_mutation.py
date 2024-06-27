from collections import deque


def min_genetic_mutation(
    start_gene: str, end_gene: str, bank: list[str]
) -> int:
    """
    Leetcode. 433. Minimum Genetic Mutation
    https://leetcode.com/problems/minimum-genetic-mutation/description

    -----------------------------Description-----------------------------------
    A gene string can be represented by an 8-character long string, with
    choices from 'A', 'C', 'G', and 'T'.
    Suppose we need to investigate a mutation from a gene string startGene
    to a gene string endGene where one mutation is defined as one single
    character changed in the gene string.

        For example, "AACCGGTT" --> "AACCGGTA" is one mutation.

    There is also a gene bank bank that records all the valid gene mutations.
    A gene must be in bank to make it a valid gene string.
    Given the two gene strings startGene and endGene and the gene bank bank,
    return the minimum number of mutations needed to mutate from startGene
    to endGene. If there is no such a mutation, return -1.
    Note that the starting point is assumed to be valid, so it might
    not be included in the bank.

    -----------------------------Constraints-----------------------------------
    : 0 <= bank.length <= 10
    : startGene.length == endGene.length == bank[i].length == 8
    : startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
    Output: 1

    Example 2:
    Input: startGene = "AACCGGTT", endGene = "AAACGGTA",
    bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
    Output: 2

    ------------------------------Algorithm------------------------------------
    Problem flow is kind of similar to breadth first search.
    We start with empty `queue` and empty `seen` set to track gene mutations
    already seen during the algorithm execution.
    We add our starting element and mutation counter (which is 0 from the start)
    in the queue and start the main loop. In the main loop we pop the leftmost
    element from the queue, compare it with the desired `end_gene` string
    and if they match we return the mutation counter. We also add this current
    gene to seen in order to skip in the future.
    After that we compare the current gene with every gene in our gene bank
    and if we find a gene that differs by ONLY one character, it means that
    we found next valifd mutation of our current gene, hence we increment
    mutation counter and add it together with the found gene to the queue.
    We repeat this pocess while the queue is not empty.
    By that time we will have proccessed all the mutations from the bank,
    counted and returned the counter.
    If we reached the end of the loop without returning, it means that
    no sequence of valid mutations is present in the bank.
    """
    seen = set()
    queue = deque()

    queue.append((start_gene, 0))

    while queue:
        current_gene, count = queue.popleft()
        if current_gene == end_gene:
            return count

        seen.add(current_gene)

        for gene in bank:
            diff = 0
            for i in range(len(current_gene)):
                if current_gene[i] != gene[i]:
                    diff += 1
            if gene not in seen and diff == 1:
                queue.append((gene, count + 1))

    return -1


st = "AACCGGTT"
en = "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
assert min_genetic_mutation(st, en, bank) == 2


st = "AAAAACCC"
en = "AACCCCCC"
bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
assert min_genetic_mutation(st, en, bank) == 3

st = "AACCGGTT"
en = "AACCGGTA"
bank = ["AACCGGTA"]
assert min_genetic_mutation(st, en, bank) == 1
