import pseudorandom_number_generation.uniform.generators as prng
from util import test_speed_lcg

func_map = {
    "RANDU" : prng.randu,
    "modified RANDU 1": prng.randu_custom_1,
    "modified RANDU 2": prng.randu_custom_2,
    "modified RANDU 3": prng.randu_custom_3
}

for key, value in func_map.items():
    test_speed_lcg(value, key, 3000, 1000)
