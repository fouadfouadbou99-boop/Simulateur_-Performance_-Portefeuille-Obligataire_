from modules.scenarios import (
    generate_parallel_shocks
)


def test_shocks():

    shocks = generate_parallel_shocks()

    assert -100 in shocks

    assert 100 in shocks
