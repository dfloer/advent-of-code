def day24_split():
    with open('day24.txt', 'r') as f:
        lines = f.readlines()
    return lines


def day24():
    package_weights = [int(x) for x in day24_split()]
    #result = [[0], [0], [0]]
    container_sum = [0, 0, 0]
    container_prod = [1, 1, 1]
    # The algorithm I'm trying here is to take the items, largest to smallest and put them in the bin that is lightest.
    sorted_weights = sorted(package_weights)[::-1]
    for package in sorted_weights:
        lightest_value = min(container_sum)
        lightest_container = container_sum.index(lightest_value)

        container_sum[lightest_container] += package
        container_prod[lightest_container] *= package
    print(container_sum, container_prod)


